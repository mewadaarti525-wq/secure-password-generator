APP_NAME = "Secure Random Password Generator"
DEFAULT_LENGTH = 16
MIN_LENGTH = 8
MAX_LENGTH = 128

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIALS = "!@#$%^&*()-_=+[]{};:,.?/"

CHARACTER_SETS = {
    "lowercase": LOWERCASE,
    "uppercase": UPPERCASE,
    "numbers": DIGITS,
    "special": SPECIALS,
}
