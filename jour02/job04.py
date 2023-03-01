class Student:
    def __init__(self, first_name, last_name, student_id):
        self._first_name = first_name 
        self._last_name = last_name 
        self._student_id = student_id 
        self._credits = 0
        self._level = self._studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits 
    
    def studentInfo(self):
        print("Student name is:", self._first_name, self._last_name)
        print("Student ID is :", self._student_id)
        print("Credits :", self._credits)
        print("Level is :", self._level)


    def _studentEval(self):
        if self._credits == 90:
            return "Bien !"
        elif self._credits >= 80:
            return "Pas mal !"
        elif self._credits >= 70:
            return "En vrai ça va"
        else:
            return "Bien !"

# Instanciation de l'objet représentant l'étudiant nommé John Doe ayant 145 comme numéro : 
john = Student("John","Doe", 145)

#Ajout de crédits à trois reprises
john.add_credits(40)
john.add_credits(10)
john.add_credits(40)

john.studentInfo()