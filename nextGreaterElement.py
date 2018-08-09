# You are given two arrays (no duplicates): arr1 and arr2 where arr1 is a subset of arr2.
# For each item x in arr1 find the first proceeding number, y, in arr2 such that y > x and
# is to the right hand side of x in arr2. If such number does not exist, return -1.
#
# Ex.
# arr1 = [4, 1, 2]
# arr2 = [1, 3, 4, 2]
# output = [-1, 3, -1]
#
# the first number in arr1, 4,  all numbers to the right of 4 in arr2 are less than 4. Thus return -1
# the second number in arr1, 1, the first number greater than 1 in arr2 is 3
# the third number in arr1, 2, there are no more numbers to the right of 2 in arr2, so return -1

# the basic idea is to iterate through arr2 once while maintaining a stack
# for the i'th iteration, if the last item placed on the stack is less than
# arr2[i], then we know that arr[i] is the next largest element of arr2[i-1]
#
# once we have determined that arr2[i] is greater than the previous element,
# map that previous element to arr2[i] by popping the stack. if the new top
# value on the stack is still less than arr2[i], map that one too, etc.
# if, however, arr2[i] is not greater than the last element on the stack, push
# arr[2] onto the stack.

# finally, iterate through arr1 and replace each element in arr1 with the key/value
# counterpart in the map. If we never mapped it in map, then there is no next
# greater element, return -1

def nextGreaterElement(targetArr, numArr):
    dict = {} #hashmap
    stack = [] #stack using a list
    for num in numArr:
        while stack and stack[len(stack) - 1] < num:
            dict.update({stack.pop() : num})
        stack.append(num)

    for i in range(len(targetArr)):
        targetArr[i] = dict.get(targetArr[i], -1)

    return targetArr

#driver code
arr1 = [4,1,2]
arr2 = [1,3,4,2]

print(nextGreaterElement(arr1,arr2))
