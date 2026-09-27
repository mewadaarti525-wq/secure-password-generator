import sys
from src.cli import run_cli
from src.ui import interactive_mode

def main():
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        run_cli()

if __name__ == "__main__":
    main()
