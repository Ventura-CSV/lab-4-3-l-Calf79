def main():
    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input(f'Enter a value {i+1}:'))
    total = 0
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
