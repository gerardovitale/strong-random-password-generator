import math

def calculate_password_entropy(bundle, password):
    return len(password) * math.log2(len(bundle))