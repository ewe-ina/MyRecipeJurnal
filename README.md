# 🧁 My Recipe Journal

A notebook for all my kitchen experiments and delicious mistakes.

## How to use it

Activate virtual environment

``bash
# Linux
source ./.venv/bin/activate

# Windows
source ./.venv/Scripts/activate
```

Compile .mo from .po

```bash
msgfmt messages.po -o messages.mo
or
python -m babel.messages.frontend compile --directory=themes/bootstrap5/translations

```

Generate locally

```bash
python3 generate_thumbnails.py
pelican content
python3 -m http.server -d output
```

## License

Recipes © Ewelina Walkusz, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  

Site code © Ewelina Walkusz, licensed under [MIT License](LICENSE)
