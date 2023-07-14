const form = document.getElementById('cadastroForm');
const passwordInput = document.getElementById('password');
const submitButton = document.getElementById('submitBtn');

passwordInput.addEventListener('input', () => {
    if (passwordInput.value.length >= 8) {
        passwordInput.classList.remove('error');
        submitButton.disabled = false;
    } else {
        passwordInput.classList.add('error');
        submitButton.disabled = true;
    }
});