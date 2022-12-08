from enum import Enum


def add_student_handler(student_service, student_id, student_name):
    student_service.remove_student(student_id)


def add_discipline_handler(discipline_service, discipline_id, discipline_name):
    discipline_service.remove_discipline(discipline_id)


def add_grade_handler(grade_book, discipline_id, student_id, grade_value):
    grade_book.remove_grade(discipline_id, student_id, grade_value)


def remove_student_handler(student_service, student_id, student_name):
    student_service.add_student(student_id, student_name)


def remove_discipline_handler(discipline_service, discipline_id, discipline_name):
    discipline_service.add_discipline(discipline_id, discipline_name)


def update_student_information_handler(student_service, student_id, old_student_name, new_student_name):
    student_service.update_student_information(student_id,old_student_name)


def update_discipline_information_handler(discipline_service, discipline_id, old_discipline_name, new_discipline_name):
    discipline_service.update_discipline_information(discipline_id, old_discipline_name)


class UndoHandler(Enum):
    ADD_STUDENT = add_student_handler
    ADD_DISCIPLINE = add_discipline_handler
    ADD_GRADE = add_grade_handler
    REMOVE_STUDENT = remove_student_handler
    REMOVE_DISCIPLINE = remove_discipline_handler
    UPDATE_STUDENT_INFORMATION = update_student_information_handler
    UPDATE_DISCIPLINE_INFORMATION = update_discipline_information_handler
