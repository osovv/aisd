MAX_ITER = 1000


def verify_bracket_sequence(expression: str) -> bool:
    bracket_list = []
    for character in expression:
        if character == '(':
            bracket_list.append(')')
        if character == ')':
            if len(bracket_list) == 0 or bracket_list[-1] != character:
                return False
            bracket_list.pop()
    return len(bracket_list) == 0


def main():
    input_str = ''
    for i in range(MAX_ITER):
        input_str = input('Enter bracket sequence: ')
        if input_str == ' ':
            break
        output_str = "Sequence is correct"\
            if verify_bracket_sequence(input_str)\
            else "Sequence is not correct"
        print(output_str)


if __name__ == "__main__":
    main()
