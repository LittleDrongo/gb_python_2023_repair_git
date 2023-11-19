def find_smallest(arr): #this function can find smallest item in array
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


array = [2, 1, 342, 100, 444]

print (array)
test = find_smallest(array)
print (test)

sorted_array = selection_sort(array)
print (sorted_array)
