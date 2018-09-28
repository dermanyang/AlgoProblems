# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

def largest_na_sum(arr):
    # we'll use a arr to store incremental maximums (a la bottom-up DP)

    # initialize cache
    opt = [0] * (len(arr) + 1) # one extra for a zero (largest sum of 0 elements is 0)
    if arr[0] > 0:
        opt[1] = arr[0]

    for i in range (2, len(arr) + 1):
        opt[i] = max(opt[i-1], opt[i-2] + arr[i-1])

    return opt[len(opt) - 1]


# Here we notice that we're only using the latest two numbers in opt...
# instead of storing an entire array which takes O(n) space, let's just use two variables! which takes O(1) space

def largest_sum_v2(arr):
    # now, we'll just use two variables to track the i-2th position(cache1) and the i-1th position (cache2)
    # initialize cache
    cache1 = 0
    cache2 = 0
    largest_sum = 0

    for i in range (0, len(arr)):
        largest_sum = max(cache2, cache1 + arr[i])
        cache1 = cache2
        cache2 = largest_sum

    return largest_sum
