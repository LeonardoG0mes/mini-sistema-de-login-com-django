const form = document.getElementById('loginForm');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const submitButton = document.getElementById('submitBtn');

form.addEventListener('input', () => {
    const usernameValue = usernameInput.value.trim();
    const passwordValue = passwordInput.value.trim();

    if (usernameValue !== '' && passwordValue !== '' && passwordValue.length >= 8) {
        submitButton.disabled = false;
    } else {
        submitButton.disabled = true;
    }
});