def quicksort(my_list, l_index, r_index):

    if r_index < l_index:
       return


def setup():

    pivot = l_index + round((r_index - l_index) /2)
    last_l_index = l_index
    last_r_index = r_index
    swap_left = False
    swap_right = False


def swap_items(l, r):

    my_list.insert(r, my_list[l])
    del (my_list[l])
    my_list.insert(l, my_list[r])
    del (my_list[r + 1])

def sort_sub:

    while r_index > pivot or l_index < pivot:

    if my_list[l_index] >= my_list[pivot]:
        swap_right = True
        elif l_index != pivot:
           l_index += 1

        if my_list[r_index] <= my_list[pivot]:
            swap_left = True
        elif r_index != pivot:
            r_index -=1

        if swap_right and swap_left:
            print("Cond 1")
            swap_items(l_index, r_index)
            print(my_list)
            l_index += 1
            r_index -= 1
            swap_left = False
            swap_right = False

        elif swap_right and r_index == pivot:
            print("Cond 2")
            swap_items(l_index, pivot)
            print(my_list)
            pivot = l_index
            swap_right = False

        elif swap_left and l_index == pivot:
            print(f"Swap {pivot}, {r_index}")
            swap_items(pivot, r_index)
            print(my_list)
            pivot = r_index
            print(pivot)
            swap_left = False


#    quicksort(my_list, last_l_index, pivot - 1)
#    quicksort(my_list, pivot + 1, last_r_index)


