# このファイルは、local_settings.pyのサンプルファイルです。

# SECURITY WARNING: keep the secret key used in production secret!
# The comments below are samples. In practice, use local_settings.py.
SECRET_KEY = "Secret_key_sample"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# The comments below are samples. In practice, use local_settings.py.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "SampleDB",
        "USER": "User",
        "PASSWORD": "Password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# email settings
EMAIL_HOST = "example.com"
EMAIL_HOST_USER = "sample@example.com"
EMAIL_HOST_PASSWORD = "password"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
