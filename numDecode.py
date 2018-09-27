# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

def numDecode(str):
    if len(str) == 2: # must be between 'a' and 'z' and thus has 2 decodings
        if int(str) in range(1,27):                              # one for two chars and one for one char
            return 2
        return 1
    if  len(str) == 1:  # digit must be between 1 and 9 i.e. 'a' thru 'j'
        return 1
    # here, the str has at least length 3...
    if int(str[0:2]) in range(1,27):
        return numDecode(str[1:]) + numDecode (str[2:])
    return numDecode(str[1:])

#   this is easily memoizable

def numDecodeHelper(str):
    mem = {} # empty dictionary

    def numDecodeDP(str):
        if len(str) == 2: # must be between 'a' and 'z' and thus has 2 decodings
            if int(str) in range(1,27):                                     # one for two chars and one for one char
                return 2
            return 1
        if  len(str) == 1:  # digit must be between 1 and 9 i.e. 'a' thru 'j'
            return 1
        # here, the str has at least length 3...
        # let's first check if we've done these caluclations before!

        #adjust scopes
        nonlocal mem

        # slice1
        if str[1:0] in mem:
            slice1 = mem[str[1:0]]
        else:
            slice1 = numDecode(str[1:])
        if str[2:0] in mem:
            slice2 = mem[str[2:0]]
        else: slice2 = numDecode(str[2:])

        if int(str[0:2]) in range (1,27):
            return slice1 + slice2
        return slice1

    # return function call
    return numDecodeDP(str)

print (numDecodeHelper('1234'))
