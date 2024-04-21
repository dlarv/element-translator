import sys

DEBUG_MODE = True
TEST_MODE = False


class Symbol:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value

    def clear(self):
        self.value = "00"

    def is_valid(self) -> bool:
        return self.value.find("*") == -1 and self.value != "00"

    def output(self) -> str:
        if self.is_valid():
            return self.value.replace('_', '').capitalize()
        return self.value.replace('*', '').replace('0', '').lower()

    def use_output(self) -> bool:
        return self.value != "00"


class Word:
    def __init__(self):
        self.letters = [Symbol("00")]
        # First loop increments this by 2.
        self.count = -1

    def append(self, val: str):
        self.letters.append(Symbol(val))

    def __repr__(self):
        return str(self.letters)

    def __str__(self):
        return ', '.join([s.output() for s in self.letters if s.use_output()])

    def has_next(self) -> bool:
        return self.count < len(self.letters) - 3

    def peek(self) -> str:
        '''Show the window value of next slice'''
        if not self.has_next():
            return ''

        initial_count = self.count
        output = self.next()
        self.count = initial_count
        return output[0]

    def next(self) -> tuple[str]:
        '''Returns (???, PC, C*, CN),
        where ??? is the binary representation of the slice.
        '''
        self.count += 2
        output = [""]
        for i in -1, 0, 1:
            if self.letters[self.count + i].is_valid():
                output[0] += "1"
            else:
                output[0] += "0"

            output.append(self.letters[self.count + i])

        return output

    def set_prev(self):
        '''Case: 100
            (P)rev and (C)urr are claimed
            O* OP P* (PC C* CN) N*
            O* 00 00 (PC 00 00) N*
            Clear previous two letters and next two letters.
        '''
        # Set index to first symbol containing 'P' char.
        start = max(0, self.count - 3)
        end = self.count + 1

        for i in range(start, end):
            # Skip Symbol that is being set.
            if i == self.count - 1:
                log(f"Setting: {self.letters[i]}")
                continue

            log(f"Clearing: {self.letters[i]}")
            self.letters[i].clear()

    def set_mid(self):
        '''Case: 010
        (C)urr is claimed.
        P* (PC C* CN) N*
        P* (00 C* 00) N*
        '''
        log(f"Clearing: {self.letters[self.count - 1]}")
        self.letters[self.count - 1].clear()
        log(f"Settings: {self.letters[self.count]}")
        log(f"Clearing: {self.letters[self.count + 1]}")
        self.letters[self.count + 1].clear()

    def set_next(self):
        '''Case: 001
            (C)urr and (N)ext are claimed
            P* (PC C* CN) N* NO O*
            P* (00 00 CN) 00 00 O*
        '''
        start = self.count - 1
        end = min(self.count + 3, len(self.letters) - 1)

        for i in range(start, end + 1):
            if i == self.count + 1:
                log(f"Setting: {self.letters[i]}")
                continue

            log(f"Clearing: {self.letters[i]}")
            self.letters[i].clear()

        # Skip over next symbol, as it was previously cleared.
        self.count += 4

    def chain_break(self):
        '''Fast forward until chain ending symbol is found (Either 100 or 110)
           Set symbol (breaking the chain) and resume back at previous count.
        '''
        # Next iteration the current slice should be evaluated again.
        initial_count = self.count - 2
        # Word must end with 100 or 110 because final letter
        # and empty space is always invalid.
        while self.has_next():
            next = self.next()[0]
            if next[-1] == "1":
                continue
            else:
                self.set_prev()
                break
        self.count = initial_count

    def test_mode_output(self):
        '''Return count of invalid symbols and unformatted array'''
        count = len([x for x in self.letters if x.value.find("*") != -1])
        arr = [s.output() for s in self.letters if s.use_output()]
        return count, arr


def log(msg: str):
    if DEBUG_MODE:
        print(msg)


# 1. Load elements.
# 2. Get input from user.
# 3. Convert input into proper formatting.
# 4. Execute
# 5. Clean up output.
def main(args):
    global DEBUG_MODE, TEST_MODE

    # Evaluate args
    if len(args) > 0:
        DEBUG_MODE = False

    user_inputs = []
    for arg in args:
        match arg:
            case "--debug" | "-d":
                DEBUG_MODE = True
            case "--no-debug" | "-D":
                DEBUG_MODE = False
            case "--test" | "-t":
                TEST_MODE = True
            case "--help" | "-h":
                print("python3 {executable} [opts] [word]")
                print("Opts")
                print("-h | --help: Print this menu.")
                print("-d | --debug: Print debug statements to console.")
                print("-D | --no-debug: Don't print debug statements.")
                exit(0)
            case _:
                if arg[0] == '-':
                    print(f"Unknown arg: '{arg}", file=sys.stderr)
                    exit(1)
                user_inputs.append(arg)

    # Read elements from file
    with open('../../elements.csv') as stream:
        elements = [x.strip() for x in stream.read().split(',')]

    # Get user input and add padding
    if len(user_inputs) == 0:
        if DEBUG_MODE:
            user_inputs = ['thermodynamics']
        else:
            user_inputs = input("Enter word or list of words delimited by spaces: ")
            user_inputs = user_inputs.split(" ")

    test_results = []
    for user_input in user_inputs:
        word = convert(f"0{user_input}0", elements)
        word = transform(word, elements)

        # Cleanup and print
        # Output is cleaned up in Word's to string implemention
        if not TEST_MODE:
            print(f"{word}")
        else:
            test_results.append(word.test_mode_output())

    if TEST_MODE:
        return test_results


# Iterate over letters.
# Check if letter by itself is a valid symbol:
#   if true: a_ else: a*
# Check if current letter + next letter is a valid symbol
def convert(user_input: str, elements: list) -> Word:
    output = Word()

    # Skip last letter (padding='0')
    while len(user_input) > 2:
        i = 1
        n = 2

        curr = user_input[i] + '_'
        if curr not in elements:
            curr = user_input[i] + '*'
        output.append(curr)

        next = user_input[i:n + 1]
        if next not in elements:
            next = '00'
        output.append(next)

        # Discard previous letter
        user_input = user_input[1:]

        log(f"Output is now: {output}")
    return output


def transform(word: Word, elements: list) -> Word:
    while word.has_next():
        window, prev, curr, next = word.next()
        log(f"Slice: {prev}, {curr}, {next}")
        match window:
            case "100" | "110":
                word.set_prev()
            case "010":
                word.set_mid()
            case "001":
                word.set_next()
            case "011":
                if word.peek()[-1] == "0":
                    word.set_next()
                # Consider a chain of symbols starting with 011
                # and ending with 100.
                # If there are an even number of symbols chain, 011 -> 001
                # Otherwise, 011 -> 010
                # If it ends with 110, it doesn't matter which option is taken.
                else:
                    word.chain_break()
            # 101, 111 become 001 & 011 due to prior rule.
            # otherwise, skip 000
            case _:
                continue
    return word


if __name__ == "__main__":
    # Skip executable argument
    main(sys.argv[1:])
