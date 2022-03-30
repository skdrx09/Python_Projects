import random
from Exceptions import *

class Human:
    '''
        Age. Humans reach adulthood in their late teens and live less than a century.
        Alignment. Humans tend toward no particular alignment. The best and the worst are found among them.
        Size. Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium.
        Speed. Your base walking speed is 30 feet.
        Languages. You can speak, read, and write Common and one extra language of your choice. Humans typically learn the languages of other peoples they deal with, including obscure dialects. They are fond of sprinkling their speech with words borrowed from other tongues: Orc curses, Elvish musical expressions, Dwarvish military phrases, and so on.
    '''
    # These are modifiers to be added when an Entity is assigned this race
    speed = 30
    size = "medium"
    languages = "common"

    def __init__(self, extra_language=(random.choice(["elvish", "dwarven", "orc"])), age=random.randrange(21, 70), alignment='') -> None:
        self.__extra_language = extra_language
        self.__age = age
        self.__alignment = alignment
    
    @property
    def alignment(self):
        return self.__alignment
    
    @alignment.setter
    def alignment(self, alignment : str):
        alignment_list = ["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic Evil"]
        try:
            if any(char.isdigit() for char in alignment):
                raise AlignmentTypeError
        except AlignmentTypeError:
            print("Alignment must not contain numbers.")
            return 'Err'

        for align in alignment_list:
            if alignment == align:
                self.__alignment = alignment
                return "Aligment setted successfully"
            else:
                return "Alignment not found"

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age: int):
        try:
            if new_age < 0 or new_age > 120:
                raise AgeNumberError
        except AgeNumberError:
            print("That age is not possible for a human to reach.")
        else:
            self.__age = new_age
            return "Age setted successfully"

    @property
    def extra_language(self):
        return self.__extra_language
    @extra_language.setter
    def extra_language(self, new_lang : str):
        lang_list = ["elvish", "dwarven", "orc"]
        try:
            for l in lang_list:
                if new_lang == l:
                    self.__extra_language = new_lang
                    self.languages += ' ' + new_lang
                    return "Extra Language setted successfully"
                else:
                    raise LanguageNotFound
        except LanguageNotFound:
            print("The specified language does not exist")
            return 'Err'
    
    def __str__(self) -> str:
        return 'Humans receive 1 extra language of their choice and can be of any alignment. Their age must be lower than 120 and their size is around medium.'


class StandardHuman(Human):
    '''
        Ability Score Increase. Your ability scores each increase by 1.
    '''
    # These are modifiers to be added when an Entity is assigned this subrace
    str = 1
    dex = 1
    con = 1
    int = 1
    wis = 1
    cha = 1

    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return super().__str__() + 'Standard Humans receive a +1 bonus to all of their abilities.'

class VariantHuman(Human):
    '''
        Ability Score Increase. Two different ability scores of your choice increase by 1.
        Skills. You gain proficiency in one skill of your choice.
        Feat. You gain one Feat of your choice.
    '''
    # These are modifiers to be added when an Entity is assigned this subrace
    score_bonus_1 = 1
    score_bonus_2 = 1
    skill_prof = 1
    feat_1 = 1

    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return super().__str__() + '\nVariant Humans Receive +1 in two different scores as a bonus, 1 skill proficiency and 1 feature to choose.'

def main():

    # Class test

    new_pj = VariantHuman()

    print(new_pj.languages)
    new_pj.extra_language = "elvish"
    print(new_pj.languages)

    print(Human())

    print(new_pj)

main()