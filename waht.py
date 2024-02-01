
def degreeToRad():
    degree = input("Degree: ")
    degNum = int(degree)
    angkol = input("circumference: ")
    radN = int(angkol)

    AngleD = degNum/1
    AngleR = 3.14/radN
    Result = AngleD * AngleR
    print(int(Result), "Rad")
degreeToRad()    

