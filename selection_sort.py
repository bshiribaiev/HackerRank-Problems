def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]

arr = [432, 423, 3, 42]       

selection_sort(arr)
print(arr)
