import pytest

from app import core


def test_there_are_horses_available():
    choice = 2
    horses = core.find_available(choice)

    assert len(horses) >= 1


def test_horse_can_be_booked():
    horses = [h for h in core.all_horses() if not h.is_booked]
    horse = horses[0]

    booked = core.book_horse(horse.horse_name)

    assert booked
    assert booked.is_booked
    assert booked.horse_name == horse.horse_name


def test_cannot_book_a_nonexistent_horse():
    with pytest.raises(core.EntityNotFoundError):
        core.book_horse("GLUE FACTORY")


def test_cannot_book_a_booked_horse():
    table = [h for h in core.all_horses() if not h.is_booked][0]
    core.book_horse(table.horse_name)

    with pytest.raises(core.HorseUnavailableError):
        core.book_horse(table.horse_name)