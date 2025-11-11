SITEURL = 'https://ewe-ina.github.io/MyRecipeJurnal'
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