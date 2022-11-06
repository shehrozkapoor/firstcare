import os

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '-05sgp9!deq=q1nltm@^^2cc+v29i(tyybv3v2t77qi66czazj'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'Patient',
    'accounts',
    'Patient_health_record',
    'Laboratory',
    'Laboratory.administration',
    'Radiology',
    'management',
    'management.ward_management',
    'management.bed_management',
    'management.outpatient_management',
    'management.outpatient_management.clinic_management',
    'management.doctor_management',
    'management.schedule_management',
    'Insurance',
    'Insurance.insurance_administration',
    'Insurance.claims',
    'drchrono_insurance',
    'FHIR',
    'FHIR.api',
    'billing',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'corsheaders',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'firstcare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'firstcare1',
        'USER': 'firstcareuser',
        'PASSWORD': 'firstcare123',
        'HOST': '20.127.29.249',
        'PORT': '5432',
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
#     }
# }

if ENVIRONMENT == 'production':
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AUTH_USER_MODEL = 'accounts.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# SMTP CONFIG
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'haexresports@gmail.com'
EMAIL_HOST_PASSWORD = 'nirjsxrwhnfexaxf'
EMAIL_PORT = 587

# DJANGO REST FRAMEWORK CONFIG


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer',
}



# GRAPPELLI CONFIG
GRAPPELLI_ADMIN_TITLE = "FIRST CARE"

# FHIR CONFIG
# FHIR_ENDPOINT = 'http://hapi.fhir.org/baseR4'
FHIR_ENDPOINT = 'http://fhirtest.b12x.org/r4'
FHIR_ENDPOINT = 'http://localhost:8080/fhir'
FHIR_AUTHORIZATION = "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjQ1Mzk2Mjg4LCJvcmlnSWF0IjoxNjQ1Mzk1OTg4fQ.3KSnml2sEgpfeQmXGmL0shC0fM6IcMXksTkFSF0jmic"

FHIR_URL= {
    'meta':{
        'url':'http://nphies.sa/fhir/ksa/nphies-fs/StructureDefinition/'
    }
}

# server credentials
# 20.127.29.249
# firstcare1
# ASDFasdf123456

APPEND_SLASH=True


FHIR_IDENTIFIER = [{
'use':'old',
'type':{'coding': [{'system': 'https://nadaa.com', 'version': 'v0.1/testing'}]}
}]


# nphies configurations

NPHIES_PROVIDER_LICENSE_VALUE = "N-F-00001"
NPHIES_SYSTEM = "http://nphies.sa/license/provider-license"
NPHIES_VALUE = "N-F-00001"
NPHIES_ENDPOINT = f"{NPHIES_SYSTEM}/{NPHIES_PROVIDER_LICENSE_VALUE}"
NPHIES_FULL_URL = "http://sgh.com.sa/"
NPHIES_ORGANIZATION_ID = "bff3aa1fbd3648619ac082357bf135db"
IDENTIFIER_URL = "localhost:8000/fhir/api/submitBundle/"
TERMINOLOGY = "http://terminology.hl7.org/"


# CELERY CONFIGURATIONS
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_TIMEZONE = 'Asia/Riyadh'