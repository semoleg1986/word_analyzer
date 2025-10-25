import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Word Analyzer CLI")
    parser.add_argument("--file", help="Путь к файлу с текстом")
    parser.add_argument("--top", type=int, default=5, help="Количество слов в топе")
    return parser.parse_args()


class App:
    """
    CLI-приложение
    """

    def __init__(self) -> None:
        self.columns = ("Words", "Unique", "Top words")

    def run(self) -> None:
        pass
