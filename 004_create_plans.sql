CREATE TABLE plans (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plan_name VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    billing_cycle ENUM('monthly', 'yearly') DEFAULT 'monthly',
    max_users INT DEFAULT 10,
    features TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);