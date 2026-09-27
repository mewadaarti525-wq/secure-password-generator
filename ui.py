from .config import APP_NAME, DEFAULT_LENGTH, CHARACTER_SETS
from .generator import generate_multiple
from .strength import check_strength
from .validators import validate_count

def ask_yes_no(prompt: str, default: bool = True) -> bool:
    suffix = " [Y/n]: " if default else " [y/N]: "
    value = input(prompt + suffix).strip().lower()
    if not value:
        return default
    return value in {"y", "yes"}

def interactive_mode() -> None:
    print("=" * 58)
    print(APP_NAME.center(58))
    print("=" * 58)

    try:
        raw_length = input(f"Password length [{DEFAULT_LENGTH}]: ").strip()
        length = int(raw_length) if raw_length else DEFAULT_LENGTH

        options = {
            "lowercase": ask_yes_no("Include lowercase letters?"),
            "uppercase": ask_yes_no("Include uppercase letters?"),
            "numbers": ask_yes_no("Include numbers?"),
            "special": ask_yes_no("Include special characters?"),
        }

        raw_count = input("How many passwords? [1]: ").strip()
        count = int(raw_count) if raw_count else 1
        validate_count(count)

        passwords = generate_multiple(length, options, count)

        print("\nGenerated Password(s):")
        print("-" * 58)
        for index, password in enumerate(passwords, start=1):
            print(f"{index}. {password}")

        print("\nStrength information:")
        print("-" * 58)
        for index, password in enumerate(passwords, start=1):
            result = check_strength(password)
            print(
                f"{index}. {result['label']} | "
                f"Estimated entropy: {result['entropy']:.1f} bits"
            )

    except (ValueError, EOFError, KeyboardInterrupt) as exc:
        if isinstance(exc, KeyboardInterrupt):
            print("\nOperation cancelled.")
        else:
            print(f"\nInput error: {exc}")

def display_categories() -> None:
    print("Available character categories:")
    for name, chars in CHARACTER_SETS.items():
        print(f"- {name:10}: {len(chars)} characters")
