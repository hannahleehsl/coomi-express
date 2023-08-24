<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $message = $_POST['message'];

    $to = "sales@coomiexpress.com";

    $subject = "New Contact Form Submission";

    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n";
    $email_content .= "Phone Number: $phone\n";
    $email_content .= "Message:\n$message\n";

    if (isset($_FILES['resume'])) {
        $file_name = $_FILES['resume']['name'];
        $file_tmp = $_FILES['resume']['tmp_name'];

        // Add the uploaded file as an attachment
        $attachment = chunk_split(base64_encode(file_get_contents($file_tmp)));
        $email_content .= "--mixedBoundary\n";
        $email_content .= "Content-Type: application/octet-stream; name=\"$file_name\"\n";
        $email_content .= "Content-Disposition: attachment\n";
        $email_content .= "Content-Transfer-Encoding: base64\n\n";
        $email_content .= "$attachment\n";
    }

    $headers = 'From: ' . $email;

    // Send the email
    mail($to, $subject, $email_content, $headers);

    header("Location: contact.html?success=1");
} else {
    header("Location: contact.html?success=0");
}
?>