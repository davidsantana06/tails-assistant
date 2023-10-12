from colorama import Fore, Style


def print_color(msg: str, sender: str, color: str):
    print(
        f'> {sender}:\n' + f'{color}{msg}{Style.RESET_ALL}'
    )


def print_light(msg: str, sender: str):
    print_color(msg, sender, Fore.WHITE)


def print_success(msg: str, sender: str):
    print_color(msg, sender, Fore.GREEN)


def print_error(msg: str, sender: str):
    print_color(msg, sender, Fore.RED)


def print_warning(msg: str, sender: str):
    print_color(msg, sender, Fore.YELLOW)


def print_info(msg: str, sender: str):
    print_color(msg, sender, Fore.BLUE)
