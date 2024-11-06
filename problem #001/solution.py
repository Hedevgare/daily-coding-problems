def has_pair_with_sum(numbers, k):
    # Initialize a set to store potential solutions
    solutions = set()
    for i in range(len(numbers)):
        # Check if the current element is in the set of solutions; if it is, return True
        if numbers[i] in solutions:
            return True
        # Add the difference between the target and the current element to the set of solutions
        solutions.add(k - numbers[i])
    # If no solution is found, return False
    return False

if __name__ == "__main__":
    assert has_pair_with_sum([10, 15, 3, 7], 17) == True
    print(has_pair_with_sum([10, 15, 3, 7], 17))

    assert has_pair_with_sum([12, 5, 2, 11, 8], 16) == True
    print(has_pair_with_sum([12, 5, 2, 11, 8], 16))

    assert has_pair_with_sum([7, 14, 1, 9], 11) == False
    print(has_pair_with_sum([7, 14, 1, 9], 11))

    assert has_pair_with_sum([], 5) == False
    print(has_pair_with_sum([], 5))