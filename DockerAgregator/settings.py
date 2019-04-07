from django.conf import settings   

settings.configure(
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PGUSER':'postgres',
        'PGPASSWORD':'password',
        'PORT': 5432,
        }
    },
    INSTALLED_APPS = [
        # 'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.sitemaps',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'ormDb',        
    ]
)