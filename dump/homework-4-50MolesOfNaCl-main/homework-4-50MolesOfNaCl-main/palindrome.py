def is_palindrome(string):
    nstring = slicer(string)
    rstring = nstring[::-1] #More slicing abuse, reverse string with slice
    return nstring == rstring

#abusing slice notation to recursively cut and merge string without the whitespace
#no particular reason for doing this way
def slicer(string):
    if string == None or len(string) == 0:
        return ''
    else:
	#hunt for whitespace
        for i in range(0, len(string)):
            if string[i] == ' ':
                return string[0:i] + slicer(string[i+1:])
        #if string has no whitespace
        return string

#reread instrunctions, just pretend it was named is_palindrome
def is_palindrome2(string):
    #kill whitespace
    if " " in string:
        string = slicer(string)
    #base
    if string == [''] or string == "":
        return True
    elif string[0] == string[-1:]:
        return is_palindrome2(string[1:-1]) #cut off head and tail
    else:
        #catch all
        return False

if __name__ == '__main__':
    print("able was I ere I saw elba (True):", is_palindrome2("able was I ere I saw elba"))
    print("mr owl ate my metal worm (True):", is_palindrome2("mr owl ate my metal worm"))
    print("foo bar fizz (False):", is_palindrome2("foo bar fizz"))
    print("AAAA AAAA AAA AAAA AAAA AAAA (True):",is_palindrome2("AAAA AAAA AAAA AAAA AAAA AAAA"))
    print("boob (True):",is_palindrome2("boob"))
    print("tacocat   (True):",is_palindrome2("tacocat  "))
    # Put your test code here
