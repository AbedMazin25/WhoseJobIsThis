import random
import string


def generate_string():
    ans = ''
    ans = ans.join(random.choices(string.ascii_lowercase
                   + string.ascii_uppercase
                   + string.digits, k=20))
    return ans
