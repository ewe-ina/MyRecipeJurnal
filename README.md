# 🧁 My Recipe Journal

A notebook for all my kitchen experiments and delicious mistakes.

## About me

I like experimenting in the kitchen. I like things quick and simple. Recipes are guidelines for me — I mostly cook “by eye,” and the biggest inspiration is whatever happens to be in my fridge. My plate is filled mainly with plant-based dishes (and those are the only ones I’ll be posting here, unless my enthusiasm turns out to be short-lived), because… In short — I eat grass and stones, and draw my energy from the sun. In a slightly less short version: I don’t eat meat (yes, fish and seafood are meat too). Definitely and without exceptions.
I avoid cashews, palm oil, white sugar, glucose-fructose syrup, products with long and complicated ingredient lists, store-bought sweets and crunchy snacks. I avoid them — but sometimes I still eat them and allow myself to indulge my weaknesses for tasty, unhealthy things. The list is probably incomplete, but certainly crazy enough.

## How to use it

Activate virtual environment

```bash
# Linux
source ./.venv/bin/activate

# Windows
source ./.venv/Scripts/activate
```

Compile .mo from .po

```bash
msgfmt messages.po -o messages.mo
```

or

```bash
python -m babel.messages.frontend compile --directory=themes/bootstrap5/translations

```

Generate locally

```bash
python3 generate_thumbnails.py
pelican content
python3 -m http.server -d output
```

## License

Recipes © Ewelina Walkusz licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  

Site code © Ewelina Walkusz, licensed under [MIT License](LICENSE)
