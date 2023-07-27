from colorama import (  # type: ignore
    Fore,
    init
)
import argparse


init(autoreset=True)


class ValidateCPF:

    def __init__(self, cpf: list[str]) -> None:
        self.cpf = cpf

    def validate_digit(self, digit, position):
        if int(self.cpf[position]) == digit:
            if position + 1 != len(self.cpf):
                self.validation(position + 1)
            else:
                print(f"{Fore.GREEN}[+] True")
        else:
            print(f"{Fore.RED}[-] False")

    def reverse_list(self, position) -> list[int]:
        return list(range(len(self.cpf[:position]) + 1, 1, -1))

    def next_digit(self, position) -> int:
        reverse_list: list[int] = self.reverse_list(position)
        calc = [
            int(self.cpf[number]) * int(reverse_list[number])
            for number in range(0, len(reverse_list), +1)
        ]
        digit = (sum(calc)) % 11

        if digit >= 2:
            digit = 11 - digit

        return digit

    def validation(self, position) -> None:
        next_digit: int = self.next_digit(position)
        self.validate_digit(next_digit, position)


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--filename",
        dest="filename",
        type=str,
        help="Filename with cpfs to verify."
    )
    parser.add_argument(
        "-c",
        "--cpf",
        dest="cpf",
        type=str,
        help="CPF to verify."
    )
    return parser.parse_args()


def verify_input(code: list[str]) -> None:
    if len(code) == 11:
        ValidateCPF(code).validation(9)
    else:
        for element in code:
            if not element.isnumeric():
                code.remove(element)
        if len(code) != 11:
            print(f"{Fore.YELLOW}[-] CPF NEEDS EXACTLY 11 NUMBERS...")
        else:
            verify_input(code)


def main() -> None:
    arguments: argparse.Namespace = get_arguments()

    if arguments.filename:
        with open(str(arguments.filename), "r") as f:
            for cpf in f:
                verify_input(list(cpf.rstrip()))
    elif arguments.cpf:
        verify_input(list(arguments.cpf))
    else:
        print("You must specify an filename with cpfs or a unique cpf...")
        print("Use: py .\\validate.py -h to get help...")


if __name__ == "__main__":
    main()
