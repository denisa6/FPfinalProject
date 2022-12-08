import unittest
from src.services.grade_book_service import GradeBookService
from src.repository.repository import GradeBookRepository


class GradeBookServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._grade_book_service = GradeBookService(GradeBookRepository())

    def test_verify_grade_validity__valid_grade__True(self):
        self.assertTrue(self._grade_book_service.verify_grade_validity(8))

    def test_verify_grade_validity__invalid_grade__False(self):
        self.assertFalse(self._grade_book_service.verify_grade_validity(15))

    def test_add_grade__empty_list__one_element_list(self):
        self._grade_book_service.add_grade(1, 100, 8)
        grade_book = self._grade_book_service.get_grade_book()
        self.assertEqual(len(grade_book), 1)

    def test_remove_student_grades__one_element_list__empty_list(self):
        self._grade_book_service.add_grade(1, 100, 8)
        self._grade_book_service.remove_student_grades(100)
        grade_book = self._grade_book_service.get_grade_book()
        self.assertEqual(len(grade_book), 0)

    def test_remove_discipline_grades__one_element_list__empty_list(self):
        self._grade_book_service.add_grade(1, 100, 8)
        self._grade_book_service.remove_discipline_grades(1)
        grade_book = self._grade_book_service.get_grade_book()
        self.assertEqual(len(grade_book), 0)

    def test_remove_a_grade__one_element_list__empty_list(self):
        self._grade_book_service.add_grade(1, 100, 8)
        self._grade_book_service.remove_grade(1, 100, 8)
        grade_book = self._grade_book_service.get_grade_book()
        self.assertEqual(len(grade_book), 0)

    def test_student_average_at_a_discipline__two_element_list__correct_average(self):
        self._grade_book_service.add_grade(1, 100, 8)
        self._grade_book_service.add_grade(1, 100, 9)
        correct_average = 8.5
        self.assertEqual(self._grade_book_service.student_average_at_a_discipline(100, 1), correct_average)

    def test_discipline_average__two_element_list__correct_result(self):
        self._grade_book_service.add_grade(1, 100, 8)
        self._grade_book_service.add_grade(1, 100, 9)
        correct_average = 8.5
        self.assertEqual(self._grade_book_service.discipline_average(1), correct_average)

    def test_student_average_at_all_disciplines__two_element_list__correct_average(self):
        self._grade_book_service.add_grade(1, 100, 8)
        self._grade_book_service.add_grade(2, 100, 9)
        correct_average = 8.5
        number_of_disciplines = 2
        self.assertEqual(self._grade_book_service.student_average_at_all_disciplines(100, number_of_disciplines),
                         correct_average)

    def test_assign_student_average__empty_list__correct_average(self):
        self._grade_book_service.add_grade(1, 100, 8)
        self._grade_book_service.add_grade(2, 100, 9)
        number_of_disciplines = 2
        self._grade_book_service.assign_student_average(number_of_disciplines)
        correct_average = 8.5
        students_with_grades = self._grade_book_service.get_students_with_grades()
        self.assertEqual(students_with_grades[0]['average grade'], correct_average)

    def test_assign_discipline_average__empty_list__correct_average(self):
        self._grade_book_service.add_grade(1, 100, 8)
        self._grade_book_service.add_grade(1, 101, 9)
        self._grade_book_service.assign_discipline_average()
        correct_average = 8.5
        disciplines_with_grades = self._grade_book_service.get_disciplines_with_grades()
        self.assertEqual(disciplines_with_grades[0]['average grade'], correct_average)

    def test_verify_if_student_is_failing__failing_student__True(self):
        self._grade_book_service.add_grade(1, 100, 4)
        self._grade_book_service.assign_discipline_average()
        self.assertTrue(self._grade_book_service.verify_if_student_is_failing(100))

    def test_verify_if_student_is_failing__not_failing_student__False(self):
        self._grade_book_service.add_grade(1, 100, 7)
        self._grade_book_service.assign_discipline_average()
        self.assertFalse(self._grade_book_service.verify_if_student_is_failing(100))

    def test_find_failing_students__empty_list__one_element_list(self):
        self._grade_book_service.add_grade(1, 100, 4)
        number_of_disciplines = 1
        self._grade_book_service.assign_discipline_average()
        self._grade_book_service.assign_student_average(number_of_disciplines)
        failing_students = self._grade_book_service.find_failing_students()
        self.assertEqual(len(failing_students), 1)

    def test_sort_students_based_on_average_grade__unsorted_list__sorted_list(self):
        self._grade_book_service.add_grade(1, 100, 4)
        self._grade_book_service.add_grade(2, 100, 6)
        self._grade_book_service.add_grade(1, 101, 5)
        self._grade_book_service.add_grade(2, 101, 7)
        number_of_disciplines = 2
        self._grade_book_service.assign_student_average(number_of_disciplines)
        self._grade_book_service.sort_students_based_on_average_grade()
        correct_sorted_list = [{'id': 101, 'average grade': 6.0}, {'id': 100, 'average grade': 5.0}]
        students_with_grades = self._grade_book_service.get_students_with_grades()
        self.assertEqual(students_with_grades, correct_sorted_list)

    def test_sort_disciplines_based_on_average_grade__unsorted_list__sorted_list(self):
        self._grade_book_service.add_grade(1, 100, 4)
        self._grade_book_service.add_grade(1, 101, 6)
        self._grade_book_service.add_grade(2, 100, 5)
        self._grade_book_service.add_grade(2, 101, 7)
        self._grade_book_service.assign_discipline_average()
        self._grade_book_service.sort_disciplines_based_on_average_grade()
        correct_sorted_list = [{'id': 2, 'average grade': 6.0}, {'id': 1, 'average grade': 5.0}]
        disciplines_with_grades = self._grade_book_service.get_disciplines_with_grades()
        self.assertEqual(disciplines_with_grades, correct_sorted_list)
