# -------- Colors terminal ------------
GREEN = '\033[32m'
RESET = '\033[0m'
RED = '\033[31m'
BLUE = '\033[34m'
CYAN = '\033[36m'
YELLOW = '\033[33m'


SPACE = 40
CARACTER = '-'

def message_empty_calendar():
    print('')
    print('AGENDA'.center(SPACE, '-'))
    print('vacía'.center(SPACE, ' '))
    print('')
