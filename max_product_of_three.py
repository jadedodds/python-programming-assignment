
def solution(A):
    # Sort the array in ascending order
    A.sort()

    # Calculate the product of the three largest numbers
    largest_product = A[-1] * A[-2] * A[-3]

    # Calculate the product of the two smallest
    # numbers and the largest number
    negative_product = A[0] * A[1] * A[-1]

    # Return whichever product is greater
    return max(largest_product, negative_product)
