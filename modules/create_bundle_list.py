import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL = string.punctuation

def create_bundle_list(*args):
    bundle = ''
    for c in args:
        bundle += c
    return list(bundle)