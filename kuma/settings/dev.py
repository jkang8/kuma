from kuma.settings.common import *  # noqa

import logging

INTERNAL_IPS = ('127.0.0.1', '192.168.10.1')

DEBUG = True
DEV = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

SESSION_COOKIE_SECURE = True

DEMO_UPLOADS_ROOT = path('uploads', 'demos')
DEMO_UPLOADS_URL = '/media/uploads/demos/'

PROD_DETAILS_DIR = path('..', '..', 'product_details_json')
MDC_PAGES_DIR = path('mdc_pages')

GOOGLE_MAPS_API_KEY = "ABQIAAAANRj9BHQi5ireVluCwVy0yRSrufPN8BjQWjkoRva24PCQEXS2OhSXu2BEgUH5PmGOmW71r2-tEuOVuQ"

RECAPTCHA_USE_SSL = True
RECAPTCHA_PUBLIC_KEY = '6LdX8cISAAAAAA9HRXmzrcRSFsUoIK9u0nWpvGS_'
RECAPTCHA_PRIVATE_KEY = '6LdX8cISAAAAACkC1kqYmpeSf-1geTmLzrLnq0t6'

BITLY_USERNAME = 'lmorchard'
BITLY_API_KEY = "R_2653e6351e31d02988b3da31dac6e2c0"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Uncomment to enable a real celery queue
CELERY_ALWAYS_EAGER = True

INSTALLED_APPS = INSTALLED_APPS + (
    "django_extensions",
    # "debug_toolbar",
    "devserver",
)

JINGO_EXCLUDE_APPS = JINGO_EXCLUDE_APPS + (
    'debug_toolbar',
)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
)

DEVSERVER_MODULES = (
    # sql modules interfere with saving some KumaScript templates
    # 'devserver.modules.sql.SQLRealTimeModule',
    # 'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    #'devserver.modules.ajax.AjaxDumpModule',
    #'devserver.modules.profile.MemoryUseModule',
    #'devserver.modules.cache.CacheSummaryModule',
    #'devserver.modules.profile.LineProfilerModule',
)

# The default database should point to the master.
DATABASES = {
    'default': {
        'NAME': 'kuma',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'kuma',
        'PASSWORD': 'kuma',
        'OPTIONS': {'init_command': 'SET storage_engine=InnoDB'},
    },
}

# This is used to hash some things in Django.
SECRET_KEY = 'jenny8675309'

DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

LOG_LEVEL = logging.ERROR

SITE_URL = 'https://developer-local.allizom.org'
PROTOCOL = 'https://'
DOMAIN = 'developer-local.allizom.org'

KUMASCRIPT_URL_TEMPLATE = 'http://localhost:9080/docs/{path}'

ATTACHMENT_HOST = 'mdn-local.mozillademos.org'

# Elasticsearch related settings.
ES_URLS = ['127.0.0.1:9200']
ES_DEFAULT_NUM_REPLICAS = 0
ES_DEFAULT_NUM_SHARDS = 1
ES_DEFAULT_REFRESH_INTERVAL = '5s'
ES_DISABLED = True
ES_INDEXES = {'default': 'main_index'}
ES_INDEX_PREFIX = 'mdn'
# Specify the extra timeout in seconds for the indexing ES connection.
ES_INDEXING_TIMEOUT = 30

SOCIALACCOUNT_PROVIDERS['persona']['AUDIENCE'] = 'https://developer-local.allizom.org'
