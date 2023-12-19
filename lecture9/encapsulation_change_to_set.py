class StudyCourse:
    def __init__(self) -> None:
        self.__students = set()

    def add_students(self, mat_nrs : list) -> None:
        self.__students.update(mat_nrs)

    def is_immatriculated(self, mat_nr : str) -> bool:
        return mat_nr in self.__students 
    
egm = StudyCourse()
egm.add_students(["shk0812", "jh6835", "shi0820"])
print("hi")