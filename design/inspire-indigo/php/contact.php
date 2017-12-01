<?php
require 'php-mailer/PHPMailerAutoload.php';
// Email address
$mail_to = 'test@gmail.com';
$error_results = array(
    'response' => 'error',
    'message' => 'Error! error sending message.'
);
$success_results = array(
    'response' => 'success',
    'message' => 'Success! message sent.'
);
if ($mail_to && isset($_POST['email'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $website = $_POST['website'];
    $msg = $_POST['message'];
    $subject = "You have received a new message from $name";

    $fields = array(
        0 => array(
            'text' => 'Name',
            'val' => $name
        ),
        1 => array(
            'text' => 'Email address',
            'val' => $email
        ),
        2 => array(
            'text' => 'Phone',
            'val' => $phone
        ),
        3 => array(
            'text' => 'Message',
            'val' => $msg
        )
    );

    $message = "";
    foreach ($fields as $field) {
        $message .= $field['text'] . ": " . htmlspecialchars($field['val'], ENT_QUOTES) . "<br>\n";
    }

    $mail = new PHPMailer;
    $mail->IsSMTP();                                      // Set mailer to use SMTP

    // Optional Settings
    //$mail->Host = 'mail.yourserver.com';				  // Specify main and backup server
    //$mail->SMTPAuth = true;                             // Enable SMTP authentication
    //$mail->Username = 'username';             		  // SMTP username
    //$mail->Password = 'secret';                         // SMTP password
    //$mail->SMTPSecure = 'tls';                          // Enable encryption, 'ssl' also accepted

    $mail->From = $email;
    $mail->FromName = $name;
    $mail->AddAddress($mail_to);                          // Add a recipient
    $mail->AddReplyTo($email, $name);
    $mail->IsHTML(true);                                  // Set email format to HTML
    $mail->CharSet = 'UTF-8';
    $mail->Subject = $subject;
    $mail->Body = $message;

    if (!$mail->Send()) {
        $results = $error_results;
    }

    $results = $success_results;
    echo json_encode($results);
} else {
    $results = $error_results;
    echo json_encode($results);
}
?>