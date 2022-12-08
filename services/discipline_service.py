from src.repository.repository import DisciplineRepository
from src.services.exceptions import IdNotUnique, DisciplineNotInList


class DisciplineService:
    def __init__(self, discipline_repository: DisciplineRepository):
        self._discipline_repository = discipline_repository

    def verify_discipline_id_uniqueness(self, discipline_id):
        """
        This function verifies if the given discipline id is unique or not
        :param discipline_id: the id of the discipline
        :return: True if the id is unique, False if it isn't
        """
        discipline_list = self._discipline_repository.get_discipline_list()
        for i in range(len(discipline_list)):
            if discipline_list[i].discipline_id == discipline_id:
                return False
        return True

    def find_discipline_by_id(self, discipline_id):
        """
        This function finds the position of the given discipline in the discipline list
        :param discipline_id: the id of the discipline
        :return: the position of the discipline in the discipline list
        """
        discipline_list = self._discipline_repository.get_discipline_list()
        for i in range(len(discipline_list)):
            if discipline_list[i].discipline_id == discipline_id:
                return i
        raise DisciplineNotInList

    def add_discipline(self, discipline_id, discipline_name):
        """
        This function adds a new discipline to the discipline list
        :param discipline_id: the id of the new discipline
        :param discipline_name: the name of the new discipline
        """
        if self.verify_discipline_id_uniqueness(discipline_id) is True:
            self._discipline_repository.add(discipline_id, discipline_name)
        else:
            raise IdNotUnique

    def remove_discipline(self, discipline_id):
        """
        This function removes a given discipline from the discipline list
        :param discipline_id: the id of the discipline that's gonna be removed
        """
        discipline_position_in_list = self.find_discipline_by_id(discipline_id)
        self._discipline_repository.remove(discipline_position_in_list)

    def update_discipline_information(self, discipline_id, new_discipline_name):
        """
        This function updates a discipline's information
        :param discipline_id: the id of the discipline
        :param new_discipline_name: the new name of the discipline
        """
        discipline_position_in_list = self.find_discipline_by_id(discipline_id)
        self._discipline_repository.update(discipline_position_in_list, new_discipline_name)

    def search_by_name(self, discipline_name):
        """
        This function finds every partial name match in the discipline list
        :param discipline_name: the name of the searched discipline
        :return: searched_disciplines: the list were the search results will end up
        """
        searched_disciplines = []
        discipline_list = self._discipline_repository.get_discipline_list()
        for i in range(len(discipline_list)):
            if discipline_name.casefold() in discipline_list[i].name.casefold():
                searched_disciplines.append(discipline_list[i])
        return searched_disciplines

    def search_by_id(self, discipline_id):
        """
        This function finds every partial id match in the discipline list
        :param discipline_id: the id of the searched discipline
        :return: searched_disciplines: the list were the search results will end up
        """
        searched_disciplines = []
        discipline_list = self._discipline_repository.get_discipline_list()
        for i in range(len(discipline_list)):
            if discipline_id in str(discipline_list[i].discipline_id):
                searched_disciplines.append(discipline_list[i])
        return searched_disciplines

    def get_discipline_list(self):
        return self._discipline_repository.get_discipline_list()

    def get_number_of_disciplines(self):
        discipline_list = self.get_discipline_list()
        return len(discipline_list)
