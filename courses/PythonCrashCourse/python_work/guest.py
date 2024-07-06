while True:
    guest_name = input("You name:")
    print(f"Hello, {guest_name}")

    with open('guest.txt', 'a') as f:
        f.write(f"{guest_name}\n")

    with open('guest.txt', 'r') as f:
        print("Adding to existing users:")
        print(f.read())
