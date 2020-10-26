import math

def get_entropy(bundle, password):
    return len(password) * math.log2(len(bundle))