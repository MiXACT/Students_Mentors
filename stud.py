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
		'''Подсчёт средней оценки за ДЗ'''
		average = 0
		n = 0
		for val in self.grades.values():
			for i in range(len(val)):
				average += int(val[i])
				n += 1
		return round(average/n, 1)

	def hw_course_avrg(self, students, course):
		'''Подсчёт средней оценки всех ДЗ по указанному курсу'''
		average = 0
		n = 0
		for i in students:
			if course in i.grades:
				for j in i.grades[course]:
					average += j
					n += 1
		if n > 0:
			return f'Средний бал за ДЗ по {course}: {round(average/n, 1)}'
		else:
			return 'ДЗ не проверено или указанного курса нет в программе.'

	def rate_lect(self, lecturer, course, grade):
		'''Оценивание лектора за курс'''
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
		'''Подсчёт средней оценки лектора'''
		average = 0
		n = 0
		for val in self.lect_grades.values():
			for i in range(len(val)):
				average += int(val[i])
				n += 1
		return round(average/n, 1)

	def course_avrg(self, lecturers, course):
		'''Подсчёт средней оценки всех лекторов за указанный курс'''
		average = 0
		n = 0
		for i in lecturers:
			if course in i.lect_grades:
				for j in i.lect_grades[course]:
					average += j
					n += 1
		if n > 0:
			return f'Средняя оценка лекторов курса {course}: {round(average/n, 1)}'
		else:
			return 'Работа лекторов не оценивалась или указанного курса нет в программе.'


class Reviewer(Mentor):
	def rate_hw(self, student, course, grade):
		'''Оценивание ДЗ указанного студента по указанному курсу'''
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'

	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname}'
 
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Scotch try outs', 'Math']
student_2 = Student('Rick', 'Mortynov', 'male')
student_2.courses_in_progress += ['Math']
student_2.add_courses('Python')
 
mentor_1 = Reviewer('Some', 'Buddy')
mentor_1.courses_attached += ['Python','Math']
mentor_2 = Reviewer('Boris', 'Britva')
mentor_2.courses_attached += ['Scotch try outs', 'Math']
 
mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_1, 'Python', 8)

mentor_1.rate_hw(student_2, 'Math', 3)
mentor_1.rate_hw(student_2, 'Math', 7)
mentor_1.rate_hw(student_2, 'Python', 9)
mentor_1.rate_hw(student_2, 'Python', 6)

mentor_2.rate_hw(student_1, 'Scotch try outs', 9)
mentor_2.rate_hw(student_1, 'Math', 7)
mentor_2.rate_hw(student_1, 'Math', 10)
 
print(student_1.grades)

lecturer_1 = Lecturer('John', 'Walker')
lecturer_1.courses_attached += ['Scotch try outs', 'Math']
lecturer_2 = Lecturer('Masha', 'Ivanova')
lecturer_2.courses_attached += ['Math']

student_1.rate_lect(lecturer_1, 'Scotch try outs', 5)
student_1.rate_lect(lecturer_1, 'Scotch try outs', 10)
student_1.rate_lect(lecturer_2, 'Math', 8)
student_2.rate_lect(lecturer_2, 'Math', 9)
student_2.rate_lect(lecturer_1, 'Math', 4)

print(f'{lecturer_1.lect_grades}\n{lecturer_2.lect_grades}')

#задача №3: перегрузка метода __str__ для "проверяющих" (Reviewer)
print(mentor_1)

#задача №3: перегрузка метода __str__ для лекторов (Lecturer)
print(lecturer_1)
print(lecturer_2)

#задача №3: перегрузка метода __str__ для студентов (Student)
print(f'{student_1}\n{student_2}')

#задача №3: сравнение оценок лекторов
print(lecturer_1 < lecturer_2)

#задача №3: сравнение оценок за ДЗ студентов
print(student_1 < student_2)

#задача №4: средняя оценка студентов за курс
print(student_1.hw_course_avrg([student_1, student_2], 'Python'))

#задача №4: средняя оценка лекторов за курс
print(lecturer_1.course_avrg([lecturer_1, lecturer_2], 'Math'))