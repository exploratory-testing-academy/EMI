import uuid
from typing import List, Optional


class Horse:
    def __init__(self, horse_name: str, stable: str, stable_type: int):
        self.stable = stable
        self.horse_name = horse_name
        self.type = stable_type
        self.is_booked = False


class EntityNotFoundError(Exception):
    pass


class HorseUnavailableError(Exception):
    pass


def find_available(choice: int) -> List[Horse]:
    global horses

    return [
        h
        for h in horses
        if h.type == choice and not h.is_booked
    ]


def book_horse(horse_id: str):
    horse = find_horse_by_name(horse_id)

    if not horse:
        raise EntityNotFoundError()

    if horse.is_booked:
        raise HorseUnavailableError()

    horse.is_booked = True
    return horse


def all_horses():
    return horses[:]


def find_horse_by_name(horse_name: str) -> Optional[Horse]:
    return horse_lookup.get(horse_name)


horses = [
    Horse("Pipsa", "Koivuniemi", 2),
    Horse("Diego", "Koivuniemi", 2),
    Horse("Rolex", "Tuomarinkylä", 1),
    Horse("Diva", "Tuomarinkylä", 1),
    Horse("Kassu", "Mustila", 2),
]

horse_lookup = {
    h.horse_name: h
    for h in horses
}