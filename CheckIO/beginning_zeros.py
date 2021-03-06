

def beginning_zeros(number: str) -> int:

    count_zeroes = 0

    # Percorre a string de frente para trás
    for index in range(len(number)):
        if number[index] == '0':
            count_zeroes += 1
        else:
            break

    return count_zeroes


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('00100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")