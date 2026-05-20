CREATE TABLE ai_predictions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    prediction_type VARCHAR(100) NOT NULL,
    prediction_result TEXT NOT NULL,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);