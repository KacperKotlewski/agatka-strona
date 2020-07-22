<?php include_once "../php/includes/includes.php"; ?>
<link rel="stylesheet" type="text/css" href="style/pages/aboutMe.css">
<?php include_once "../php/includes/menu.php"; menu("about me"); ?>
    <div id="container">
        <section id="content">
            <?php
            echo "<article id='images'>

            <div class='image contain autofill'>
            <div class='imgCanvas'><div class='imgContain'>
            <div class='overlay'></div>
            <div class='picFill' style='background-image: url(\"pic/"."agieta.jpg"."\");'>
            </div></div></div></div>
            
            </article>";
            $title = "Agata 'Lyzewa' Łyżwa";
            $text = "Some text";
            echo "
            <article id='aboutme'>
                <h2>$title</h2>
                <span>$text</span>
            </article>
            ";
            ?>
        </section>
        <script>
            $(document).ready(function() {
                if(mediaMaches)
                scrollToElem('#aboutme');
            });
        </script>
    </div>
<?php include_once "../php/includes/footer.php";
?>