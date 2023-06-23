from palindrome import is_palindrome

short = ""
shortest_list = []
longest_list = []
longest = ""
list = []

with open("words.txt") as file:
    for line in file:
        list.append(line[:-2]) #workaround for being unable to use rstrip, slice off escape characters. On my machine I got two, r and n

#init short with something
short = list[0]

for item in list:
    if is_palindrome(item):
        #new short
        if len(item) < len(short):
            short = item
            shortest_list = []
            shorest_list.append(short)
        #equal short
        elif len(item) == len(short):
            shortest_list.append(item)
        #new long
        elif len(item) > len(longest):
            longest = item
            longest_list = []
            longest_list.append(longest)
        #equal long
        elif len(item) == len(longest):
            longest_list.append(item)

print(shortest_list)
print(longest_list)
