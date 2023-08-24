document.getElementById("submitBtn").addEventListener("click", function () {
    // Get form values
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var message = document.getElementById("message").value;
  
    // Validate form fields (optional)
    if (!name || !email || !phone || !message) {
      alert("Please fill out all fields.");
      return;
    }
  
    // Create a new FormData object
    var formData = new FormData();
    formData.append("name", name);
    formData.append("email", email);
    formData.append("phone", phone);
    formData.append("message", message);
  
    // Send the form data using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "send_email.php", true);
    xhr.onload = function () {
      if (xhr.status === 200) {
        alert("Message sent successfully!");
        // Reset the form fields if needed
        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("phone").value = "";
        document.getElementById("message").value = "";
      } else {
        alert("Error sending message. Please try again later.");
      }
    };
    xhr.send(formData);
  });