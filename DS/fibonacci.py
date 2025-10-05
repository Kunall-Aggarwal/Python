def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b



def max_subarray_sum(arr):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.

    Args:
        arr: A list of integers.

    Returns:
        The maximum sum of a contiguous subarray.
    """
    if not arr:
        # Handle empty array case: an empty array has no non-empty subarray.
        # Depending on problem constraints, you might raise an error or return a specific value.
        # Here, we raise a ValueError for clarity.
        raise ValueError("Input array cannot be empty.")

    max_so_far = arr[0]  # Stores the maximum sum found globally so far
    current_max = arr[0] # Stores the maximum sum ending at the current position

    for i in range(1, len(arr)):
        # At each position, decide whether to extend the previous subarray
        # or start a new subarray from the current element.
        current_max = max(arr[i], current_max + arr[i])

        # Update the overall maximum sum if the current_max is greater.
        max_so_far = max(max_so_far, current_max)

    return max_so_far