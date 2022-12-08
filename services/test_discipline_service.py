import unittest
from src.services.discipline_service import DisciplineService
from src.repository.repository import DisciplineRepository


class DisciplineServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._discipline_service = DisciplineService(DisciplineRepository())

    def test_verify_discipline_id_uniqueness__unique_id__True(self):
        self.assertTrue(self._discipline_service.verify_discipline_id_uniqueness(1))

    def test_verify_discipline_id_uniqueness__not_unique_id__False(self):
        self._discipline_service.add_discipline(1, "math")
        self.assertFalse(self._discipline_service.verify_discipline_id_uniqueness(1))

    def test_find_discipline_by_id__first_discipline__0(self):
        self._discipline_service.add_discipline(1, "math")
        correct_result = 0
        self.assertEqual(self._discipline_service.find_discipline_by_id(1), correct_result)

    def test_add_discipline__empty_list__one_element_list(self):
        self._discipline_service.add_discipline(1, "math")
        discipline_list = self._discipline_service.get_discipline_list()
        self.assertEqual(len(discipline_list), 1)

    def test_remove_discipline__one_element_list__empty_list(self):
        self._discipline_service.add_discipline(1, "math")
        self._discipline_service.remove_discipline(1)
        discipline_list = self._discipline_service.get_discipline_list()
        self.assertEqual(len(discipline_list), 0)

    def test_update_discipline_information__initial_information__updated_information(self):
        self._discipline_service.add_discipline(1, "math")
        new_discipline_name = "english"
        self._discipline_service.update_discipline_information(1, new_discipline_name)
        discipline_list = self._discipline_service.get_discipline_list()
        self.assertEqual(discipline_list[0].name, new_discipline_name)

    def test_search_by_name__incorrect_name__empty_list(self):
        self._discipline_service.add_discipline(1, "math")
        searched_name = "english"
        search_results = self._discipline_service.search_by_name(searched_name)
        self.assertEqual(len(search_results), 0)

    def test_search_by_name__partially_correct_name__one_element_list(self):
        self._discipline_service.add_discipline(1, "math")
        searched_name = "ma"
        search_results = self._discipline_service.search_by_name(searched_name)
        self.assertEqual(len(search_results), 1)

    def test_search_by_id__incorrect_id__empty_list(self):
        self._discipline_service.add_discipline(12, "math")
        searched_id = "25"
        search_results = self._discipline_service.search_by_id(searched_id)
        self.assertEqual(len(search_results), 0)

    def test_search_by_id__partially_correct_id__one_element_list(self):
        self._discipline_service.add_discipline(12, "math")
        searched_id = "1"
        search_results = self._discipline_service.search_by_id(searched_id)
        self.assertEqual(len(search_results), 1)
