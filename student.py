class Student:
    def __init__(self, name: str):
        self._name = name
        self._grades = {}
    
    @property
    def name(self) -> str:
        return self._name
    
    def add_grade(self, subject: str, grade: int):
        if not isinstance(grade, int) or not (2 <= grade <= 5):
            raise ValueError("оценка должна быть целым числом от 2 до 5")
            
        if subject not in self._grades:
            self._grades[subject] = []
        self._grades[subject].append(grade)
        
    def average(self, subject: str = None) -> float:
        if subject is None:
            all_grades = []
            for grades_list in self._grades.values():
                all_grades.extend(grades_list)
                
            if not all_grades:
                return 0.0
            return sum(all_grades) / len(all_grades)
        else:
            if subject not in self._grades or not self._grades[subject]:
                raise KeyError(f"у студента {self.name} нет оценок по предмету '{subject}' ")
            return sum(self._grades[subject]) / len(self._grades[subject])
                
    def subjects(self) -> list[str]:
        return sorted(list(self._grades.keys()))
        
    def debts(self) -> list[str]:
        debt_subject = []
        for subj in self._grades:
            if self.average(subj) < 3:
                debt_subject.append(subj)
        return sorted(debt_subject)
        
    def __lt__(self, other) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average() < other.average()
        
    def __repr__(self) -> str:
        return f"Student('{self.name}', {self.average():.2f})"
        
        
class Group:
    def __init__(self, name: str):
        self.name = name
        self._students = []
        
    def add(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError("в группу можно добавить только объекты класса Student")
        if any(s.name == student.name for s in self._students):
            raise ValueError(f"студент с именем '{student.name}' уже есть в группе ")
            
        self._students.append(student)
        
    def __len__(self) -> int:
        return len(self._students)
        
    def __contains__(self, student_name: str) -> bool:
        return any(s.name == student_name for s in self._students)
        
    def ranking(self) -> list[Student]:
        return sorted(self._students, key=lambda s: (-s.average(), s.name))
        
    def with_debts(self) -> list[str]:
        return [s.name for s in self._students if len(s.debts()) > 0]


a = Student("Аня")
a.add_grade("матанализ", 5)
a.add_grade("матанализ", 4)
a.add_grade("информатика", 5)

b = Student("Боря")
b.add_grade("матанализ", 2)
b.add_grade("информатика", 4)

print(a.average())
print(a.average("матанализ"))
print(a.subjects())
print(b.debts())
print(b < a)

try:
    a.average("физика")
except KeyError as e:
    print(f"Ошибка: {e}")

g = Group("ИСиТ-1")
g.add(a)
g.add(b)

print("Аня" in g)
print(g.ranking())
print(g.with_debts())

try:
    g.add(Student("Аня"))
except ValueError as e:
    print(f"Ошибка: {e}") 