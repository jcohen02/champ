import os

from .settings import *  # noqa: F401, F403

DEBUG = False
ALLOWED_HOSTS = ["openondemand.rcs.ic.ac.uk"]
SECRET_KEY = os.environ["SECRET_KEY"]
EMAIL_HOST = "smarthost.cc.ic.ac.uk"
SERVER_EMAIL = "noreply@imperial.ac.uk"
DEFAULT_FROM_EMAIL = "noreply@imperial.ac.uk"
ADMINS = [("Christopher Cave-Ayland", "c.cave-ayland@imperial.ac.uk")]
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")  # noqa: F405
SECURE_BROWSER_XSS_FILTER = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = 15552000
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
