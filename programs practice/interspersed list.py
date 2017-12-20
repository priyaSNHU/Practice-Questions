def main():

    a_list = []
    num = int(input('Enter the number of elements: '))
    for i in range(0,num):
        num_item = input('enter the elements in the array: ')
        a_list.append(num_item)


    print(a_list)

    search_element = input('enter the element you want to search for: ')
    bin_search(a_list , search_element)

def bin_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        mid_point = (first+last)//2
        if (a_list[mid_point] == item):
            found = True
            print('The element is found at %d', mid_point)
        else:
            if (item < a_list[mid_point] ):
                last = mid_point-1
            else:
                first = mid_point+1
    return found

main()
