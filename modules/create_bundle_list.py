import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL = string.punctuation

def create_bundle_list(*args):
    bundle = [c for c in args]
    return bundle