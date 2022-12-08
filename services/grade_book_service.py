from src.repository.repository import GradeBookRepository
from src.services.exceptions import InvalidGrade


class GradeBookService:
    def __init__(self, grade_book_repository: GradeBookRepository):
        self._grade_book_repository = grade_book_repository

    @staticmethod
    def verify_grade_validity(grade_value):
        """
        This function verifies if the grade is valid or not
        :param grade_value: the grade that needs to be verified
        :return: True if the grade is valid, False if it isn't
        """
        if 0 <= grade_value <= 10:
            return True
        else:
            return False

    def add_grade(self, discipline_id, student_id, grade_value):
        """
        This function adds a new grade to the grade book (list of all grades)
        :param discipline_id: the id of the discipline where the grade was given
        :param student_id: the id of the student who received the grade
        :param grade_value: the value of the new grade
        """
        if self.verify_grade_validity(grade_value) is True:
            self._grade_book_repository.add(discipline_id, student_id, grade_value)
        else:
            raise InvalidGrade

    def remove_student_grades(self, student_id):
        """
        This function removes all grades of a given student
        :param student_id: the id of the student
        """
        self._grade_book_repository.remove_student_grades(student_id)

    def remove_discipline_grades(self, discipline_id):
        """
        This function function removes all grades of a given discipline
        :param discipline_id: the id of the discipline
        """
        self._grade_book_repository.remove_discipline_grades(discipline_id)

    def remove_grade(self, discipline_id, student_id, grade_value):
        """
        This function removes a certain grade from the grade book
        :param student_id: the id of the student who received the grade
        :param discipline_id: the id of the discipline where the grade was given
        :param grade_value: the grade itself
        """
        self._grade_book_repository.remove_a_grade(discipline_id, student_id, grade_value)

    def student_average_at_a_discipline(self, student_id, discipline_id):
        """
        This function computes the average grade of a student at a given discipline
        :param student_id: the id of the student
        :param discipline_id: the id of the discipline
        :return: the average grade of that student at that discipline
        """
        sum_of_grades = 0
        grades_number = 0
        grade_book = self._grade_book_repository.get_grade_book()
        for i in range(len(grade_book)):
            if grade_book[i].student_id == student_id and grade_book[i].discipline_id == discipline_id:
                sum_of_grades = sum_of_grades + grade_book[i].grade_value
                grades_number = grades_number + 1
        average = float(sum_of_grades / grades_number)
        return average

    def discipline_average(self, discipline_id):
        """
        This function computes the average grade at a given discipline
        :param discipline_id: the id of the discipline
        :return: the average grade
        """
        sum_of_grades = 0
        grades_number = 0
        grade_book = self._grade_book_repository.get_grade_book()
        for i in range(len(grade_book)):
            if grade_book[i].discipline_id == discipline_id:
                sum_of_grades = sum_of_grades + grade_book[i].grade_value
                grades_number = grades_number + 1
        average = float(sum_of_grades / grades_number)
        return average

    def student_average_at_all_disciplines(self, student_id, number_of_disciplines):
        """
        This function computes the overall average grade of a student
        :param student_id: the id of the student
        :param number_of_disciplines: the number of disciplines
        :return: the overall average grade of that student
        """
        checked_disciplines = []
        sum_of_grades = 0
        grade_book = self._grade_book_repository.get_grade_book()
        for i in range(len(grade_book)):
            if grade_book[i].student_id == student_id and grade_book[i].discipline_id not in checked_disciplines:
                checked_disciplines.append(grade_book[i].discipline_id)
                discipline_average = self.student_average_at_a_discipline(student_id, grade_book[i].discipline_id)
                sum_of_grades = sum_of_grades + discipline_average
        average = float(sum_of_grades / number_of_disciplines)
        return average

    def assign_student_average(self, number_of_disciplines):
        """
        This function assigns the overall average grade of all students that have at least one grade
        to the students_with_grades
        :param number_of_disciplines: the number of all disciplines
        """
        checked_students = []
        grade_book = self._grade_book_repository.get_grade_book()
        for i in range(len(grade_book)):
            if grade_book[i].student_id not in checked_students:
                student_id = grade_book[i].student_id
                average = self.student_average_at_all_disciplines(student_id, number_of_disciplines)
                self._grade_book_repository.add_student_average(student_id, average)
                checked_students.append(student_id)

    def assign_discipline_average(self):
        """
        This function assigns the average grade of all disciplines that have at least one grade
        to the disciplines_with_grades list
        """
        checked_disciplines = []
        grade_book = self._grade_book_repository.get_grade_book()
        for i in range(len(grade_book)):
            if grade_book[i].discipline_id not in checked_disciplines:
                discipline_id = grade_book[i].discipline_id
                average = self.discipline_average(discipline_id)
                self._grade_book_repository.add_discipline_average(discipline_id, average)
                checked_disciplines.append(discipline_id)

    def verify_if_student_is_failing(self, student_id):
        """
        This function verifies if a student is failing one or more disciplines, or not failing any
        :param student_id: the id of the student
        :return: True if the student is failing, False if they aren't
        """
        disciplines_with_grades = self._grade_book_repository.get_disciplines_with_grades()
        for i in range(len(disciplines_with_grades)):
            discipline_id = disciplines_with_grades[i]['id']
            if self.student_average_at_a_discipline(student_id, discipline_id) < 5:
                return True
        return False

    def find_failing_students(self):
        """
        This function finds the students with grades that are failing at one or more disciplines
        :return: failing_students: the list were the failing students will end up
        """
        failing_students = []
        students_with_grades = self._grade_book_repository.get_students_with_grades()
        for i in range(len(students_with_grades)):
            student_id = students_with_grades[i]['id']
            if self.verify_if_student_is_failing(student_id) is True:
                failing_students.append(students_with_grades[i])
        return failing_students

    def sort_students_based_on_average_grade(self):
        """
        This function sorts the students with grades based on their overall average grade (descending order)
        """
        students_with_grades = self._grade_book_repository.get_students_with_grades()
        for i in range(len(students_with_grades) - 1):
            for j in range(i, len(students_with_grades)):
                if students_with_grades[i]['average grade'] < students_with_grades[j]['average grade']:
                    students_with_grades[i], students_with_grades[j] = \
                     students_with_grades[j], students_with_grades[i]

    def sort_disciplines_based_on_average_grade(self):
        """
        This function sorts the disciplines with grades based on their average grade (descending order)
        """
        disciplines_with_grades = self._grade_book_repository.get_disciplines_with_grades()
        for i in range(len(disciplines_with_grades) - 1):
            for j in range(i, len(disciplines_with_grades)):
                if disciplines_with_grades[i]['average grade'] < disciplines_with_grades[j]['average grade']:
                    disciplines_with_grades[i], disciplines_with_grades[j] = \
                     disciplines_with_grades[j], disciplines_with_grades[i]

    def find_students_without_grades(self, student_list):
        students_with_grades = self.get_students_with_grades()
        students_without_grades = []
        for i in range(len(student_list)):
            has_grades = False
            for j in range(len(students_with_grades)):
                if student_list[i].student_id == students_with_grades[j]["id"]:
                    has_grades = True
            if has_grades is False:
                students_without_grades.append({'id': student_list[i].student_id, 'average grade': 0.0})
        return students_without_grades

    def get_students_with_grades(self):
        return self._grade_book_repository.get_students_with_grades()

    def get_disciplines_with_grades(self):
        return self._grade_book_repository.get_disciplines_with_grades()

    def get_grade_book(self):
        return self._grade_book_repository.get_grade_book()
