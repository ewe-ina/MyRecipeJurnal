SITEURL = 'https://ewe-ina.github.io/MyRecipeJurnal'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

THEME = 'themes/bootstrap5'
STATIC_PATHS = ['static']

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

I18N_SUBSITES = {
    'pl': {
        'SITENAME': 'Przepysznik',
        'DEFAULT_LANG': 'pl',
        'LOCALE': 'pl_PL.UTF-8',
        'SITEURL': 'https://ewe-ina.github.io/MyRecipeJurnal'
    }
}

DEFAULT_METADATA_ENCODING = 'utf-8'
