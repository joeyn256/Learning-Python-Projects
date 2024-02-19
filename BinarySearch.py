def NonBinary(list1, a1):
    p = 0
    for x in list1:
        if x == a1:
            return True
        return False

x1 = NonBinary([1,2,3,4,5,6,7], 5)
print(x1)
x2 = NonBinary([1,2,3,4,5,6,7], 8)
print(x2)

def Binary(list1, a1):
    while True:
        l1 = len(list1)
        l2 = l1 / 2
        if list1(l2) > a1:
            while (l2 < l1):
                list1.pop(l2)
                l2 = l2 + 1
        else:
            while (0 < l2):
                list1.pop(l2)
                l2 = l2 - 1
        if len(list1) == 1:
            if (a1 == list1[0]):
                print('Element is in list')
                break
            else:
                print('Element is not in list')
                break
##solution below... I was deleting items in the list, this simply goes through indexes and is much better

def find(ordered_list, element_to_find):
  start_index = 1
  end_index = len(ordered_list) - 1
  
  while True:
    middle_index = (end_index - start_index) / 2
    
    if middle_index < start_index or middle_index > end_index or middle_index < 0:
      return False
    
    middle_element = ordered_list[middle_index]
    if middle_element == element_to_find:
      return True
    elif middle_element < element_to_find:
      end_index = middle_index
    else:
      start_index = middle_index

def Attempt2(list1, index):
    start_index = 0
    end_index = len(list1) - 1
    while True:
        middle_index = (end_index - start_index) / 2
        if middle_index < 0:
            return False

        middle_element = list1[middle_index]
        if middle_element == index:
            return True
        elif middle_element < index:
            end_index = middle_index
        else:
            start_index = middle_index
    
x1 = Attempt2([1,2,3,4,5,6,7], 5)
print(x1)
            

