<?php
    echo '
                <footer>
                    footer
                </footer>
            </div>
        </div>';
    if(isset($feedBack) && !empty($feedBack)){
        echo "<script>alert('".$feedBack."');</script>";
    }

    echo '
        </body>
    </html>
    ';
?>