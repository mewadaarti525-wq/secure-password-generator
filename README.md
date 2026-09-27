# Secure Random Password Generator

A command-line Python application for generating secure random passwords and evaluating password strength.

## Features

- Secure password generation using Python's `secrets` module.
- Custom password length from 8 to 128 characters.
- Optional lowercase, uppercase, numeric, and special-character sets.
- Generate multiple passwords in one run.
- Password strength classification.
- Estimated entropy calculation.
- Input validation and clear error messages.
- Interactive mode and command-line arguments.
- Unit tests using Python's built-in `unittest` framework.
- No external runtime dependencies.

## Project Structure

```text
SecurePasswordGenerator/
├── main.py
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── generator.py
│   ├── strength.py
│   ├── ui.py
│   └── validators.py
├── tests/
│   └── test_password_generator.py
├── docs/
│   ├── architecture.md
│   └── workflow.md
├── statement.md
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- Terminal / command prompt
- No third-party packages are required.

## Installation

1. Clone the repository.
2. Open a terminal in the project folder.
3. Optional: create a virtual environment.

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

4. No package installation is required because the project uses Python's standard library.

## Run

Interactive mode:

```bash
python main.py
```

Generate a 20-character password:

```bash
python main.py generate --length 20
```

Generate five passwords:

```bash
python main.py generate --length 20 --count 5
```

Generate without special characters:

```bash
python main.py generate --length 16 --no-special
```

Check password strength:

```bash
python main.py check "ExamplePassword123!"
```

## Testing

Run all tests from the project root:

```bash
python -m unittest discover -s tests -v
```

## Security Notes

Passwords are generated with `secrets`, which is designed for security-sensitive random values. The application does not save generated passwords to disk and does not send them to a network service.

The entropy value is an estimate based on the character categories detected in the password. It should not be treated as a complete password-audit system.

## Academic Scope

This project demonstrates Python modules, functions, command-line interfaces, exception handling, validation, data structures, secure random generation, and unit testing.
