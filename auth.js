document.addEventListener("DOMContentLoaded", function () {
    console.log("Auth JS loaded");

    const loginForm = document.querySelector("#loginForm");
    const registerForm = document.querySelector("#registerForm");

    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            const email = document.querySelector("#email").value.trim();
            const password = document.querySelector("#password").value.trim();

            if (email === "" || password === "") {
                event.preventDefault();
                alert("Please enter both email and password.");
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener("submit", function (event) {
            const fullName = document.querySelector("#full_name").value.trim();
            const email = document.querySelector("#email").value.trim();
            const password = document.querySelector("#password").value.trim();

            if (fullName.length < 3) {
                event.preventDefault();
                alert("Full name must be at least 3 characters.");
                return;
            }

            if (!validateEmail(email)) {
                event.preventDefault();
                alert("Please enter a valid email address.");
                return;
            }

            if (password.length < 6) {
                event.preventDefault();
                alert("Password must be at least 6 characters.");
            }
        });
    }
});

function validateEmail(email) {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
}

function togglePassword(inputId) {
    const passwordInput = document.getElementById(inputId);

    if (!passwordInput) {
        return;
    }

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}