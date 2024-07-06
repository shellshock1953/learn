def get_int(position: str) -> int:
    error = True
    answer = ""
    number = int()
    while error:
        try:
            answer = input(f"Write {position} number:")
            number = int(answer)
            error = False
        except ValueError:
            print(f"{answer} is not a number?")
            error = True
    return number


while True:
    first = get_int("first")
    second = get_int("second")

    try:
        result = int(first) + int(second)
        print(f"{first}+{second}={result}")
    except ValueError:
        print("Seems you add wrong number. Only numbers allowed!")
    print("")
