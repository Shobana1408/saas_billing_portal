document.addEventListener("DOMContentLoaded", function () {
    console.log("Main JS loaded");

    autoHideAlerts();
    setActiveSidebarLink();
});

function autoHideAlerts() {
    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alertBox) {
        setTimeout(function () {
            alertBox.style.display = "none";
        }, 4000);
    });
}

function setActiveSidebarLink() {
    const currentPath = window.location.pathname;
    const sidebarLinks = document.querySelectorAll(".sidebar a");

    sidebarLinks.forEach(function (link) {
        if (link.getAttribute("href") === currentPath) {
            link.style.background = "#1f2937";
            link.style.color = "#ffffff";
        }
    });
}

function confirmAction(message) {
    return confirm(message || "Are you sure you want to continue?");
}

function toggleSidebar() {
    const sidebar = document.querySelector(".sidebar");

    if (!sidebar) {
        return;
    }

    sidebar.classList.toggle("show-sidebar");
}