import unittest
from src.repository.repository import DisciplineRepository


class DisciplineRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._discipline_repository = DisciplineRepository()

    def test_add__empty_list__one_element_list(self):
        self._discipline_repository.add(1, "math")
        discipline_list = self._discipline_repository.get_discipline_list()
        self.assertEqual(len(discipline_list), 1)

    def test_remove__one_element_list__empty_list(self):
        self._discipline_repository.add(1, "math")
        discipline_position_in_list = 0
        self._discipline_repository.remove(discipline_position_in_list)
        discipline_list = self._discipline_repository.get_discipline_list()
        self.assertEqual(len(discipline_list), 0)

    def test_update__initial_list__updated_values(self):
        self._discipline_repository.add(1, "math")
        discipline_position_list = 0
        new_discipline_name = "english"
        self._discipline_repository.update(discipline_position_list, new_discipline_name)
        discipline_list = self._discipline_repository.get_discipline_list()
        self.assertEqual(discipline_list[0].name, new_discipline_name)
