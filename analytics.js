document.addEventListener("DOMContentLoaded", function () {
    console.log("Analytics JS loaded");

    fetchRevenueForecast();
    fetchChurnPrediction();
    fetchSpendingInsights();
});

function fetchRevenueForecast() {
    const revenueBox = document.getElementById("predictedRevenue");

    if (!revenueBox) {
        return;
    }

    fetch("/analytics/revenue-forecast")
        .then(response => response.json())
        .then(data => {
            revenueBox.innerText = "₹" + data.predicted_revenue;
        })
        .catch(error => {
            console.error("Revenue forecast error:", error);
            revenueBox.innerText = "Unable to load";
        });
}

function fetchChurnPrediction() {
    const churnBox = document.getElementById("churnPrediction");

    if (!churnBox) {
        return;
    }

    fetch("/analytics/churn-prediction")
        .then(response => response.json())
        .then(data => {
            if (data.length === 0) {
                churnBox.innerHTML = "<p>No high-risk companies found.</p>";
                return;
            }

            let html = "";

            data.forEach(company => {
                html += `
                    <div class="ai-insight">
                        ${company.company} has ${company.churn_rate}% churn risk.
                    </div>
                `;
            });

            churnBox.innerHTML = html;
        })
        .catch(error => {
            console.error("Churn prediction error:", error);
            churnBox.innerHTML = "<p>Unable to load churn data.</p>";
        });
}

function fetchSpendingInsights() {
    const insightBox = document.getElementById("spendingInsights");

    if (!insightBox) {
        return;
    }

    fetch("/analytics/spending-insights")
        .then(response => response.json())
        .then(data => {
            if (data.length === 0) {
                insightBox.innerHTML = "<p>No spending insights available.</p>";
                return;
            }

            let html = "";

            data.forEach(insight => {
                html += `<div class="ai-insight">${insight}</div>`;
            });

            insightBox.innerHTML = html;
        })
        .catch(error => {
            console.error("Spending insights error:", error);
            insightBox.innerHTML = "<p>Unable to load insights.</p>";
        });
}