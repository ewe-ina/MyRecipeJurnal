AUTHOR = 'Ewelina Walkusz'
SITENAME = 'My Recipe Journal'
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = False

TIMEZONE = 'Europe/Warsaw'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

PATH = 'content'
STATIC_PATHS = ['static']

THEME = 'themes/bootstrap5'

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

DEFAULT_METADATA_ENCODING = 'utf-8'

# -------------------------------
import json
import locale
import os
from pelican import signals

# -------------------------------
# Thumbnail flags from JSON
# -------------------------------
THUMBS_JSON = os.path.join(PATH, 'thumbs.json') # Path to JSON file created by generate_thumbnails.py
if os.path.exists(THUMBS_JSON):
    with open(THUMBS_JSON, 'r', encoding='utf-8') as f:
        thumbs_data = json.load(f)
else:
    thumbs_data = {}

def add_thumb_flag(generator):
    """
    Add a 'has_thumb' attribute to each article.
    This flag is True if a thumbnail exists for the article's slug.
    """
    for article in generator.articles:
        article.has_thumb = thumbs_data.get(article.slug, False)

signals.article_generator_finalized.connect(add_thumb_flag)

# -------------------------------
# Date formatting filter depending on article language
# -------------------------------
def datetimeformat(article, format_pl='%d %B %Y', format_en='%B %d, %Y'):
    """
    Format article.date according to its language.
    - 'pl' -> Polish format
    - otherwise -> English format
    """
    try:
        if getattr(article, 'lang', 'en') == 'pl':
            locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')
            return article.date.strftime(format_pl)
        else:
            locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
            return article.date.strftime(format_en)
    except locale.Error:
        return article.date.strftime('%Y-%m-%d')

# Register the filter for Jinja2
JINJA_FILTERS = {
    'datetimeformat': datetimeformat,
}

# -------------------------------
# Global SITE_LANG for Jinja templates
# -------------------------------
def set_site_lang(generator, metadata):
    """
    Set SITE_LANG variable in Jinja context for the current page.
    Uses the generator's DEFAULT_LANG or the article's lang.
    """
    # For articles, use article.lang
    lang = getattr(generator, 'lang', generator.settings.get('DEFAULT_LANG', 'en'))
    generator.context['SITE_LANG'] = lang

# Connect to article generator and page generator
signals.article_generator_preread.connect(set_site_lang)
signals.page_generator_preread.connect(set_site_lang)
