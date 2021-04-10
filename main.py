from string import ascii_uppercase, digits
from random import choices
def generateCode(lenght: int):
    return "".join(choices(ascii_uppercase + digits, k=lenght))