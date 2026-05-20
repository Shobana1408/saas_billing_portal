CREATE TABLE companies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(150) NOT NULL,
    company_email VARCHAR(120) UNIQUE,
    company_phone VARCHAR(20),
    company_address TEXT,
    industry VARCHAR(100),
    total_employees INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);