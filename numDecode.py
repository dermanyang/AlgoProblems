# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

def numDecode(str):
    if len(str) == 2 and int(str) in (1,27): # must be between 'a' and 'z' and thus has 2 decodings
                                             # one for two chars and one for one char
        return 2
    if  len(str) == 1:  # digit must be between 1 and 9 i.e. 'a' thru 'j'
        return 1
    # here, the str has at least length 3...
    if int(str[0:2]) in range (1,27):
        return 2 + numDecode(str[1:]) + numDecode (str[2:])
    return 1 + numDecode(str[1:]) + numDecode (str[2:])
