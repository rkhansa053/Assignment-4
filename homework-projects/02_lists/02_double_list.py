# Write a program that doubles each element in a list of numbers. For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]


def main():
    numbers: list[int] = [2,7,9,6,4]

    for i in range(len(numbers)): 
        elem_at_index = numbers[i] 
        numbers[i] = elem_at_index * 2  

    print(numbers)



if __name__ == '__main__':
    main()


