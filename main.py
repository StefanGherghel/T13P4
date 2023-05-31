from functional import seq

if __name__ == '__main__':
    text = "acesta este textul care se va reuni dupa prima litera din fiecare cuvant din el"
    listaMea = text.split(" ")
    print(listaMea)
    listaMea2 = seq(listaMea).map(lambda element: [element[0], element])
    print(listaMea2)
    listaMea3 = listaMea2.group_by(lambda element: element[0]).map(lambda element: [element[0],element[1]])
    print(listaMea3)

