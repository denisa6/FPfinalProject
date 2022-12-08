import unittest
from src.services.student_service import StudentService
from src.repository.repository import StudentRepository


class StudentServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._student_service = StudentService(StudentRepository())

    def test_verify_student_id_uniqueness__unique_id__True(self):
        self.assertTrue(self._student_service.verify_student_id_uniqueness(100))

    def test_verify_student_id_uniqueness__not_unique_id__False(self):
        self._student_service.add_student(100, "Anna")
        self.assertFalse(self._student_service.verify_student_id_uniqueness(100))

    def test_find_student_by_id__first_student__0(self):
        self._student_service.add_student(100, "Anna")
        correct_result = 0
        self.assertEqual(self._student_service.find_student_by_id(100), correct_result)

    def test_add_student__empty_list__one_element_list(self):
        self._student_service.add_student(100, "Anna")
        student_list = self._student_service.get_student_list()
        self.assertEqual(len(student_list), 1)

    def test_remove_student__one_element_list__empty_list(self):
        self._student_service.add_student(100, "Anna")
        self._student_service.remove_student(100)
        student_list = self._student_service.get_student_list()
        self.assertEqual(len(student_list), 0)

    def test_update_student_information__initial_information__updates_information(self):
        self._student_service.add_student(100, "Anna")
        new_student_name = "Marie"
        self._student_service.update_student_information(100, new_student_name)
        student_list = self._student_service.get_student_list()
        self.assertEqual(student_list[0].name, new_student_name)

    def test_search_by_name__incorrect_name__empty_list(self):
        self._student_service.add_student(100, "Anna")
        searched_name = "Marie"
        search_results = self._student_service.search_by_name(searched_name)
        self.assertEqual(len(search_results), 0)

    def test_search_by_name__partially_correct_name__one_element_list(self):
        self._student_service.add_student(100, "Anna")
        searched_name = "Ann"
        search_results = self._student_service.search_by_name(searched_name)
        self.assertEqual(len(search_results), 1)

    def test_search_by_id__incorrect_id__empty_list(self):
        self._student_service.add_student(100, "Anna")
        searched_id = "200"
        search_results = self._student_service.search_by_id(searched_id)
        self.assertEqual(len(search_results), 0)

    def test_search_by_id__partially_correct_id__one_element_list(self):
        self._student_service.add_student(100, "Anna")
        searched_id = "10"
        search_results = self._student_service.search_by_id(searched_id)
        self.assertEqual(len(search_results), 1)
