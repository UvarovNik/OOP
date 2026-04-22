class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        
        if course not in self.courses_in_progress:
            return 'Ошибка'
        
        if course not in lecturer.courses_attached:
            return 'Ошибка'
        
        if not (0 <= grade <= 10):
            return 'Ошибка'
        
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]
        
        return None
    
    def average_grade(self):
        """Метод для подсчёта средней оценки за домашние задания"""
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses) if self.finished_courses else "Нет"
        
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()
    
    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()
    
    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()
    
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()
    
    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def average_hw_grade_for_course(students_list, course_name):
    if not students_list:
        return 0
    
    all_grades = []
    for student in students_list:
        if isinstance(student, Student) and course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    
    if not all_grades:
        return 0
    
    return sum(all_grades) / len(all_grades)

def average_lecture_grade_for_course(lecturers_list, course_name):
    if not lecturers_list:
        return 0
    
    all_grades = []
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    
    if not all_grades:
        return 0
    
    return sum(all_grades) / len(all_grades)

# Создание экземпляров классов
if __name__ == "__main__":
        
    # Создаём студентов
    student1 = Student('Ruoy', 'Eman', 'M')
    student1.courses_in_progress += ['Python', 'Git']
    student1.finished_courses += ['Введение в программирование']
    
    student2 = Student('Anna', 'Smith', 'F')
    student2.courses_in_progress += ['Python', 'Java']
    student2.finished_courses += ['Основы алгоритмов']
    
    # Создаём лекторов
    lecturer1 = Lecturer('Ivan', 'Ivanov')
    lecturer1.courses_attached += ['Python', 'Git']
    
    lecturer2 = Lecturer('Petr', 'Petrov')
    lecturer2.courses_attached += ['Python', 'Java']
    
    # Создаём экспертов
    reviewer1 = Reviewer('Some', 'Buddy')
    reviewer1.courses_attached += ['Python', 'Git']
    
    reviewer2 = Reviewer('John', 'Doe')
    reviewer2.courses_attached += ['Python', 'Java']
    
    
    
    reviewer1.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Git', 8)
    
    reviewer2.rate_hw(student2, 'Python', 7)
    reviewer2.rate_hw(student2, 'Python', 8)
    reviewer2.rate_hw(student2, 'Java', 9)
    
    # Выставление оценок лекторам от студентов
    print("=" * 60)
    print("ВЫСТАВЛЕНИЕ ОЦЕНОК ЛЕКТОРАМ")
    print("=" * 60)
    
    student1.rate_lecture(lecturer1, 'Python', 10)
    student1.rate_lecture(lecturer1, 'Python', 9)
    student1.rate_lecture(lecturer1, 'Git', 8)
    
    student2.rate_lecture(lecturer2, 'Python', 8)
    student2.rate_lecture(lecturer2, 'Python', 9)
    student2.rate_lecture(lecturer2, 'Java', 10)
    
    # Пробуем выставить некорректные оценки
    print("\nПроверка обработки ошибок:")
    print(student1.rate_lecture(lecturer1, 'C++', 7))  # Лектор не ведёт курс
    print(student1.rate_lecture(reviewer1, 'Python', 8))  # Оценивать может только лектор
    print(student2.rate_lecture(lecturer2, 'Python', 15))  # Оценка вне диапазона
    
    
    # Вывод информации об объектах через __str__
    print("=" * 60)
    print("ИНФОРМАЦИЯ ОБ ОБЪЕКТАХ")
    print("=" * 60)
    
    print("\n--- Студенты ---")
    print(student1)
    print()
    print(student2)
    
    print("\n--- Лекторы ---")
    print(lecturer1)
    print()
    print(lecturer2)
    
    print("\n--- Эксперты ---")
    print(reviewer1)
    print()
    print(reviewer2)
    
    # Сравнение студентов и лекторов
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ ОБЪЕКТОВ")
    print("=" * 60)
    
    print(f"\nСравнение студентов:")
    print(f"student1 > student2: {student1 > student2}")  # True/False
    print(f"student1 < student2: {student1 < student2}")
    print(f"student1 == student2: {student1 == student2}")
    
    print(f"\nСравнение лекторов:")
    print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
    print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
    print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
    
    # Подсчет средних оценок по курсам
    print("\n" + "=" * 60)
    print("ПОДСЧЕТ СРЕДНИХ ОЦЕНОК ПО КУРСАМ")
    print("=" * 60)
    
    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]
    
    # Средняя оценка за ДЗ по курсу Python
    avg_hw_python = average_hw_grade_for_course(students_list, 'Python')
    print(f"\nСредняя оценка за ДЗ по курсу 'Python': {avg_hw_python:.2f}")
    
    # Средняя оценка за ДЗ по курсу Git
    avg_hw_git = average_hw_grade_for_course(students_list, 'Git')
    print(f"Средняя оценка за ДЗ по курсу 'Git': {avg_hw_git:.2f}")
    
    # Средняя оценка за ДЗ по курсу Java
    avg_hw_java = average_hw_grade_for_course(students_list, 'Java')
    print(f"Средняя оценка за ДЗ по курсу 'Java': {avg_hw_java:.2f}")
    
    # Средняя оценка за лекции по курсу Python
    avg_lecture_python = average_lecture_grade_for_course(lecturers_list, 'Python')
    print(f"\nСредняя оценка за лекции по курсу 'Python': {avg_lecture_python:.2f}")
    
    # Средняя оценка за лекции по курсу Git
    avg_lecture_git = average_lecture_grade_for_course(lecturers_list, 'Git')
    print(f"Средняя оценка за лекции по курсу 'Git': {avg_lecture_git:.2f}")
    
    # Средняя оценка за лекции по курсу Java
    avg_lecture_java = average_lecture_grade_for_course(lecturers_list, 'Java')
    print(f"Средняя оценка за лекции по курсу 'Java': {avg_lecture_java:.2f}")
    
   