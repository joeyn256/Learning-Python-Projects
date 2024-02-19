def Attempt2(list1, index):
    start_index = 1
    end_index = len(list1) - 1
    while True:
        middle_index = (end_index - start_index) / 2
        if middle_index < 0 or middle_index < start_index or middle_index > end_index:
            return False

        middle_element = list1[middle_index]
        if middle_element == index:
            return True
        elif middle_element < index:
            end_index = middle_index
        else:
            start_index = middle_index

    x1 = Attempt2([1,2,3,4,5,6,7], 5)
    if x1 == true:
        print('yes')
    else:
        print('no')
