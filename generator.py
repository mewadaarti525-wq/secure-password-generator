import secrets
import string

from .config import CHARACTER_SETS
from .validators import validate_length, validate_options

def _secure_shuffle(items):
    # secrets.SystemRandom uses the operating system's secure random source.
    rng = secrets.SystemRandom()
    rng.shuffle(items)

def generate_password(length: int, options: dict) -> str:
    validate_length(length)
    validate_options(options)

    selected_sets = [
        CHARACTER_SETS[name]
        for name, enabled in options.items()
        if enabled
    ]

    if length < len(selected_sets):
        raise ValueError(
            "Password length must be at least the number of selected categories."
        )

    password = [secrets.choice(chars) for chars in selected_sets]
    pool = "".join(selected_sets)

    while len(password) < length:
        password.append(secrets.choice(pool))

    _secure_shuffle(password)
    return "".join(password)

def generate_multiple(length: int, options: dict, count: int) -> list[str]:
    return [generate_password(length, options) for _ in range(count)]
