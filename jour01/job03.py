class Operation():
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        result = self.number1 + self.number2
        print("le résultat de l'addition est de", result)

operation = Operation(12, 3)
operation.addition()