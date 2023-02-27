class Operation():
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

        print("le nombre 1 est égal à", self.number1)
        print("le nombre 2 est égal à", self.number2)

#Instanciation de la classe
operation = Operation(12, 3)
