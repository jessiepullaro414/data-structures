def mergeSort(A):
    print("Split ",A)
    if len(A)>1:
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                A[k]=lefthalf[i]
                i=i+1
            else:
                A[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            A[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            A[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merge ",A)

A = [54,26,9,17,7,1,4,55,20]
mergeSort(A)
print(A)
