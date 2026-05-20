document.addEventListener("DOMContentLoaded", function () {
    console.log("Admin JS loaded");

    const deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(function (button) {
        button.addEventListener("click", function (event) {
            const confirmDelete = confirm("Are you sure you want to delete this item?");

            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });

    const roleForm = document.querySelector("#roleForm");

    if (roleForm) {
        roleForm.addEventListener("submit", function (event) {
            const roleName = document.querySelector("#role_name").value.trim();

            if (roleName.length < 2) {
                event.preventDefault();
                alert("Role name must be at least 2 characters long.");
            }
        });
    }
});