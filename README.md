# AI-Powered Role-Based SaaS Billing & Analytics Portal

## Project Overview

The AI-Powered Role-Based SaaS Billing & Analytics Portal is a full-stack web application built using Python Flask, MySQL, HTML, CSS, and JavaScript.

This project is designed for SaaS businesses to manage users, companies, subscription plans, invoices, payments, notifications, finance reports, and AI-powered analytics from a single secure dashboard.

The system supports role-based access control so that each user sees and accesses only the features allowed for their role.

---

## Project Title

AI-Powered Role-Based SaaS Billing & Analytics Portal

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python Flask |
| Database | MySQL |
| Frontend | HTML, CSS, JavaScript |
| Authentication | Flask-Login |
| Forms | Flask-WTF |
| Email Support | Flask-Mail |
| AI / Analytics | Python, Pandas, NumPy, Scikit-learn |
| PDF Support | ReportLab |
| Styling | Custom CSS |
| Charts / Insights | Dataset-based analytics |

---

## Main Features

### Authentication
- User login
- User registration
- Logout
- Password hashing
- Session management

### Role-Based Access Control
The system supports four user roles:

| Role | Description |
|---|---|
| Super Admin | Complete system access |
| Company Admin | Manages company users, subscriptions, invoices, and analytics |
| Finance Manager | Handles invoices, payments, finance reports, and analytics |
| User | Basic access to profile and notifications |

---

## Role Access Summary

| Module | Super Admin | Company Admin | Finance Manager | User |
|---|---|---|---|---|
| Dashboard | Yes | Yes | Yes | Yes |
| Users | Yes | Yes | No | No |
| Companies | Yes | No | No | No |
| Plans | Yes | Yes | No | No |
| Subscriptions | Yes | Yes | No | No |
| Invoices | Yes | Yes | Yes | No |
| Payments | Yes | Yes | Yes | No |
| Analytics | Yes | Yes | Yes | No |
| Notifications | Yes | Yes | Yes | Yes |
| Finance | Yes | No | Yes | No |
| Admin Settings | Yes | No | No | No |

---

## Modules

### 1. Dashboard Module
Each role has a different dashboard view.

- Super Admin Dashboard
- Company Admin Dashboard
- Finance Manager Dashboard
- User Dashboard

### 2. User Management
- Create users
- View users
- Update user status
- Block users
- Activate users
- Assign roles
- View user details

### 3. Company Management
- Create company
- View companies
- Edit company details
- Delete company
- View company billing summary

### 4. Plans and Subscriptions
- Create subscription plans
- View available plans
- Create subscriptions
- Upgrade subscription plans
- Cancel subscriptions
- Activate cancelled subscriptions
- View subscription details

### 5. Invoice Management
- Create invoices
- View invoice list
- View invoice details
- Preview invoice
- Print invoice view
- Update invoice status
- Delete invoice

### 6. Payment Management
- Record payments
- View payment history
- Track successful payments
- Track pending payments
- Track failed payments
- Auto-update invoice status based on payment status

### 7. Analytics and AI Insights
- Revenue forecast
- Revenue report
- User growth report
- Churn prediction
- Spending insights
- AI billing recommendations

### 8. Notification System
- View notifications
- Mark notifications as read
- Mark all notifications as read
- Delete notifications
- Auto-generate notifications for invoices and payments

### 9. Finance Module
- Finance dashboard
- Transaction list
- Revenue tracking
- Tax reports
- Expense tracking

---

## AI Features

This project includes simple AI-powered analytics using Python and Scikit-learn.

### AI Revenue Forecast
The system predicts next month’s revenue using Linear Regression based on previous monthly revenue data.

### Churn Prediction
The system analyzes churn rate and classifies companies into:

- High Risk
- Medium Risk
- Low Risk

### Spending Insights
The system reviews billing data and generates insights such as:

- Companies spending above average
- Companies with high failed payment counts
- Enterprise account recommendations

---

## Folder Structure

```plaintext
saas_billing_portal/
│
├── app.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── ai_models/
│   ├── __init__.py
│   ├── revenue_forecast.py
│   ├── churn_prediction.py
│   ├── spending_insights.py
│   ├── model_prediction.py
│   ├── model_train.py
│   └── dataset/
│       ├── revenue_data.csv
│       ├── churn_data.csv
│       └── billing_data.csv
│
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   ├── mysql_connector.py
│   └── migrations/
│
├── docs/
│   ├── api_documentation.md
│   ├── database_design.md
│   ├── project_overview.md
│   └── role_matrix.md
│
├── forms/
│
├── models/
│
├── routes/
│
├── services/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── uploads/
│
├── templates/
│   ├── admin/
│   ├── analytics/
│   ├── auth/
│   ├── billing/
│   ├── companies/
│   ├── dashboard/
│   ├── emails/
│   ├── finance/
│   ├── invoices/
│   ├── notifications/
│   ├── subscriptions/
│   └── users/
│
├── tests/
│
└── utils/