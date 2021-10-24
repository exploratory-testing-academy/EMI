import core


def main():
    while True:
        if not book_riding_hour():
            break

        print()


def book_riding_hour():
    print("*********************************************")
    print("* EMI stables: Find a horse for playriding! *")
    print("*********************************************")
    print()

    print("Which stables to try booking in first")
    print("1. Local in Helsinki")
    print("2. Summer/weekend places")
    choice = input("Choose a number: ")
    if not choice or not choice.strip():
        print("Ok, bye!")
        return False

    choice = int(choice)

    options = core.find_available(choice)

    print()
    if not options:
        print("Whoops, no horses for that stable. Try another.")
        return True

    print("Here are the available horses:")
    for idx, o in enumerate(options):
        print("{}. Stable: {}, horse: {}.".format(idx + 1, o.stable, o.horse_name))

    print()
    choice = input("Enter a number of the horse to book: ")
    if not choice or not choice.strip():
        print("Ok, bye!")
        return False

    num = int(choice) - 1

    to_book = options[num]
    booked = core.book_horse(to_book.horse_name)
    print("Booked you a horse at {} named {}".format(booked.stable, booked.horse_name))
    return True


if __name__ == '__main__':
    main()