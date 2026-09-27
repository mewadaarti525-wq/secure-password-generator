from .config import MIN_LENGTH, MAX_LENGTH

def validate_length(length: int) -> int:
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(
            f"Password length must be between {MIN_LENGTH} and {MAX_LENGTH}."
        )
    return length

def validate_count(count: int) -> int:
    if count < 1 or count > 50:
        raise ValueError("Number of passwords must be between 1 and 50.")
    return count

def validate_options(options: dict) -> None:
    if not any(options.values()):
        raise ValueError("Select at least one character category.")
