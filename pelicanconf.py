AUTHOR = 'Ewelina Walkusz'
SITENAME = 'My Recipe Jurnal'
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = False

TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

PATH = 'content'
STATIC_PATHS = ['static']

THEME = 'themes/bootstrap5'

# Enable i18n plugin and translations
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Define your languages
I18N_SUBSITES = {
    'pl': {
        'SITENAME': 'Przepysznik',
        'DEFAULT_LANG': 'pl',
        'LOCALE': 'pl_PL.UTF-8',
        'SITEURL': 'http://localhost:8000',
        'ARTICLE_URL': '{slug}-pl.html',
        'ARTICLE_SAVE_AS': '{slug}-pl.html',
    }
}

DEFAULT_METADATA_ENCODING = 'utf-8'
