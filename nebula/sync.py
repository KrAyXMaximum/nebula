# Copyright 2022 iiPython

# Modules
import os
import sys
import json
import hashlib
import requests
from time import sleep

from .config import config

# Handle rich
def make_fake_rich():
    import re

    class Table(object):
        def __init__(self, **kwargs) -> None:
            self.add_column = lambda *a: None

        def add_row(self, date: str, local: str, upstream: str) -> None:
            print(f"{self.strip(date)}\t{self.strip(local)} .. {self.strip(upstream)}")

        def strip(self, value: str) -> str:
            for i in re.findall(re.compile(r"\[[^\[\]]*\]"), value):
                value = value.replace(i, "")

            return value

    class Console(object):
        def __init__(self) -> None:
            self.clear = lambda: None
            self.print = lambda *a: None

    return Table, Console

try:
    from rich.table import Table
    from rich.console import Console

except ImportError:
    Table, Console = make_fake_rich()

if config.get("nebula.plain_output", "--no-rich" in sys.argv):
    Table, Console = make_fake_rich()

# Sync class
class SyncManager(object):
    def __init__(self) -> None:
        self.upstream = f"https://{config.get('nebula.upstream')}/sync/"
        self.cache_dir = config.get("nebula.cache_dir", os.path.join(os.path.dirname(__file__), "../cache"))

        self.rcon = Console()

    def cache(self, fn: str, data: str) -> None:
        fp = os.path.join(self.cache_dir, fn)
        if not os.path.isdir(self.cache_dir):
            os.makedirs(self.cache_dir)

        with open(fp, "w+") as fh:
            fh.write(data)

    def request(self, endpoint: str) -> list | dict:
        try:
            return requests.get(self.upstream + endpoint, timeout = 2).json()

        except Exception:
            return {}

    def checksum(self, fn: str) -> str | None:
        fp = os.path.join(self.cache_dir, fn)
        if not os.path.isfile(fp):
            return None

        checksum = hashlib.md5()
        with open(fp, "rb") as fh:
            [checksum.update(c) for c in iter(lambda: fh.read(4096), b"")]

        return checksum.hexdigest()

    def sync(self) -> None:
        tb = Table(title = "Sync Status")
        [tb.add_column(c) for c in ["Date", "Local", "Upstream"]]
        for date, checksum in self.request("status").items():
            local_checksum = self.checksum(date + ".json")
            tb.add_row(f"[cyan]{date}", f"[{'green' if local_checksum == checksum else 'red'}]{local_checksum}", f"[green]{checksum}")
            if local_checksum != checksum:
                self.cache(date + ".json", json.dumps(self.request(date)))

        self.rcon.clear()
        self.rcon.print(tb)

    def loop(self) -> None:
        while True:
            self.sync()
            sleep(30)