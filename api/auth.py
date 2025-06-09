# api/auth.py

from utils.logger import log_event

def user_login(user_id):
    log_event("info", "login_attempt", "User attempting login", component="auth_login", user_id=user_id)

    # Simulated logic
    if user_id == "admin":
        log_event("info", "login_success", "Admin login success", component="auth_login", user_id=user_id)
    else:
        log_event("warning", "login_warning", "Non-admin login", component="auth_login", user_id=user_id)

