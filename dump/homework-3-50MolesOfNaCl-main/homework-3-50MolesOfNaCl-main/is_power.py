def is_power(a, b):
    #print(a, b) ##debug
    if type(a) is not int or type(b) is not int:
        return None
    if b == 1 or a == b:
        return True
    elif a % b == 0:
        #print((a/b)% b) ##debug
        return is_power(int(a/b), b) #int to stop py from passing a a float
    else:
        return False

if __name__ == "__main__":
    # Put your test code here!
    print(is_power(8, 2), " == True")
    print(is_power(16, 4), " == True")
    print(is_power(10, 1), " == True")
    print(is_power(8, 3), " == False")
    print(is_power(8, 3.5), " == None")
    print(is_power(8.5, 3), " == None")
    print(is_power(8.5, 3.5), " == None")


