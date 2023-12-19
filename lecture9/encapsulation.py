class StudyCourse:
    def __init__(self) -> None:
        self.__students = []

    def add_students(self, mat_nrs : list) -> None:
        self.__students.extend(mat_nrs)

    def is_immatriculated(self, mat_nr : str) -> bool:
        return mat_nr in self.__students
    
egm = StudyCourse()
egm.add_students(["shk0812", "jh6835", "shi0820"])
print(egm.__students)
