document.addEventListener("DOMContentLoaded", function () {
    console.log("Dashboard JS loaded");

    loadDashboardSummary();
});

function loadDashboardSummary() {
    const summaryBox = document.getElementById("dashboardSummary");

    if (!summaryBox) {
        return;
    }

    fetch("/api/dashboard-summary")
        .then(response => response.json())
        .then(data => {
            document.getElementById("totalRevenue").innerText = "₹" + data.total_revenue;
            document.getElementById("totalUsers").innerText = data.total_users;
            document.getElementById("totalCompanies").innerText = data.total_companies;
            document.getElementById("activeSubscriptions").innerText = data.active_subscriptions;
            document.getElementById("failedPayments").innerText = data.failed_payments;
        })
        .catch(error => {
            console.error("Dashboard summary error:", error);
        });
}

function refreshDashboard() {
    loadDashboardSummary();
    alert("Dashboard refreshed successfully.");
}