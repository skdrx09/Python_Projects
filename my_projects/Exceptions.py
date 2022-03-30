class AlignmentTypeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class AgeNumberError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class LanguageNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)