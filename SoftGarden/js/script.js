const registerLink = document.querySelector('.register-link');
const registerForm = document.querySelector('.register-form');

registerLink.addEventListener('click', () => {
    registerForm.classList.toggle('hidden');
});
