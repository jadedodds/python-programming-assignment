def solution(A):
    # Start one pointer at each end of the array
    left = 0
    right = len(A) - 1

    # Keep track of the number of distinct absolute values
    count = 0

    # Continue until the pointers cross
    while left <= right:

        # Find the absolute values at both pointers
        left_abs = abs(A[left])
        right_abs = abs(A[right])

        # If the left absolute value is larger
        if left_abs > right_abs:
            current = left_abs

            # Skip all occurrences of this absolute value
            while left <= right and abs(A[left]) == current:
                left += 1

        # If the right absolute value is larger
        elif right_abs > left_abs:
            current = right_abs

            # Skip all occurrences of this absolute value
            while left <= right and abs(A[right]) == current:
                right -= 1

        # If both absolute values are equal
        else:
            current = left_abs

            # Skip matching values from the left
            while left <= right and abs(A[left]) == current:
                left += 1

            # Skip matching values from the right
            while left <= right and abs(A[right]) == current:
                right -= 1

        # Count this distinct absolute value
        count += 1

    return count
