"""Scrape a recipe from a website and spit out as schema.org/recipe json.

Usage:
    recipe_importer [-w] URL

Options:
    -w, --web-page    Print as a webpage. Useful for importing to Nextcloud recipes...run this script, output to index.html, then run python3 -m http.server and import to Nextcloud using the printed URL.
"""

import sys
import typing as ty

import json
from docopt import docopt

import recipe_scrapers


def get_recipe(url: str) -> recipe_scrapers.AbstractScraper:
    return recipe_scrapers.scrape_me(url)


def print_recipe(recipe: recipe_scrapers.AbstractScraper, as_webpage=False) -> None:
    header = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
<?xml encoding="UTF-8">
<html>
    <body>
        <script type="application/ld+json">
"""
    schema = json.dumps(recipe.schema.data, indent=2)
    footer = """
        </script>
    </body>
</html>"""
    if as_webpage:
        text = header + schema + footer
    else:
        text = schema
    print(text)


def main(ops: ty.Dict[str, ty.Any]) -> int:
    print_recipe(get_recipe(ops["URL"]), as_webpage=ops.get("-w"))
    return 0


if __name__ == "__main__":
    sys.exit(main(docopt(__doc__)))
