from functional import seq

if __name__ == '__main__':
    listaMea = list([1, 21, 75, 39, 7, 2, 35, 3, 31, 7, 8])

    listaMea2 = seq(listaMea).filter(lambda elem: elem>5)           #a)
    print(listaMea2)

    listaMea3 = seq(listaMea2).grouped(2)                            #b)
    print(listaMea3)

    listaMea4 = seq(listaMea3).map(lambda elem: elem[0]*elem[1])     #c)
    print(listaMea4)

    listaMea5 = seq(listaMea4).sum()
    print(listaMea5)

