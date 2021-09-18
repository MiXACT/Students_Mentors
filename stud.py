class Student:
	def __init__(self, name, surname, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}

	def add_courses(self, course_name):
		self.finished_courses.append(course_name)

	def rate_lect(self, lecturer, course, grade):
		if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
			if course in lecturer.lect_grades:
				lecturer.lect_grades[course] += [grade]
			else:
				lecturer.lect_grades[course] = [grade]
		else:
			return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.courses_attached = []
		self.lect_grades = {}


class Reviewer(Mentor):
	def rate_hw(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Scotch try outs', 'Math']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)

best_lecturer_1 = Lecturer('John', 'Walker')
best_lecturer_1.courses_attached += ['Scotch try outs']
best_lecturer_2 = Lecturer('Masha', 'Ivanova')
best_lecturer_2.courses_attached += ['Math']

best_student.rate_lect(best_lecturer_1, 'Scotch try outs', 5)
best_student.rate_lect(best_lecturer_2, 'Math', 8)

print(f'{best_lecturer_1.lect_grades}\n{best_lecturer_2.lect_grades}')