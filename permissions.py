ROLE_SUPER_ADMIN = 1
ROLE_COMPANY_ADMIN = 2
ROLE_FINANCE_MANAGER = 3
ROLE_USER = 4


PERMISSIONS = {
    ROLE_SUPER_ADMIN: [
        "manage_users",
        "manage_roles",
        "manage_companies",
        "manage_plans",
        "manage_subscriptions",
        "manage_invoices",
        "manage_payments",
        "view_analytics",
        "view_audit_logs",
        "manage_settings"
    ],
    ROLE_COMPANY_ADMIN: [
        "manage_users",
        "manage_subscriptions",
        "view_invoices",
        "view_payments",
        "view_analytics"
    ],
    ROLE_FINANCE_MANAGER: [
        "manage_invoices",
        "manage_payments",
        "view_analytics",
        "view_reports"
    ],
    ROLE_USER: [
        "view_dashboard",
        "view_notifications",
        "view_profile"
    ]
}


def has_permission(role_id, permission):
    role_id = int(role_id)

    if role_id not in PERMISSIONS:
        return False

    return permission in PERMISSIONS[role_id]


def is_super_admin(role_id):
    return int(role_id) == ROLE_SUPER_ADMIN


def is_company_admin(role_id):
    return int(role_id) == ROLE_COMPANY_ADMIN


def is_finance_manager(role_id):
    return int(role_id) == ROLE_FINANCE_MANAGER


def is_regular_user(role_id):
    return int(role_id) == ROLE_USER