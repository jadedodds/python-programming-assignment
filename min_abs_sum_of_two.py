def solution(A):
    # Sort the array in ascending order
    A.sort()

    # Start pointers at both ends of the array
    left = 0
    right = len(A) - 1

    # Start with the largest possible absolute sum
    min_sum = float('inf')

    # Continue while the pointers have not crossed
    while left <= right:

        # Calculate the absolute sum of the two values
        current_sum = abs(A[left] + A[right])

        # Update the minimum if a smaller sum is found
        min_sum = min(min_sum, current_sum)

        # If the sum is zero, it is the smallest possible
        if current_sum == 0:
            return 0

        # If the sum is negative before taking absolute value,
        # move the left pointer to a larger number
        if A[left] + A[right] < 0:
            left += 1

        # Otherwise, move the right pointer to a smaller number
        else:
            right -= 1

    return min_sum
