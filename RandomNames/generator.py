
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import data
import random


def _load_txt_to_list(filename):
    d = pkg_resources.read_text(data, filename).strip().split('\n')
    return d


def random_name(seed=None):

    if seed is not None:
        random.seed(seed, version=2)

    adjectives = _load_txt_to_list('adj_character.txt')
    nouns = _load_txt_to_list('noun_food.txt')

    name_template = "{}_{}"

    a = random.choice(adjectives)
    n = random.choice(nouns)
    name = name_template.format(a, n)
    if seed is not None:
        random.seed()

    return name