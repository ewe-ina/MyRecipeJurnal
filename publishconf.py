SITEURL = 'https://myrecipejournal.walkusz.art'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

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
# Thumbnail flags from JSON
# -------------------------------
import json
import os
from pelican import signals

# Path to JSON file created by generate_thumbnails.py
THUMBS_JSON = os.path.join(PATH, 'thumbs.json')
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
import locale

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
