from .base import *

ALLOWED_HOSTS = [
    "habitstacker.coderustle.com",
    "habitstacker.azurewebsites.net",
]

# SECURITY
# -----------------------------------------------------------------------------
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_TRUSTED_ORIGINS = ["https://habitstacker.azurewebsites.ro"]
