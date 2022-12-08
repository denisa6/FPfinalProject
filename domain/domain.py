class Student:
    def __init__(self, id_of_student, name_of_student):
        self._student_id = id_of_student
        self._name = name_of_student

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name


class Discipline:
    def __init__(self, id_of_discipline, discipline_name):
        self._discipline_id = id_of_discipline
        self._name = discipline_name

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def name(self):
        return self._name


class Grade:
    def __init__(self, discipline_id, student_id, grade_value):
        self._discipline_id = discipline_id
        self._student_id = student_id
        self._grade_value = grade_value

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def student_id(self):
        return self._student_id

    @property
    def grade_value(self):
        return self._grade_value
