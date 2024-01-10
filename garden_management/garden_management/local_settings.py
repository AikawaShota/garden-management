# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')@2@&ic)=kov6sp6!rxc2es4oq1b0365x^f-!r(y2bj##^qlcd'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'garden_management',
        'USER': 'garden_management_admin',
        'PASSWORD': 'GardenManagementAdmin410927{psql}=(Good)',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
