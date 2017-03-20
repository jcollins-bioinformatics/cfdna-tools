import string
import random

def id_generator(size=12, chars=string.ascii_uppercase+string.punctuation):
    rand_s = ''.join([random.choice(chars) for _ in size])
    return rand_s

print(id_generator())
