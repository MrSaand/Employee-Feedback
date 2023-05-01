
  function createAccount() {
    // Get the input values
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;

    // Check if passwords match
    if (password !== confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    // Create account logic here
    // ...

    // Redirect to home page after account creation
    window.location.href = "home.html";
  }
