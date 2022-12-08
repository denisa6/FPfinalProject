from src.services.student_service import StudentService
from src.services.discipline_service import DisciplineService
from src.services.grade_book_service import GradeBookService
from src.services.undo_handlers import UndoHandler
from src.services.redo_handlers import RedoHandler
from src.services.undo import UndoManager
from src.services.redo import RedoManager


class Ui:
    def __init__(self, student_service: StudentService, discipline_service: DisciplineService,
                 grade_book_service: GradeBookService):
        self._student_service = student_service
        self._discipline_service = discipline_service
        self._grade_book_service = grade_book_service

    @staticmethod
    def print_menu():
        print("1. Add new student\n"
              "2. Add new discipline\n"
              "3. Add new grade\n"
              "4. List all students\n"
              "5. List all disciplines\n"
              "6. Remove a student\n"
              "7. Remove a discipline\n"
              "8. Update a student's information\n"
              "9. Update a discipline's information\n"
              "10. Look for a student by name\n"
              "11. Look for discipline by name\n"
              "12. Look for students by id\n"
              "13. Look for disciplines by id\n"
              "14. All students failing at one or more disciplines\n"
              "15. Students, sorted in descending order of their aggregated average\n"
              "16. Disciplines, sorted in descending order of the average grade(s) received by all students\n"
              "17. Undo\n"
              "18. Redo\n"
              "19. Exit\n")

    def add_menu(self, option):
        if option == 1:
            student_id = int(input("Give student id\n>"))
            student_name = input("Give student name\n>")
            self._student_service.add_student(student_id, student_name)
            UndoManager.register_operation(self._student_service, UndoHandler.ADD_STUDENT, student_id, student_name)
        elif option == 2:
            discipline_id = int(input("Give discipline id\n>"))
            discipline_name = input("Give discipline name\n>")
            self._discipline_service.add_discipline(discipline_id, discipline_name)
            UndoManager.register_operation(self._discipline_service, UndoHandler.ADD_DISCIPLINE, discipline_id,
                                           discipline_name)
        elif option == 3:
            discipline_id = int(input("Enter discipline id\n>"))
            student_id = int(input("Enter student id\n>"))
            grade_value = int(input("Enter grade\n>"))
            self._grade_book_service.add_grade(discipline_id, student_id, grade_value)
            UndoManager.register_operation(self._grade_book_service, UndoHandler.ADD_GRADE, discipline_id, student_id,
                                           grade_value)

    def list_menu(self, option):
        if option == 4:
            student_list = self._student_service.get_student_list()
            for i in range(len(student_list)):
                print("id: " + str(student_list[i].student_id) + " name: " + student_list[i].name)
        elif option == 5:
            discipline_list = self._discipline_service.get_discipline_list()
            for i in range(len(discipline_list)):
                print("id: " + str(discipline_list[i].discipline_id) + " name: " + discipline_list[i].name)

    def remove_menu(self, option):
        if option == 6:
            student_id = int(input("Give student id\n>"))
            student = self._student_service.search_by_id(str(student_id))
            student_name = student[0].name
            self._student_service.remove_student(student_id)
            self._grade_book_service.remove_student_grades(student_id)
            UndoManager.register_operation(self._student_service, UndoHandler.REMOVE_STUDENT, student_id, student_name)
        elif option == 7:
            discipline_id = int(input("Give discipline id\n>"))
            discipline = self._discipline_service.search_by_id(str(discipline_id))
            discipline_name = discipline[0].name
            self._discipline_service.remove_discipline(discipline_id)
            self._grade_book_service.remove_discipline_grades(discipline_id)
            UndoManager.register_operation(self._discipline_service, UndoHandler.REMOVE_DISCIPLINE, discipline_id,
                                           discipline_name)

    def update_menu(self, option):
        if option == 8:
            student_id = int(input("Give student id\n>"))
            new_student_name = input("Give new student name\n>")
            student = self._student_service.search_by_id(str(student_id))
            old_student_name = student[0].name
            self._student_service.update_student_information(student_id, new_student_name)
            UndoManager.register_operation(self._student_service, UndoHandler.UPDATE_STUDENT_INFORMATION, student_id,
                                           old_student_name, new_student_name)
        elif option == 9:
            discipline_id = int(input("Give discipline id\n>"))
            new_discipline_name = input("Give discipline name\n>")
            discipline = self._discipline_service.search_by_id(str(discipline_id))
            old_discipline_name = discipline[0].name
            self._discipline_service.update_discipline_information(discipline_id, new_discipline_name)
            UndoManager.register_operation(self._discipline_service, UndoHandler.UPDATE_DISCIPLINE_INFORMATION,
                                           discipline_id, old_discipline_name, new_discipline_name)

    def search_menu(self, option):
        if option == 10:
            student_name = input("Give student name\n>")
            searched_students = self._student_service.search_by_name(student_name)
            for i in range(len(searched_students)):
                print("id: " + str(searched_students[i].student_id) + " name: " + searched_students[i].name)
        elif option == 11:
            discipline_name = input("Give discipline name\n>")
            searched_disciplines = self._discipline_service.search_by_name(discipline_name)
            for i in range(len(searched_disciplines)):
                print("id: " + str(searched_disciplines[i].discipline_id) + " name: " + searched_disciplines[i].name)
        elif option == 12:
            student_id = input("Give student id\n>")
            searched_students = self._student_service.search_by_id(student_id)
            for i in range(len(searched_students)):
                print("id: " + str(searched_students[i].student_id) + " name: " + searched_students[i].name)
        elif option == 13:
            discipline_id = input("Give discipline id\n>")
            searched_disciplines = self._discipline_service.search_by_id(discipline_id)
            for i in range(len(searched_disciplines)):
                print("id: " + str(searched_disciplines[i].discipline_id) + " name: " + searched_disciplines[i].name)

    def statistics_menu(self, option):
        number_of_disciplines = self._discipline_service.get_number_of_disciplines()
        self._grade_book_service.assign_student_average(number_of_disciplines)
        self._grade_book_service.assign_discipline_average()
        if option == 14:
            failing_students = self._grade_book_service.find_failing_students()
            for i in range(len(failing_students)):
                print(failing_students[i])
            # students without grades
            student_list = self._student_service.get_student_list()
            students_without_grades = self._grade_book_service.find_students_without_grades(student_list)
            for i in range(len(students_without_grades)):
                print(students_without_grades[i])
        elif option == 15:
            self._grade_book_service.sort_students_based_on_average_grade()
            students_with_grades = self._grade_book_service.get_students_with_grades()
            for i in range(len(students_with_grades)):
                print(students_with_grades[i])
            # for students that don't have any grades
            student_list = self._student_service.get_student_list()
            students_without_grades = self._grade_book_service.find_students_without_grades(student_list)
            for i in range(len(students_without_grades)):
                print(students_without_grades[i])
        elif option == 16:
            self._grade_book_service.sort_disciplines_based_on_average_grade()
            disciplines_with_grades = self._grade_book_service.get_disciplines_with_grades()
            for i in range(len(disciplines_with_grades)):
                print(disciplines_with_grades[i])

    def undo_menu(self, redo_handler):
        if redo_handler is RedoHandler.ADD_STUDENT:
            student_id = RedoManager.get_first_argument()
            student_name = RedoManager.get_second_argument()
            UndoManager.register_operation(self._student_service, UndoHandler.ADD_STUDENT, student_id, student_name)
        elif redo_handler is RedoHandler.ADD_DISCIPLINE:
            discipline_id = RedoManager.get_first_argument()
            discipline_name = RedoManager.get_second_argument()
            UndoManager.register_operation(self._discipline_service, UndoHandler.ADD_DISCIPLINE, discipline_id,
                                           discipline_name)
        elif redo_handler is RedoHandler.ADD_GRADE:
            discipline_id = RedoManager.get_first_argument()
            student_id = RedoManager.get_second_argument()
            grade_value = RedoManager.get_third_argument()
            UndoManager.register_operation(self._grade_book_service, UndoHandler.ADD_GRADE, discipline_id, student_id,
                                           grade_value)
        elif redo_handler is RedoHandler.REMOVE_STUDENT:
            student_id = RedoManager.get_first_argument()
            student_name = RedoManager.get_second_argument()
            UndoManager.register_operation(self._student_service, UndoHandler.REMOVE_STUDENT, student_id, student_name)
        elif redo_handler is RedoHandler.REMOVE_DISCIPLINE:
            discipline_id = RedoManager.get_first_argument()
            discipline_name = RedoManager.get_second_argument()
            UndoManager.register_operation(self._discipline_service, UndoHandler.REMOVE_DISCIPLINE, discipline_id,
                                           discipline_name)
        elif redo_handler is RedoHandler.UPDATE_DISCIPLINE_INFORMATION:
            student_id = RedoManager.get_first_argument()
            old_student_name = RedoManager.get_second_argument()
            new_student_name = RedoManager.get_third_argument()
            UndoManager.register_operation(self._student_service, UndoHandler.UPDATE_STUDENT_INFORMATION, student_id,
                                           old_student_name, new_student_name)
        elif redo_handler is RedoHandler.UPDATE_DISCIPLINE_INFORMATION:
            discipline_id = RedoManager.get_first_argument()
            old_discipline_name = RedoManager.get_second_argument()
            new_discipline_name = RedoManager.get_third_argument()
            UndoManager.register_operation(self._discipline_service, UndoHandler.UPDATE_DISCIPLINE_INFORMATION,
                                           discipline_id, old_discipline_name, new_discipline_name)

    def redo_menu(self, undo_handler):
        if undo_handler is UndoHandler.ADD_STUDENT:
            student_id = UndoManager.get_first_argument()
            student_name = UndoManager.get_second_argument()
            RedoManager.register_operation(self._student_service, RedoHandler.ADD_STUDENT, student_id, student_name)
        elif undo_handler is UndoHandler.ADD_DISCIPLINE:
            discipline_id = UndoManager.get_first_argument()
            discipline_name = UndoManager.get_second_argument()
            RedoManager.register_operation(self._discipline_service, RedoHandler.ADD_DISCIPLINE, discipline_id,
                                           discipline_name)
        elif undo_handler is UndoHandler.ADD_GRADE:
            discipline_id = UndoManager.get_first_argument()
            student_id = UndoManager.get_second_argument()
            grade_value = UndoManager.get_third_argument()
            RedoManager.register_operation(self._grade_book_service, RedoHandler.ADD_GRADE, discipline_id, student_id,
                                           grade_value)
        elif undo_handler is UndoHandler.REMOVE_STUDENT:
            student_id = UndoManager.get_first_argument()
            student_name = UndoManager.get_second_argument()
            RedoManager.register_operation(self._student_service, RedoHandler.REMOVE_STUDENT, student_id, student_name)
        elif undo_handler is UndoHandler.REMOVE_DISCIPLINE:
            discipline_id = UndoManager.get_first_argument()
            discipline_name = UndoManager.get_second_argument()
            RedoManager.register_operation(self._discipline_service, RedoHandler.REMOVE_DISCIPLINE, discipline_id,
                                           discipline_name)
        elif undo_handler is UndoHandler.UPDATE_STUDENT_INFORMATION:
            student_id = UndoManager.get_first_argument()
            old_student_name = UndoManager.get_second_argument()
            new_student_name = UndoManager.get_third_argument()
            RedoManager.register_operation(self._student_service, RedoHandler.UPDATE_STUDENT_INFORMATION, student_id,
                                           new_student_name, old_student_name)
        elif undo_handler is UndoHandler.UPDATE_DISCIPLINE_INFORMATION:
            discipline_id = UndoManager.get_first_argument()
            old_discipline_name = UndoManager.get_second_argument()
            new_discipline_name = UndoManager.get_third_argument()
            RedoManager.register_operation(self._discipline_service, RedoHandler.UPDATE_DISCIPLINE_INFORMATION,
                                           discipline_id, new_discipline_name, old_discipline_name)

    def option_menu(self):
        self.print_menu()
        while True:
            option = int(input("Enter option\n>"))
            if option in [1, 2, 3]:
                self.add_menu(option)
            elif option in [4, 5]:
                self.list_menu(option)
            elif option in [6, 7]:
                self.remove_menu(option)
            elif option in [8, 9]:
                self.update_menu(option)
            elif option in [10, 11, 12, 13]:
                self.search_menu(option)
            elif option in [14, 15, 16]:
                self.statistics_menu(option)
            elif option == 17:
                undo_handler = UndoManager.get_handler()
                self.redo_menu(undo_handler)
                UndoManager.undo()
            elif option == 18:
                redo_handler = RedoManager.get_handler()
                self.undo_menu(redo_handler)
                RedoManager.redo()
            elif option == 19:
                break
            print("")
