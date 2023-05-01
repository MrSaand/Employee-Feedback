// Get references to the login form and login button
const loginForm = document.querySelector('#login-form');
const loginButton = document.querySelector('#login-button');

// Add an event listener to the login button
loginButton.addEventListener('click', (e) => {
    e.preventDefault();
    
    // Get the username and password from the form
    const username = loginForm.querySelector('#username').value;
    const password = loginForm.querySelector('#password').value;
    
    // Make an AJAX request to authenticate the user
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/authenticate');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = () => {
        if (xhr.status === 200) {
            // If the authentication was successful, redirect to the home page
            window.location.href = '/home';
        } else {
            // If the authentication failed, display an error message
            const errorMessage = document.createElement('p');
            errorMessage.innerText = 'Invalid username or password.';
            loginForm.appendChild(errorMessage);
        }
    };
    xhr.send(JSON.stringify({username, password}));
});
