"""Scrape a recipe from a website and spit out as schema.org/recipe json.

Usage:
    recipe_importer URL
"""
import sys
import typing as ty

import json
from docopt import docopt

import recipe_scrapers

def get_recipe(url: str) -> recipe_scrapers.AbstractScraper:
    return recipe_scrapers.scrape_me(url)

def print_recipe(recipe: recipe_scrapers.AbstractScraper) -> None:
    print(json.dumps(recipe.schema.data, indent=2))

def main(ops: ty.Dict[str, ty.Any]) -> int:
    print_recipe(get_recipe(ops["URL"]))
    return 0

if __name__ == '__main__':
    sys.exit(main(docopt(__doc__)))


