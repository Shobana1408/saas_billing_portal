document.addEventListener("DOMContentLoaded", function () {
    console.log("Billing JS loaded");

    calculateInvoiceTotal();

    const amountInput = document.getElementById("amount");
    const taxInput = document.getElementById("tax");

    if (amountInput) {
        amountInput.addEventListener("input", calculateInvoiceTotal);
    }

    if (taxInput) {
        taxInput.addEventListener("input", calculateInvoiceTotal);
    }

    const paymentForm = document.getElementById("paymentForm");

    if (paymentForm) {
        paymentForm.addEventListener("submit", function (event) {
            const amountPaid = document.getElementById("amount_paid").value;

            if (parseFloat(amountPaid) < 0) {
                event.preventDefault();
                alert("Amount paid cannot be negative.");
            }
        });
    }
});

function calculateInvoiceTotal() {
    const amountInput = document.getElementById("amount");
    const taxInput = document.getElementById("tax");
    const totalInput = document.getElementById("total_amount");

    if (!amountInput || !taxInput || !totalInput) {
        return;
    }

    const amount = parseFloat(amountInput.value) || 0;
    const tax = parseFloat(taxInput.value) || 0;
    const total = amount + tax;

    totalInput.value = total.toFixed(2);
}

function confirmPayment() {
    return confirm("Are you sure you want to save this payment?");
}