from src.domain.domain import Student, Discipline, Grade


class StudentRepository:
    def __init__(self):
        self._student_list = []

    def add(self, student_id, student_name):
        """
        This function adds the given information to the student_list
        :param student_id: the id of the new student
        :param student_name: the name of the new student
        """
        new_student = Student(student_id, student_name)
        self._student_list.append(new_student)

    def remove(self, student_position_in_list):
        """
        This function removes a certain student from the student_list
        :param student_position_in_list: the position of the student in the student_list
        """
        self._student_list.pop(student_position_in_list)

    def update(self, student_position_in_list, new_student_name):
        """
        This function updates a student's information
        :param student_position_in_list: the position of the student that needs their information updated
        :param new_student_name: the new name of the student
        """
        setattr(self._student_list[student_position_in_list], "_name", new_student_name)

    def get_student_list(self):
        return self._student_list


class DisciplineRepository:
    def __init__(self):
        self._discipline_list = []

    def add(self, discipline_id, discipline_name):
        """
        This function adds a new discipline to the discipline_list
        :param discipline_id: the id of the new discipline
        :param discipline_name: the name of the new discipline
        """
        new_discipline = Discipline(discipline_id, discipline_name)
        self._discipline_list.append(new_discipline)

    def remove(self, discipline_position_in_list):
        """
        This function removes a certain discipline from the discipline_list
        :param discipline_position_in_list: the position of the discipline that's gonna be removed
        """
        self._discipline_list.pop(discipline_position_in_list)

    def update(self, discipline_position_in_list, new_discipline_name):
        """
        This function updates a discipline's information
        :param discipline_position_in_list: the position of the discipline in the discipline_list
        :param new_discipline_name: the new name of the discipline
        """
        setattr(self._discipline_list[discipline_position_in_list], "_name", new_discipline_name)

    def get_discipline_list(self):
        return self._discipline_list


class GradeBookRepository:
    def __init__(self):
        self._grade_book = []
        self._students_with_grades = []
        self._disciplines_with_grades = []

    def add(self, discipline_id, student_id, grade_value):
        """
        This function adds a new grade to the grade book (list of all grades)
        :param discipline_id: the id of the discipline where the grade was given
        :param student_id: the id of the student who received the grade
        :param grade_value: natural number between 0 and 10,  the value of the grade
        """
        new_grade = Grade(discipline_id, student_id, grade_value)
        self._grade_book.append(new_grade)

    def remove_student_grades(self, student_id):
        """
        This function removes all of the grades of a student
        :param student_id: the student who needs their grades removed
        """
        i = 0
        while i < len(self._grade_book):
            if self._grade_book[i].student_id == student_id:
                self._grade_book.pop(i)
            else:
                i = i + 1

    def remove_discipline_grades(self, discipline_id):
        """
        This function removes all grades from a given discipline
        :param discipline_id: the id of the discipline where the grades will be removed
        """
        i = 0
        while i < len(self._grade_book):
            if self._grade_book[i].discipline_id == discipline_id:
                self._grade_book.pop(i)
            else:
                i = i + 1

    def remove_a_grade(self, discipline_id, student_id, grade_value):
        """
        This function removes a grade from the grade book
        :param student_id: the id of the student who received the grade
        :param discipline_id: the id of the discipline where the grade was given
        :param grade_value: the grade itself
        """
        i = 0
        while i in range(len(self._grade_book)):
            if self._grade_book[i].student_id == student_id and self._grade_book[i].discipline_id == discipline_id and \
               self._grade_book[i].grade_value == grade_value:
                self._grade_book.pop(i)
            else:
                i = i + 1

    def add_student_average(self, student_id, average):
        """
        This function adds a student's average to the students_with_grades list
        :param student_id: the id of the student
        :param average: the average grade of the student
        """
        student_information = {'id': student_id, 'average grade': average}
        self._students_with_grades.append(student_information)

    def add_discipline_average(self, discipline_id, average):
        """
        This function adds a discipline's average to the disciplines_with_grades list
        :param discipline_id: the id of the discipline
        :param average: the average of the discipline
        """
        discipline_information = {'id': discipline_id, 'average grade': average}
        self._disciplines_with_grades.append(discipline_information)

    def get_grade_book(self):
        return self._grade_book

    def get_students_with_grades(self):
        return self._students_with_grades

    def get_disciplines_with_grades(self):
        return self._disciplines_with_grades
