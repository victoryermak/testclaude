def get_digit(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and len(value) == 1:
            return int(value)
        print("Please enter a single digit (0-9).")


def main():
    a = get_digit("Enter first digit: ")
    b = get_digit("Enter second digit: ")
    c = get_digit("Enter third digit: ")
    d = get_digit("Enter fourth digit: ")
    print(f"Result: {a} * {b} * {c} * {d} = {a * b * c * d}")


if __name__ == "__main__":
    main()
