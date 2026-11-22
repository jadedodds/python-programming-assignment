
def solution(A):
    # Create a set to store distinct values
    distinct_values = set()

    # Loop through every element in the array
    for number in A:
        distinct_values.add(number)

    # Return the number of distinct values
    return len(distinct_values)
