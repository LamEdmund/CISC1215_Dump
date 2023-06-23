def remove_duplicates(lst):
    for i in lst:
        cnt = lst.count(i)
        if cnt > 1:
            # using built in list function remove() to remove the first instance if an element
            for j in range(1,cnt):
                lst.remove(i)
    return lst.sort() #return list as sorted since remove method may make it unsorted

#Why not?
def remove_duplicates2(lst):
    for i in lst:
        while lst.count(i) > 1:
            lst.remove(i)
    return lst.sort()

if __name__ == '__main__':
    a = [1, 2, 1, 1]
    b = [1,1,2,2,3,3,4,4,1,1,2,2,5,5,6,6,7,7,8,9,0]
    remove_duplicates(a)
    remove_duplicates2(b)
    print(a)
    print(b)
