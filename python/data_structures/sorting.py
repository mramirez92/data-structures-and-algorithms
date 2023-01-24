def insertion_sort(array):

    for i in range(1, len(array)):

        key_item = array[i]

        j = i - 1

        while j >= 0 and array[j] > key_item:

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item
    print(array)
    return array
   
def test_insertion_sort():
    # Test case 1: Check if the function sorts an array correctly
    array = [3, 2, 5, 1, 4]
    result = insertion_sort(array)
    expected = [1, 2, 3, 4, 5]
    assert result == expected
    print('pass')

def test_insertion_sort_2():
    array = [-2,3,5,7,13,11]
    result = insertion_sort(array)
    expected = [-2,3,5,7,11,13]
    assert result == expected
    print('pass')


test_insertion_sort()

test_insertion_sort_2()
  
