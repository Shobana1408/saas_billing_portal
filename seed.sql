USE saas_billing_portal;

-- =========================================
-- INSERT DEFAULT ROLES
-- =========================================

INSERT INTO roles (role_name, description)
VALUES
('Super Admin', 'Complete system access'),
('Company Admin', 'Manages company users and billing'),
('Finance Manager', 'Handles payments and invoices'),
('User', 'Regular platform user');

-- =========================================
-- INSERT SAMPLE COMPANIES
-- =========================================

INSERT INTO companies (
    company_name,
    company_email,
    company_phone,
    company_address,
    industry,
    total_employees
)
VALUES
(
    'TechNova Solutions',
    'contact@technova.com',
    '9876543210',
    'Chennai, Tamil Nadu',
    'Software',
    120
),
(
    'CloudSync Pvt Ltd',
    'hello@cloudsync.com',
    '9123456780',
    'Bangalore, Karnataka',
    'Cloud Services',
    80
);

-- =========================================
-- INSERT SAMPLE PLANS
-- =========================================

INSERT INTO plans (
    plan_name,
    price,
    billing_cycle,
    max_users,
    features
)
VALUES
(
    'Basic',
    4999,
    'monthly',
    25,
    'Basic dashboard, billing access'
),
(
    'Pro',
    9999,
    'monthly',
    100,
    'Analytics, AI insights, reports'
),
(
    'Enterprise',
    24999,
    'monthly',
    500,
    'Advanced AI analytics and priority support'
);

-- =========================================
-- INSERT SAMPLE USERS
-- =========================================

INSERT INTO users (
    full_name,
    email,
    password,
    role_id,
    company_id,
    status
)
VALUES
(
    'Admin User',
    'admin@saasportal.com',
    'admin123',
    1,
    1,
    'active'
),
(
    'Finance Manager',
    'finance@technova.com',
    'finance123',
    3,
    1,
    'active'
),
(
    'Regular User',
    'user@cloudsync.com',
    'user123',
    4,
    2,
    'active'
);

-- =========================================
-- INSERT SAMPLE SUBSCRIPTIONS
-- =========================================

INSERT INTO subscriptions (
    company_id,
    plan_id,
    start_date,
    end_date,
    status
)
VALUES
(
    1,
    2,
    '2026-01-01',
    '2026-12-31',
    'active'
),
(
    2,
    1,
    '2026-02-01',
    '2026-08-01',
    'active'
);

-- =========================================
-- INSERT SAMPLE INVOICES
-- =========================================

INSERT INTO invoices (
    company_id,
    subscription_id,
    invoice_number,
    amount,
    tax,
    total_amount,
    due_date,
    status
)
VALUES
(
    1,
    1,
    'INV-1001',
    9999,
    1800,
    11799,
    '2026-06-01',
    'paid'
),
(
    2,
    2,
    'INV-1002',
    4999,
    900,
    5899,
    '2026-06-10',
    'unpaid'
);

-- =========================================
-- INSERT SAMPLE PAYMENTS
-- =========================================

INSERT INTO payments (
    invoice_id,
    payment_method,
    payment_status,
    transaction_id,
    amount_paid
)
VALUES
(
    1,
    'UPI',
    'success',
    'TXN123456',
    11799
),
(
    2,
    'Credit Card',
    'pending',
    'TXN654321',
    0
);

-- =========================================
-- INSERT SAMPLE NOTIFICATIONS
-- =========================================

INSERT INTO notifications (
    user_id,
    title,
    message
)
VALUES
(
    1,
    'Welcome',
    'Welcome to the SaaS Billing Portal'
),
(
    2,
    'Payment Reminder',
    'Invoice INV-1002 payment is pending'
);

-- =========================================
-- INSERT SAMPLE AUDIT LOGS
-- =========================================

INSERT INTO audit_logs (
    user_id,
    action,
    ip_address
)
VALUES
(
    1,
    'Logged into dashboard',
    '127.0.0.1'
),
(
    2,
    'Viewed invoice INV-1002',
    '127.0.0.1'
);

-- =========================================
-- INSERT SAMPLE AI PREDICTIONS
-- =========================================

INSERT INTO ai_predictions (
    prediction_type,
    prediction_result
)
VALUES
(
    'Revenue Forecast',
    'Expected revenue growth next month is 15%'
),
(
    'Churn Prediction',
    'CloudSync Pvt Ltd has high churn risk'
);