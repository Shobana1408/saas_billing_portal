import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_invoice_pdf(invoice_data, output_folder="static/uploads/invoice_pdfs"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    invoice_number = invoice_data.get("invoice_number", "invoice")
    file_name = f"{invoice_number}.pdf"
    file_path = os.path.join(output_folder, file_name)

    pdf = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, height - 50, "SaaS Billing Portal")

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 90, "Invoice")

    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, height - 130, f"Invoice Number: {invoice_data.get('invoice_number', '')}")
    pdf.drawString(50, height - 155, f"Company: {invoice_data.get('company_name', '')}")
    pdf.drawString(50, height - 180, f"Amount: Rs. {invoice_data.get('amount', '')}")
    pdf.drawString(50, height - 205, f"Tax: Rs. {invoice_data.get('tax', '')}")
    pdf.drawString(50, height - 230, f"Total Amount: Rs. {invoice_data.get('total_amount', '')}")
    pdf.drawString(50, height - 255, f"Due Date: {invoice_data.get('due_date', '')}")
    pdf.drawString(50, height - 280, f"Status: {invoice_data.get('status', '')}")

    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, height - 340, "Thank you for using SaaS Billing Portal.")

    pdf.save()

    return file_path


def delete_pdf(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return True

    return False