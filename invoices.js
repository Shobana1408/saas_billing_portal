document.addEventListener("DOMContentLoaded", function () {
    console.log("Invoices JS loaded");

    const invoiceForm = document.getElementById("invoiceForm");

    if (invoiceForm) {
        invoiceForm.addEventListener("submit", function (event) {
            const amount = parseFloat(document.getElementById("amount").value) || 0;
            const tax = parseFloat(document.getElementById("tax").value) || 0;
            const total = parseFloat(document.getElementById("total_amount").value) || 0;

            if (amount < 0 || tax < 0 || total < 0) {
                event.preventDefault();
                alert("Invoice amount, tax, and total cannot be negative.");
            }
        });
    }

    calculateTotal();
});

function calculateTotal() {
    const amountInput = document.getElementById("amount");
    const taxInput = document.getElementById("tax");
    const totalInput = document.getElementById("total_amount");

    if (!amountInput || !taxInput || !totalInput) {
        return;
    }

    amountInput.addEventListener("input", updateTotal);
    taxInput.addEventListener("input", updateTotal);

    updateTotal();
}

function updateTotal() {
    const amount = parseFloat(document.getElementById("amount").value) || 0;
    const tax = parseFloat(document.getElementById("tax").value) || 0;
    const total = amount + tax;

    document.getElementById("total_amount").value = total.toFixed(2);
}

function printInvoice() {
    window.print();
}

function confirmInvoiceDelete() {
    return confirm("Are you sure you want to delete this invoice?");
}