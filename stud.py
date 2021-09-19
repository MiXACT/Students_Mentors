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

	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.hw_avrg()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'

	def __lt__(self, other):
		if self.hw_avrg() < other.hw_avrg():
			return f'{other.name} {other.surname} имеет больший средний бал.'
		else:
			return f'{self.name} {self.surname} имеет больший средний бал.'

	def hw_avrg(self):
		average = 0
		n = 0
		for val in self.grades.values():
			for i in range(len(val)):
				average += int(val[i])
				n += 1
		return round(average/n, 1)

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

	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}'

	def __lt__(self, other):
		if self.average() < other.average():
			return f'{other.name} {other.surname} - лучший лектор.'
		else:
			return f'{self.name} {self.surname} - лучший лектор.'

	def average(self):
		average = 0
		n = 0
		for val in self.lect_grades.values():
			for i in range(len(val)):
				average += int(val[i])
				n += 1
		return round(average/n, 1)


class Reviewer(Mentor):
	def rate_hw(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'

	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname}'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Scotch try outs', 'Math']
best_student_2 = Student('Rick', 'Mortynov', 'male')
best_student_2.courses_in_progress += ['Math']
best_student_2.add_courses('Python')
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python','Math']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)

cool_mentor.rate_hw(best_student_2, 'Math', 3)
cool_mentor.rate_hw(best_student_2, 'Math', 7)
cool_mentor.rate_hw(best_student_2, 'Python', 9)
cool_mentor.rate_hw(best_student_2, 'Python', 6)
 
print(best_student.grades)

best_lecturer_1 = Lecturer('John', 'Walker')
best_lecturer_1.courses_attached += ['Scotch try outs']
best_lecturer_2 = Lecturer('Masha', 'Ivanova')
best_lecturer_2.courses_attached += ['Math']

best_student.rate_lect(best_lecturer_1, 'Scotch try outs', 5)
best_student.rate_lect(best_lecturer_2, 'Math', 8)
best_student_2.rate_lect(best_lecturer_1, 'Scotch try outs', 10)
best_student_2.rate_lect(best_lecturer_2, 'Math', 9)

print(f'{best_lecturer_1.lect_grades}\n{best_lecturer_2.lect_grades}')

#задача №3: перегрузка метода __str__ для "проверяющих" (Reviewer)
print(cool_mentor)

#задача №3: перегрузка метода __str__ для лекторов (Lecturer)
print(best_lecturer_1)
print(best_lecturer_2)

#задача №3: перегрузка метода __str__ для студентов (Student)
print(f'{best_student}\n{best_student_2}')

#задача №3: сравнение оценок лекторов
print(best_lecturer_1 < best_lecturer_2)

#задача №3: сравнение оценок за ДЗ студентов
print(best_student < best_student_2)