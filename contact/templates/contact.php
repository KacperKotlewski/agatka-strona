
<?php // Check if form was submitted:
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $feedBack = null;

        // Build POST request:
        $recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify';
        $recaptcha_secret = '6LcMQcQUAAAAAHBAljTC6f1qbo2BoZTYEQpkikcq';
        $recaptcha_response = $_POST['recaptcha_response'];
        // Make and decode POST request:
        $recaptcha = file_get_contents($recaptcha_url . '?secret=' . $recaptcha_secret . '&response=' . $recaptcha_response);
        $recaptcha = json_decode($recaptcha);
        if($recaptcha->success==true){
            // Take action based on the score returned:
            if ($recaptcha->score >= 0.8 && !empty($_POST['names']) && !empty($_POST['email']) && !empty($_POST['message'])) {
                $_POST["topic"] = "[Strona/portfolio]: ".$_POST["topic"];
                $feedBack = "email send successful";
            } else {
                $feedBack = "email send failed";
            }
        }else{
            $feedBack = null;
        }
        if(session_status() != 2){
            session_start();
        }
    }
?>


<?php include_once "../php/includes/includes.php"; ?>
<link rel="stylesheet" type="text/css" href="style/pages/contact.css">

<script src="https://www.google.com/recaptcha/api.js?render=6LcMQcQUAAAAAKBWZib-WnlR0ZduVMIA_snm42Ri"></script>
<?php include_once "../php/includes/menu.php"; menu("contact"); ?>

    <div id="container">
        <section id="content">
                <form id="messageForm" method="POST">
                    <div class="halfOfForm">
                        <div class="formSection">
                            <label>Imię i nazwisko<span style="color:red;">*</span></label>
                            <input type="text" placeholder="Wpisz swoje imię i nazwisko" name="names" data-validate="required,Generic"/>
                        </div>
                        <div class="formSection">
                            <label>E-Mail<span style="color:red;">*</span></label>
                            <input type="text" placeholder="Twój e-mail" name="email" data-validate="required,Email,required" required=""/>
                        </div> 
                        <div class="formSection">
                            <label>Temat</label>
                            <input type="text" placeholder="W jakiej sprawie piszesz" name="topic" data-validate="Generic"/>
                        </div> 
                    </div>
                    <div class="halfOfForm" id="secHalfOfForm">
                        <div class="formSection">
                            <label>Wiadomość<span style="color:red;">*</span></label>
                            <textarea placeholder="Czego dusza pragnie?" name="message" data-validate="required, Generic"></textarea>
                        </div> 
                        <input type="hidden" value="" name="recaptcha_response" id="recaptchaResponse">
                        <input type="submit" id="submit" value="Wyślij wiadomość"/>
                    </div>
                </form>
        </section>
    </div>
<script>
    grecaptcha.ready(function () {
        grecaptcha.execute('6LcMQcQUAAAAAKBWZib-WnlR0ZduVMIA_snm42Ri', { action: 'contact' })
            .then(function (token) {
            var recaptchaResponse = document.getElementById('recaptchaResponse');
            console.log(recaptchaResponse);
            recaptchaResponse.value = token;
        });
    });
</script>
<?php include_once "../php/includes/footer.php";
?>