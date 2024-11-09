from functools import reduce

def product_of_all_other_numbers(numbers):
    new_list = []
    for i in range(len(numbers)):
        # Multiply all numbers except the current number
        new_list.append(reduce(lambda x, y: x * y, numbers[:i] + numbers[i+1:]))
    return new_list

if __name__ == "__main__":
    assert product_of_all_other_numbers([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    print(product_of_all_other_numbers([1, 2, 3, 4, 5]))

    assert product_of_all_other_numbers([3, 2, 1]) == [2, 3, 6]
    print(product_of_all_other_numbers([3, 2, 1]))