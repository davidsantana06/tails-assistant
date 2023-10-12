from colorama import Fore, Style
from time import sleep


CHAR_GAP_SECS = 0.04


def print_color(msg: str, sender: str, color: str):
    print(
        '\n> ' + sender + ':\n' +
        f'{color}{msg}{Style.RESET_ALL}'
    )


def print_light(msg: str, sender: str, char_by_char: bool = True):
    print('\n> ' + sender + ':')

    if char_by_char:
        for char in msg:
            print(char, end='', flush=True)

            if char != ' ':
                sleep(CHAR_GAP_SECS)

        print()
    else:
        print(msg)


def print_success(msg: str, sender: str):
    print_color(msg, sender, Fore.GREEN)


def print_error(msg: str, sender: str):
    print_color(msg, sender, Fore.RED)


def print_warning(msg: str, sender: str):
    print_color(msg, sender, Fore.YELLOW)
