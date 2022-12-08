class IdNotUnique(Exception):
    def __init__(self):
        message = "This id is already used"
        super().__init__(message)


class StudentNotInList(Exception):
    def __init__(self):
        message = "This student is not registered in the student list"
        super().__init__(message)


class DisciplineNotInList(Exception):
    def __init__(self):
        message = "This discipline is not registered in the discipline list"
        super(DisciplineNotInList, self).__init__(message)


class InvalidGrade(Exception):
    def __init__(self):
        message = "The grade introduced isn't valid"
        super(InvalidGrade, self).__init__(message)
