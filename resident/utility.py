import random
import string

def generate_code():
  return ''.join(random.choice(string.ascii_uppercase + string.digits, k=6))
