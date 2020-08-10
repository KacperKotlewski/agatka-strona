<?php 

function menu($title = null, $addHeader = True)
{
    $tableOfButtonsInMenu = array(
        "Portfolio"=> "portfolio",
        "O mnie"=> "about-me",
        "Kontakt"=> "contact",
        "<i class='icon-facebook'></i>"=> "https://www.facebook.com/Lyzewa-352218608703639\" target=\"_blank",
        "<i class='icon-instagram'></i>"=> "https://www.instagram.com/lyzewa\" target=\"_blank",
    );
    echo '
    <title>'.$title.'</title>
</head>
<body class="lightMode">
    <div id="container">
    <div class="lightModeMenu" id="menuBar">
    <a href="./">
                <div id="logo" class="picFill"></div>
                </a>
                <i onclick="menuBtn(this)" id="menubutton" class="icon-menu"></i>
                <menu>';

        foreach ($tableOfButtonsInMenu as $key => $value) {
            echo "<li><a href=\"$value\"".($title==$key?"class='hovered'":"").">$key</a></li>";
        }

    echo '          <div><li id="settings">
                    <i class="icon-cog"></i>
                        <ul class="submenu">
                            './*'<li>
                                <span>jakość zdjęć</span>
                                <input type="range" min="1" max="3" value="2" class="sliderRange" id="imageQuality">
                            </li>'.*/'
                            <li onclick="darkmodeSwitch()" class="settingBtn">
                                <span id="darkModeSpan">Tryb ciemny</span><i class="icon-moon-inv" id="darkMode"></i>
                            </li>
                        </ul>
                    </li>
                    './*'<li id="searchBar">
                    <i class="icon-search"></i>
                        <ul class="submenu">
                            <li>
                                <form id="searchForm">
                                    <input type="input" placeholder="Czego szukasz, przyjacielu?" class="textInp" id="searchInput">
                                    <input type="submit" value="Szukaj" id="searchBtn">
                                </form>
                            </li>
                        </ul>
                    </li>'.*/'
                    </div>
                </menu>'.
                ($addHeader == True?'<header><h1>'.$title.'</h1></header>':"")
            .'</div>
            <div id="menuback"></div>
            <div id="main">'; 
    echo "<script>
    title$title isDark = ".(isset($_COOKIE["isDark"])?$_COOKIE["isDark"]:"false")."; 
    darkmodeSet();
    </script>";
}?>