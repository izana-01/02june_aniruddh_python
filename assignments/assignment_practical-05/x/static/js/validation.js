document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("regForm");
    const name = document.getElementById("id_full_name");
    const email = document.getElementById("id_email");
    const phone = document.getElementById("id_phone");

    const nameError = document.getElementById("nameError");
    const emailError = document.getElementById("emailError");
    const phoneError = document.getElementById("phoneError");

    function validateEmail(emailValue) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailValue);
    }

    function validatePhone(phoneValue) {
        return /^\+?\d{7,15}$/.test(phoneValue);
    }

    form.addEventListener("submit", function (e) {
        let valid = true;

        nameError.textContent = "";
        emailError.textContent = "";
        phoneError.textContent = "";

        if (name.value.trim() === "") {
            nameError.textContent = "Full name is required";
            valid = false;
        }

        if (!validateEmail(email.value)) {
            emailError.textContent = "Invalid email format";
            valid = false;
        }

        if (!validatePhone(phone.value)) {
            phoneError.textContent = "Phone must be 7–15 digits";
            valid = false;
        }

        if (!valid) {
            e.preventDefault();
        }
    });
});
