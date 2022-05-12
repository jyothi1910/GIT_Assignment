def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]


##1st method of taking array as input
arr = list(map(int, input("Enter the arry elements:").strip().split()))
print(arr)

##2nd method to take array as input
arr=[]
n = int(input("Number of elements in array:"))
for i in range(0,n):
    l = int(input())
    arr.append(l)

##3rd method
arr = [64,34,25,22,11]


bubbleSort(arr)
print("Sorted arry is:")
for i in range(len(arr)):
    print("%d" %arr[i] , end = " ")
