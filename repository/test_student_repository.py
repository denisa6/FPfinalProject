import unittest
from src.repository.repository import StudentRepository


class StudentRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_repository = StudentRepository()

    def test_add__empty_list__one_element_list(self):
        self._student_repository.add(100, "Anna")
        student_list = self._student_repository.get_student_list()
        self.assertEqual(len(student_list), 1)

    def test_remove__one_element_list__empty_list(self):
        self._student_repository.add(100, "Anna")
        student_position_in_list = 0
        student_list = self._student_repository.get_student_list()
        self._student_repository.remove(student_position_in_list)
        self.assertEqual(len(student_list), 0)

    def test_update__initial_list__updated_values(self):
        self._student_repository.add(100, "Anna")
        student_position_in_list = 0
        new_student_name = "Marie"
        student_list = self._student_repository.get_student_list()
        self._student_repository.update(student_position_in_list, new_student_name)
        self.assertEqual(student_list[0].name, new_student_name)
