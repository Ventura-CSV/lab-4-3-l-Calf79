def main():
    total = 0
    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input('enter value'))
    for numbers in numbers:
        total += numbers   
    
    """
    ########################################
    Code Your Program here
    ########################################
    """
    # total = sum(numbers)
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total, numbers


if __name__ == '__main__':
    main()
