import random

def password_generator(bundle, length=12):
    random.shuffle(bundle)
    password = random.choices(bundle, k=length)
    password = ''.join(password)
    return password