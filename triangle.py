def solution(A):
    # Sort the array in ascending order
    A.sort()

    # Check each group of three consecutive numbers
    for i in range(len(A) - 2):

        # Check if these three numbers can form a triangle
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    # Return 0 if no valid triangle is found
    return 0
