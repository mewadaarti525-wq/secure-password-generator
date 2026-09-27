import math
from .config import LOWERCASE, UPPERCASE, DIGITS, SPECIALS

def calculate_entropy(password: str) -> float:
    pool_size = 0
    if any(c in LOWERCASE for c in password):
        pool_size += len(LOWERCASE)
    if any(c in UPPERCASE for c in password):
        pool_size += len(UPPERCASE)
    if any(c in DIGITS for c in password):
        pool_size += len(DIGITS)
    if any(c in SPECIALS for c in password):
        pool_size += len(SPECIALS)

    if pool_size == 0:
        return 0.0
    return len(password) * math.log2(pool_size)

def check_strength(password: str) -> dict:
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")
    if any(not c.isalnum() for c in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    if score <= 2:
        label = "WEAK"
    elif score <= 4:
        label = "MEDIUM"
    else:
        label = "STRONG"

    return {
        "label": label,
        "score": score,
        "entropy": calculate_entropy(password),
        "suggestions": suggestions,
    }
