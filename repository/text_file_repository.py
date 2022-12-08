from src.repository.repository import StudentRepository, DisciplineRepository, GradeBookRepository


class StudentTextFileRepository(StudentRepository):
    def __init__(self):
        super().__init__()
        self._file_name = 'C:\\Users\\Denisa\\Documents\\GitHub\\a9-914LaszloDenisa\\src\\files\\grade_book.txt'
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")
        for line in file.readlines():
            student_id, name = line.split(maxsplit=1, sep=',')
            self.add(int(student_id), name.rstrip())
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wt")  # wt -> write, text-mode
        for i in range(len(self._student_list)):
            file.write(str(self._student_list[i].student_id) + ',' + self._student_list[i].name + "\n")
        file.close()

    def add(self, student_id, student_name):
        super(StudentTextFileRepository, self).add(student_id, student_name)
        self._save_file()

    def remove(self, student_position_in_list):
        super(StudentTextFileRepository, self).remove(student_position_in_list)
        self._save_file()

    def update(self, student_position_in_list, new_student_name):
        super(StudentTextFileRepository, self).update(student_position_in_list, new_student_name)
        self._save_file()


class DisciplineTextFileRepository(DisciplineRepository):
    def __init__(self):
        super().__init__()
        self._file_name = "C:\\Users\\Denisa\\Documents\\GitHub\\a9-914LaszloDenisa\\src\\files\\disciplines.txt"
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")
        for line in file.readlines():
            discipline_id, name = line.split(maxsplit=1, sep=',')
            self.add(int(discipline_id), name.rstrip())
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wt")  # wt -> write, text-mode
        for i in range(len(self._discipline_list)):
            file.write(str(self._discipline_list[i].discipline_id) + ',' + self._discipline_list[i].name + "\n")
        file.close()

    def add(self, discipline_id, student_name):
        super(DisciplineTextFileRepository, self).add(discipline_id, student_name)
        self._save_file()

    def remove(self, discipline_position_in_list):
        super(DisciplineTextFileRepository, self).remove(discipline_position_in_list)
        self._save_file()

    def update(self, discipline_position_in_list, new_discipline_name):
        super(DisciplineTextFileRepository, self).update(discipline_position_in_list, new_discipline_name)
        self._save_file()


class GradeBookTextFileRepository(GradeBookRepository):
    def __init__(self):
        super().__init__()
        self._file_name = "C:\\Users\\Denisa\\Documents\\GitHub\\a9-914LaszloDenisa\\src\\files\\grade_book.txt"
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")
        for line in file.readlines():
            discipline_id, student_id, grade_value = line.split(maxsplit=2, sep=',')
            self.add(int(discipline_id), int(student_id), int(grade_value))
        file.close()

    def _save_file(self):
        f = open(self._file_name, "wt")  # wt -> write, text-mode
        for i in range(len(self._grade_book)):
            f.write(str(self._grade_book[i].discipline_id) + ',' + str(self._grade_book[i].student_id) + ',' +
                    str(self._grade_book[i].grade_value) + "\n")
        f.close()

    def add(self, discipline_id, student_id, grade_value):
        super(GradeBookTextFileRepository, self).add(discipline_id, student_id, grade_value)
        self._save_file()

    def remove_student_grades(self, student_id):
        super(GradeBookTextFileRepository, self).remove_student_grades(student_id)
        self._save_file()

    def remove_discipline_grades(self, discipline_id):
        super(GradeBookTextFileRepository, self).remove_discipline_grades(discipline_id)
        self._save_file()

    def remove_a_grade(self, discipline_id, student_id, grade_value):
        super(GradeBookTextFileRepository, self).remove_a_grade(discipline_id, student_id, grade_value)
        self._save_file()

    def add_student_average(self, student_id, average):
        pass

    def add_discipline_average(self, discipline_id, average):
        pass
