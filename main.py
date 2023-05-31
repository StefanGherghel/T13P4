from functional import seq

def isPrim(numar):
    ind = 2
    while ind<=numar/2:
        if(numar%ind==0):
            return False
        ind = ind+1
    return True

if __name__ == '__main__':
    listaMea = list([1,6,2,98,12,53,23,87,4])
    listaMea2 = seq(listaMea).filter(lambda element: isPrim(element) and element%2==1 and element<50)
    print(listaMea2)


