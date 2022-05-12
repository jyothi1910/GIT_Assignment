arr = [34,76,53,98,12]
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1,len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j

    arr[i] , arr[min_idx] = arr[min_idx] , arr[i]


print("Sorted array is :")
for i in range(len(arr)):
    print("%d" %arr[i] , end=" ")
