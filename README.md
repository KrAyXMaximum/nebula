<html lang="en"><head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Discord/twitter meta -->
        <meta name="theme-color" content="#4585ed">
        <meta content="Roblox Status Live" property="og:title">
        <meta content="The smarter alternative to the Roblox Status Page." property="og:description">
        <meta content="/s/favicon.png" property="og:image">

        <!-- Norton Safeweb (ew) -->
        <meta name="norton-safeweb-site-verification" content="8jogce-47v058kipk24l326g2u3epy3h4zb4-v1aop1eg0ymgmaxmzghaco0xsur0xlywu7-nb5r3dgrth9nxttgx8azw0bvpd9ucaqk4nddypll6o7l3olnmy3i0gbh">

        <!-- CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css" rel="stylesheet">
        <style>

            /* iiPython Dark Theme CSS */
            :root {

                /* Base pallet */
                --ii-fg: #bfbfbf;
                --ii-bg1: #1c1d21;
                --ii-bg2: #111214;
                --ii-gray1: #9e9e9e;
                --ii-gray2: #4b4b4b;
                --ii-gray3: #262626;

                /* Individual colors */
                --ii-red: #de2a2a;
                --ii-blue: #4585ed;
                --ii-green: #42f560;
                --ii-yellow: #bbd911;
            }

            /* RSL CSS */
            body {
                color: var(--ii-fg);
                background-color: var(--ii-bg1);
            }
            nav {
                top: 0px;
                width: 100%;
                height: 5rem;
                z-index: 999;
                display: flex;
                position: fixed;
                place-content: center;
                background-image: url("/s/img/online.png");
            }
            nav div:not(#layout-changer) {
                top: 10%;
                width: calc(100% - 70px);
                position: relative;
            }
            nav div a {
                color: black;
            }
            a {
                color: var(--ii-gray1);
                text-decoration: none;
            }
            a:hover {
                color: var(--ii-gray2);
                text-decoration: underline;
            }
            div#content {
                top: 5rem;
                width: 100%;
                padding: 20px;
                position: absolute;
                overflow-x: hidden;
                height: calc(100% - 5rem);
            }
            footer {
                left: 10px;
                bottom: 10px;
                color: #fefefe;
                position: fixed;
            }
            h1.navbar-brand a:hover {
                text-decoration: none;
            }
            h1.navbar-brand {
                margin-bottom: 0;
            }
            div.service-row {
                margin-bottom: 10px;
                justify-content: center;
            }
            div[data-rsl-id] h6 { cursor: pointer; width: fit-content; }
            div[data-rsl-id] p.card-text { font-size: 14px; }
            .service-card {
                background-color: var(--ii-gray3);
            }
            #layout-changer {
                top: 50%;
                left: 10px;
                position: absolute;
                transform: translateY(-50%);
            }

            /* Media scaling */
            @media (max-width: 1600px) {
                .col-sm-2 { width: 25%; }
            }

            /* Bootstrap custom modal dark theme */
            .bootbox-close-button {
                float: right;
            }
            .modal-content {
                background-color: var(--ii-gray3);
            }
            .modal-dialog { max-width: 650px; }
            .modal-notice {
                font-size: 12px;
                margin-top: 20px;
                margin-bottom: 0px;
            }
            .modal-notice a {
                cursor: pointer;
                color: var(--ii-blue) !important;
            }
            .modal-header {
                border-bottom: 1px solid var(--ii-bg1);
            }
            .modal-footer {
                border-top: 1px solid var(--ii-bg1);
            }

            /* API docs */
            div.endpoint-container {
                width: 100%;
            }
            div.dark-card {
                margin-bottom: 20px;
                color: var(--ii-fg);
                background-color: var(--ii-bg2);
            }
            span.badge {
                margin-right: 5px;
            } 
            h5 a:hover {
                text-decoration: none;
            }
            div.endpoint div div div.card {
                border: none;
                background-color: var(--ii-bg2);
            }
        </style>

        <link rel="icon" type="image/png" href="/s/favicon.png">
        <title>Home · Roblox Status Live</title>
    </head>
    <body>

        <!-- Header -->
        <nav style="background-image: url(&quot;/s/img/online.png&quot;);">
            
                <div id="layout-changer">
                    <a href="/grid"><i class="bi bi-grid"></i></a> <br>
                    <a href="/list"><i class="bi bi-list-ul"></i></a>
                </div>
            
            <div align="center">
                <h1 class="navbar-brand"><a href="/">
                    <span style="color: black;">Roblox Status Live</span>
                </a></h1>
                <p style="color: black;">
                    <a href="/api/docs">API docs</a> ·
                    <a href="https://github.com/RobloxStatusLive/nebula">Github</a> ·
                    <a href="https://devforum.roblox.com/t/roblox-status-live-the-better-automatic-roblox-down-detector/1567879">Devforum</a>
                </p>
            </div>
        </nav>

        <!-- Content -->
        <div id="content">
            
    <style>
        th p {
            width: fit-content;
            margin: 0;
            cursor: pointer;
        }
        footer {
            position: static;
        }
    </style>
    <table class="table table-dark">
        <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Ping</th>
                <th scope="col">Status</th>
            </tr>
        </thead>
        <tbody>
            
                <tr data-rsl-id="auth">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="auth.roblox.com">Authentication</p></th>
                    <td>323ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="devforum">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="devforum.roblox.com">Devforum</p></th>
                    <td>278ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="accountinformation">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="accountinformation.roblox.com">Account Info</p></th>
                    <td>178ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="accountsettings">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="accountsettings.roblox.com">Account Settings</p></th>
                    <td>281ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="ads">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="ads.roblox.com">Ad Service</p></th>
                    <td>319ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="assetdelivery">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="assetdelivery.roblox.com">Asset Delivery</p></th>
                    <td>290ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="avatar">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="avatar.roblox.com">Avatar Service</p></th>
                    <td>287ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="badges">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="badges.roblox.com">Badge Service</p></th>
                    <td>179ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="billing">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="billing.roblox.com">Billing Service</p></th>
                    <td>308ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="catalog">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="catalog.roblox.com">Catalog</p></th>
                    <td>305ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="cdnproviders">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="cdnproviders.roblox.com">CDN</p></th>
                    <td>285ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="chat">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="chat.roblox.com">Chat Service</p></th>
                    <td>279ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="develop">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="develop.roblox.com">Develop</p></th>
                    <td>219ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="economy">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="economy.roblox.com">Economy</p></th>
                    <td>282ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="friends">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="friends.roblox.com">Friends Service</p></th>
                    <td>293ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="gamejoin">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="gamejoin.roblox.com">Game Joining</p></th>
                    <td>179ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="games">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="games.roblox.com">Games</p></th>
                    <td>309ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="groups">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="groups.roblox.com">Groups</p></th>
                    <td>178ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="inventory">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="inventory.roblox.com">Inventory</p></th>
                    <td>191ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="locale">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="locale.roblox.com">Localization</p></th>
                    <td>299ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="metrics">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="metrics.roblox.com">Metrics</p></th>
                    <td>306ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="notifications">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="notifications.roblox.com">Notifications</p></th>
                    <td>289ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="premiumfeatures">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="premiumfeatures.roblox.com">Premium</p></th>
                    <td>186ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="privatemessages">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="privatemessages.roblox.com">Private Messages</p></th>
                    <td>282ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="publish">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="publish.roblox.com">Game Publishing</p></th>
                    <td>311ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="search">
                    
                    <th><p style="color: var(--ii-red);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="search.roblox.com">Search</p></th>
                    <td>564ms</td>
                    <td>Ping exceeds threshold</td>
                </tr>
            
                <tr data-rsl-id="textfilter">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="textfilter.roblox.com">Text Filtering</p></th>
                    <td>184ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="thumbnails">
                    
                    <th><p style="color: var(--ii-red);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="thumbnails.roblox.com">Thumbnails</p></th>
                    <td>917ms</td>
                    <td>Ping exceeds threshold</td>
                </tr>
            
                <tr data-rsl-id="trades">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="trades.roblox.com">Trading</p></th>
                    <td>179ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="twostepverification">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="twostepverification.roblox.com">2FA</p></th>
                    <td>290ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="users">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="users.roblox.com">User Service</p></th>
                    <td>285ms</td>
                    <td>No problems detected</td>
                </tr>
            
                <tr data-rsl-id="voice">
                    
                    <th><p style="color: var(--ii-green);" data-bs-toggle="tooltip" data-bs-placement="top" title="" data-bs-original-title="voice.roblox.com">Voice Chat</p></th>
                    <td>318ms</td>
                    <td>No problems detected</td>
                </tr>
            
        </tbody>
    </table>

        
            <!-- Footer -->
            <footer>
                <img src="/s/favicon.png" style="max-height: 20px;"> Nebula v1.1.2<br>
                Made with ❤️ by <a href="https://iipython.cf">iiPython</a> + <a href="https://devforum.roblox.com/u/crcoli737">Crcoli737</a>
            </footer>
        </div>

        <!-- JS -->
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js"></script>
        <script src="/s/js/bootbox.all.js"></script>
        
    <script>
        let NebulaConfig = {
            clickElement: "tr[data-rsl-id] th p",
            elementOverwriteCallback: (elems) => {
                $($(elems[0]).children()[0]).css("color", `var(--ii-${color})`);  // Service header
                $(elems[1]).text(`${Math.round(service.ping)}ms`);  // Ping time
                $(elems[2]).text(service.guess.reason);  // Guess element (.card-text)
            }
        };
    </script>
    <script>// Copyright 2022 iiPython

