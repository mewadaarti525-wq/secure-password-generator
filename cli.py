import argparse

from .config import DEFAULT_LENGTH, MIN_LENGTH, MAX_LENGTH
from .generator import generate_multiple
from .strength import check_strength
from .validators import validate_count

def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords or check password strength."
    )
    sub = parser.add_subparsers(dest="command")

    gen = sub.add_parser("generate", help="Generate one or more passwords.")
    gen.add_argument("-l", "--length", type=int, default=DEFAULT_LENGTH,
                     help=f"Length ({MIN_LENGTH}-{MAX_LENGTH}).")
    gen.add_argument("-n", "--count", type=int, default=1,
                     help="Number of passwords (1-50).")
    gen.add_argument("--no-lower", action="store_true")
    gen.add_argument("--no-upper", action="store_true")
    gen.add_argument("--no-numbers", action="store_true")
    gen.add_argument("--no-special", action="store_true")

    check = sub.add_parser("check", help="Check the strength of a password.")
    check.add_argument("password", help="Password to analyze.")

    return parser

def run_cli(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "generate":
        options = {
            "lowercase": not args.no_lower,
            "uppercase": not args.no_upper,
            "numbers": not args.no_numbers,
            "special": not args.no_special,
        }
        try:
            validate_count(args.count)
            passwords = generate_multiple(args.length, options, args.count)
            for i, password in enumerate(passwords, 1):
                print(f"{i}. {password}")
        except ValueError as exc:
            parser.error(str(exc))

    elif args.command == "check":
        result = check_strength(args.password)
        print(f"Strength: {result['label']}")
        print(f"Score: {result['score']}/6")
        print(f"Estimated entropy: {result['entropy']:.1f} bits")
        if result["suggestions"]:
            print("Suggestions:")
            for item in result["suggestions"]:
                print(f"- {item}")
    else:
        parser.print_help()
