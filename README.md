# FPfinalProject
## Students Register Management 
*<sub>(menu-driven console-based user interface, layered architecture with classes)</sub>*
* A faculty stores information about: <br />
  - Student: student_id, name <br />
  - Discipline: discipline_id, name <br />
  - Grade: discipline_id, student_id, grade_value <br />

* The application can:

1. Manage students and disciplines. The user can add, remove, update, and list both students and disciplines.
2. Grade students at a given discipline. Any student may receive one or several grades at any discipline. Deleting a student also removes their grades. Deleting a discipline deletes all grades at that discipline for all students.
3. Search for disciplines/students based on ID or name/title. The search must work using case-insensitive, partial string matching, and must return all matching disciplines/students.
4. Create statistics:
   - All students failing at one or more disciplines (students having an average <5 for a discipline are failing it)
   - Students with the best school situation, sorted in descending order of their aggregated average (the average between their average grades per discipline)
   - All disciplines at which there is at least one grade, sorted in descending order of the average grade(s) received by all students
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying)
6. Persistent storage for all entities using file-based repositories in addition to the in-memory repository
7. Settings.properties file to configure your application. (switch between text/binary files storage)
