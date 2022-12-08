import unittest
from src.repository.repository import GradeBookRepository


class GradeBookRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._grade_book_repository = GradeBookRepository()

    def test_add__empty_list__one_element_list(self):
        self._grade_book_repository.add(1, 100, 8)
        grade_book = self._grade_book_repository.get_grade_book()
        self.assertEqual(len(grade_book), 1)

    def test_remove_student_grades__one_element_list__empty_list(self):
        self._grade_book_repository.add(1, 100, 8)
        self._grade_book_repository.remove_student_grades(100)
        grade_book = self._grade_book_repository.get_grade_book()
        self.assertEqual(len(grade_book), 0)

    def test_remove_discipline_grades__one_element_list__empty_list(self):
        self._grade_book_repository.add(1, 100, 8)
        self._grade_book_repository.remove_discipline_grades(1)
        grade_book = self._grade_book_repository.get_grade_book()
        self.assertEqual(len(grade_book), 0)

    def test_remove_a_grade__one_element_list__empty_list(self):
        self._grade_book_repository.add(1, 100, 8)
        self._grade_book_repository.remove_a_grade(1, 100, 8)
        grade_book = self._grade_book_repository.get_grade_book()
        self.assertEqual(len(grade_book), 0)

    def test_add_student_average__empty_list__one_element_list(self):
        self._grade_book_repository.add_student_average(100, 8.5)
        students_with_grades = self._grade_book_repository.get_students_with_grades()
        self.assertEqual(len(students_with_grades), 1)

    def test_add_discipline_average__empty_list__one_element_list(self):
        self._grade_book_repository.add_discipline_average(1, 7.5)
        disciplines_with_grades = self._grade_book_repository.get_disciplines_with_grades()
        self.assertEqual(len(disciplines_with_grades), 1)
