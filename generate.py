from validate import ValidateCPF
import random


class Generate:

    FILENAME: str = "cpfs.txt"

    def __init__(self, amount: int = 100) -> None:
        self.amount = amount

    def generate_cpf(self) -> tuple:
        random_cpf: list[str] = [str(random.randint(0, 9)) for _ in range(9)]
        while len(random_cpf) != 11:
            random_cpf.append(str(
                ValidateCPF(random_cpf).next_digit(
                    len(random_cpf) + 1
                )
            ))
        return tuple(random_cpf)

    def generate(self) -> None:
        data: set[tuple] = set()
        while len(data) != self.amount:
            data.add(self.generate_cpf())
        self.save(data)

    def save(self, data: set[tuple]) -> None:
        with open(self.FILENAME, 'w') as f:
            for cpf in data:
                f.write("".join(map(str, cpf)) + '\n')


if __name__ == '__main__':
    Generate().generate()
