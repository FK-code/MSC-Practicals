def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 key < arr[j]:
            arr[j+1]=arr[j+1]
            j-=1
        ar