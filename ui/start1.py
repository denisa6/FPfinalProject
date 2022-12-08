from src.repository.repository import GradeBookRepository
from src.services.grade_book_service import GradeBookService
from src.services.student_service import StudentService
from src.services.discipline_service import DisciplineService
from ui import Ui
from src.repository.text_file_repository import StudentTextFileRepository, DisciplineTextFileRepository, \
     GradeBookTextFileRepository
from src.repository.bin_file_repository import StudentBinFileRepository, DisciplineBinFileRepository, GradeBookBinFileRepository


# student_repository = StudentTextFileRepository()
# discipline_repository = DisciplineTextFileRepository()
# grade_book_repository = GradeBookTextFileRepository()

student_repository = StudentBinFileRepository()
discipline_repository = DisciplineBinFileRepository()
grade_book_repository = GradeBookBinFileRepository()

#student_repository.add(100, "Grace")
#student_repository.add(101, "Ben")
#student_repository.add(102, "Rose")
#student_repository.add(103, "Claire")
#student_repository.add(104, "Jessie")
#student_repository.add(105, "Marty")
"""
discipline_repository.add(1, "math")
discipline_repository.add(2, "english")

grade_book_repository.add(1, 100, 4)
grade_book_repository.add(1, 100, 5)
grade_book_repository.add(1, 101, 6)
grade_book_repository.add(1, 102, 7)
grade_book_repository.add(1, 103, 8)
grade_book_repository.add(1, 104, 9)
grade_book_repository.add(2, 104, 10)
grade_book_repository.add(2, 103, 9)
grade_book_repository.add(2, 102, 8)
grade_book_repository.add(2, 101, 7)
grade_book_repository.add(2, 100, 6)
grade_book_repository.add(2, 100, 5)
"""
student_service = StudentService(student_repository)
discipline_service = DisciplineService(discipline_repository)
grade_book_service = GradeBookService(grade_book_repository)

ui = Ui(student_service, discipline_service, grade_book_service)
ui.option_menu()
