def bubbleSort(arr):
    n=len(arr)
    for i in range (n):
        for j in range(j+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[j]
    return arr