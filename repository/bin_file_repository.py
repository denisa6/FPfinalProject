from src.repository.repository import StudentRepository, DisciplineRepository, GradeBookRepository
import pickle


class StudentBinFileRepository(StudentRepository):
    def __init__(self):
        super().__init__()
        self._file_name = "C:\\Users\\Denisa\\Documents\\GitHub\\a9-914LaszloDenisa\\src\\files\\students.bin"
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rb")  # rt -> read, binary
        self._student_list = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self._student_list, file)
        file.close()

    def add(self, student_id, student_name):
        super(StudentBinFileRepository, self).add(student_id, student_name)
        self._save_file()

    def remove(self, student_position_in_list):
        super(StudentBinFileRepository, self).remove(student_position_in_list)
        self._save_file()

    def update(self, student_position_in_list, new_student_name):
        super(StudentBinFileRepository, self).update(student_position_in_list, new_student_name)
        self._save_file()


class DisciplineBinFileRepository(DisciplineRepository):
    def __init__(self):
        super().__init__()

        self._file_name = "C:\\Users\\Denisa\\Documents\\GitHub\\a9-914LaszloDenisa\\src\\files\\disciplines.bin"
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rb")  # rt -> read, binary
        self._discipline_list = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self._discipline_list, file)
        file.close()

    def add(self, discipline_id, discipline_name):
        super(DisciplineBinFileRepository, self).add(discipline_id, discipline_name)
        self._save_file()

    def remove(self, discipline_position_in_list):
        super(DisciplineBinFileRepository, self).remove(discipline_position_in_list)
        self._save_file()

    def update(self, discipline_position_in_list, new_discipline_name):
        super(DisciplineBinFileRepository, self).update(discipline_position_in_list, new_discipline_name)
        self._save_file()


class GradeBookBinFileRepository(GradeBookRepository):
    def __init__(self):
        super().__init__()

        self._file_name = "C:\\Users\\Denisa\\Documents\\GitHub\\a9-914LaszloDenisa\\src\\files\\grade_book.bin"
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rb")  # rt -> read, binary
        self._grade_book = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")  # wb -> write, binary
        pickle.dump(self._grade_book, file)
        file.close()

    def add(self, discipline_id, student_id, grade_value):
        super(GradeBookBinFileRepository, self).add(discipline_id, student_id, grade_value)
        self._save_file()

    def remove_student_grades(self, student_id):
        super(GradeBookBinFileRepository, self).remove_student_grades(student_id)
        self._save_file()

    def remove_discipline_grades(self, discipline_id):
        super(GradeBookBinFileRepository, self).remove_discipline_grades(discipline_id)
        self._save_file()

    def remove_a_grade(self, discipline_id, student_id, grade_value):
        super(GradeBookBinFileRepository, self).remove_a_grade(discipline_id, student_id, grade_value)
        self._save_file()
