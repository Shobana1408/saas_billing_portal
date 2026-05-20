document.addEventListener("DOMContentLoaded", function () {
    console.log("Chart JS loaded");

    renderRevenueChart();
    renderUserGrowthChart();
});

function renderRevenueChart() {
    const chartCanvas = document.getElementById("revenueChart");

    if (!chartCanvas) {
        return;
    }

    const months = JSON.parse(chartCanvas.dataset.months || "[]");
    const revenues = JSON.parse(chartCanvas.dataset.revenues || "[]");

    new Chart(chartCanvas, {
        type: "line",
        data: {
            labels: months,
            datasets: [
                {
                    label: "Monthly Revenue",
                    data: revenues,
                    borderWidth: 2,
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function renderUserGrowthChart() {
    const chartCanvas = document.getElementById("userGrowthChart");

    if (!chartCanvas) {
        return;
    }

    const months = JSON.parse(chartCanvas.dataset.months || "[]");
    const users = JSON.parse(chartCanvas.dataset.users || "[]");

    new Chart(chartCanvas, {
        type: "bar",
        data: {
            labels: months,
            datasets: [
                {
                    label: "User Growth",
                    data: users,
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}