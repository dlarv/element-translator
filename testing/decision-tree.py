import random

VALID_DOUBLES = []
VALID_SINGLES = []
MAX_DEPTH = 7

with open('singles.csv') as stream:
    VALID_SINGLES = [x.strip('_\n') for x in stream.read().split(',')]

with open('doubles.csv') as stream:
    VALID_DOUBLES = [x.strip() for x in stream.read().split(',')]


def single(data: list, code: str) -> dict:
    print('*' * 10 + "Calculate: " + code)
    if len(code) == MAX_DEPTH:
        return {code: data}

    yes = []
    no = []

    for word in data:
        print(f"Calculating for {word}")
        print(f"Is {word[-1]} a valid single?")
        if word[-1] in VALID_SINGLES:
            print("Yes")
            yes.append(word)
        else:
            print("No")
            no.append(word)
        print("")

    return double(yes, code + '1') | double(no, code + '0')


def double(data: list, code: str) -> dict:
    print('*' * 10 + "Calculate: " + code)
    if len(code) == MAX_DEPTH:
        return {code: data}

    yes = []
    no = []

    for word in data:
        print(f"Calculating for {word}")
        print(f"Finding valid doubles starting with: {word[-1]}?")
        for letter in range(97, 122):
            d = chr(letter)
            print(f"Connecting to {d}")
            val = word[-1] + d
            print(f"Is {val} a valid double?")
            if val in VALID_DOUBLES:
                print("yes")
                yes.append(word + d)
            else:
                print("no")
                no.append(word + d)
        print("")

    return single(yes, code + '1') | single(no, code + '0')


def main():
    data = single([chr(x) for x in range(97, 122)], '')

    output = ''
    full_output = ''
    for key in data:
        word = data[key]
        full_output += f"{key}: {word}\n"
        index = random.randint(0, len(word) - 1)
        output += f"{key},{data[key][index]}\n"

    print(full_output)
    with open('test-cases.txt', 'w') as stream:
        stream.write(output)


if __name__ == "__main__":
    main()