// Initialization
const LocaleFormatter = new Intl.DateTimeFormat("en-US", { hour12: true, hour: "2-digit", minute: "2-digit" });
const DateTimeFormatter = new Intl.DateTimeFormat("en-US", { month: "2-digit", day: "2-digit", year: "2-digit" });

$("[data-bs-toggle='tooltip']").each((i, e) => { new bootstrap.Tooltip(e); })

// Handle historical data
var historyChart = null;
let formatDate = (date = new Date()) => DateTimeFormatter.format(new Date(date)).replace(/\//g, "-");
function hsRenderDate(date) {
    let serviceID = $("#hscanvas").attr("data-rsl-id");

    // Create the chart
    $.get(`/api/day/${formatDate(date)}/${serviceID}`, {}, (r) => {
        const ctx = document.getElementById("hscanvas").getContext("2d");
        if (historyChart) historyChart.destroy();
        historyChart = new Chart(ctx, {
            type: "line",
            options: {
                responsive: false,
                maintainAspectRatio: false,
                scales: {
                    x: { title: { display: true, text: "Time" } },
                    y: { title: { display: true, text: "Ping" }, ticks: { callback: (v) => { return `${v}ms` } } }
                }
            }
        });
        historyChart.data.datasets = [{
            label: "Ping",
            data: Object.entries(r.data).map(v => { return { x: LocaleFormatter.format(v[0]), y: v[1].ping } } ),
            borderColor: "rgb(159, 159, 159)"
        }];
        historyChart.update();
    })
}
function hsRenderCustomDate() {
    bootbox.prompt({
        title: "Select date to view",
        inputType: "date",
        callback: hsRenderDate
    });
}
$(NebulaConfig.clickElement).click((e) => {
    let serviceID = $(e.currentTarget).parent().attr("data-rsl-id");
    bootbox.dialog({
        title: $(NebulaConfig.clickElement.replace("data-rsl-id", `data-rsl-id='${serviceID}'`)).text(),
        message: `
        <div><canvas id = "hscanvas" height = "450" width = "600" data-rsl-id = "${serviceID}"></canvas></div>
        <p class = "modal-notice"><a onclick = "hsRenderDate();">Today</a> · <a onclick = "hsRenderCustomDate();">Custom</a></p>
        `,
        buttons: { ok: { label: "Close", className: "btn btn-secondary", callback: () => {} } },
        onEscape: true
    })
    hsRenderDate();
})

// Handle autoreloading
setInterval(() => {
    $.get("/api/status", {}, (d) => {

        // Load status information
        $("nav").css("background-image", `url("/s/img/${d.status}.png")`);

        // Render our service data
        for (let service of Object.values(d.data)) {
            let elems = $(NebulaConfig.clickElement.replace("data-rsl-id", `data-rsl-id='${service.id}'`)).children();
            let color = { up: "green", slow: "yellow", down: "red" }[service.guess.name];

            // Update service data
            if (NebulaConfig.elementOverwriteCallback) NebulaConfig.elementOverwriteCallback(elems);
            else {
                $(elems[0]).css("color", `var(--ii-${color})`);  // Service header
                $(elems[1]).text(`${Math.round(service.ping)}ms`);  // Ping time
                $(elems[2]).text(service.guess.reason);  // Guess element (.card-text)
            }
        }
    })
}, 60000);  // 1m since our internal database doesn't update faster than that
</script>

    
</body></html>
