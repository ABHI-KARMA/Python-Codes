if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(list(integer_list))
    print(hash(t))
    

    
# map(function, iterable)
#function: A mandatory function to be given to map, that will be applied to all the items available in the iterator.
#iterator: An iterable compulsory object. It can be a list, a tuple, etc. You can pass multiple iterator objects to map() function.

# str.split(separator, maxsplit)
# separator (optional)- Delimiter at which splits occur. If not provided, the string is splitted at whitespaces.
# maxsplit (optional) - Maximum number of splits. If not provided, there is no limit on the number of splits.
