CREATE TABLE payments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    invoice_id INT NOT NULL,
    payment_method VARCHAR(50),
    payment_status ENUM('success', 'failed', 'pending') DEFAULT 'pending',
    transaction_id VARCHAR(150),
    amount_paid DECIMAL(10,2),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);