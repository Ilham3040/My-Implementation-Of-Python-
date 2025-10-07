myarr = [1,2,3,4,5]

def addingsomeelement(arr):
    arr[-1] = arr[0]

addingsomeelement(myarr)
print(myarr)

def changingsome(something):
    something = "okay"
    
notgood = "whatever"
changingsome(notgood)
print(notgood)