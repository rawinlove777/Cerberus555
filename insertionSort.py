data = [4,3,1,5,2]

def InsertionSort(a):
    for j in range(len(a)):
        key = a[j]
        i = j
        while i > 0 and a[i-1] > key:
            a[i] = a[i-1]
            i = i-1
        a[i] = key
print("Insertion Sort")
print("Input",data)
InsertionSort(data)
print("Output",data)

        


       
