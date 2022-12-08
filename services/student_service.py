from src.repository.repository import StudentRepository
from src.services.exceptions import IdNotUnique, StudentNotInList


class StudentService:
    def __init__(self, student_repository: StudentRepository):
        self._student_repository = student_repository

    def verify_student_id_uniqueness(self, student_id):
        """
        This function verifies if the given student id is unique or not
        :param student_id: the student id to be verified
        :return: True if the id is unique, False if it isn't
        """
        student_list = self._student_repository.get_student_list()
        for i in range(len(student_list)):
            if student_list[i].student_id == student_id:
                return False
        return True

    def find_student_by_id(self, student_id):
        """
        This function finds the position of the student_id in the student_list
        :param student_id: the id of the student that needs to be found
        :return: the position of the student in the student_list
        """
        student_list = self._student_repository.get_student_list()
        for i in range(len(student_list)):
            if student_list[i].student_id == student_id:
                return i
        raise StudentNotInList

    def add_student(self, student_id, student_name):
        """
        This function adds a new student to the student list
        :param student_id: the id of the new student
        :param student_name: the name of the new student
        """
        if self.verify_student_id_uniqueness(student_id) is True:
            self._student_repository.add(student_id, student_name)
        else:
            raise IdNotUnique

    def remove_student(self, student_id):
        """
        This function removes a student from the student list
        :param student_id: the id of the student that needs to be removed
        """
        student_position_in_list = self.find_student_by_id(student_id)
        self._student_repository.remove(student_position_in_list)

    def update_student_information(self, student_id, new_student_name):
        """
        This function updates a student's information
        :param student_id: the id of the student
        :param new_student_name: the new name of the student
        """
        student_position_in_list = self.find_student_by_id(student_id)
        self._student_repository.update(student_position_in_list, new_student_name)

    def search_by_name(self, student_name):
        """
        This function finds every partial name match in the student list
        :param student_name: the name of the searched student
        :return: searched_students: the list were the search results will end up
        """
        searched_students = []
        student_list = self._student_repository.get_student_list()
        for i in range(len(student_list)):
            if student_name.casefold() in student_list[i].name.casefold():
                searched_students.append(student_list[i])
        return searched_students

    def search_by_id(self, student_id):
        """
        This function finds every partial id match in the student list
        :param student_id: the id of the searched student
        :return: searched_students: the list were the search results will end up
        """
        searched_students = []
        student_list = self._student_repository.get_student_list()
        for i in range(len(student_list)):
            if student_id in str(student_list[i].student_id):
                searched_students.append(student_list[i])
        return searched_students

    def get_student_list(self):
        return self._student_repository.get_student_list()
