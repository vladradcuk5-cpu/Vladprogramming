
class Student:
    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year

    def full_name(self):
        return self.name + " " + self.surname

    def age(self, year):
        return year - self.birth_year

    def card(self):
        return (
            "+---------------------+\n"
            f"| {self.full_name():<19} |\n"
            f"| group: {self.group:<12} |\n"
            f"| age in 2026: {self.age(2026):<7} |\n"
            "+---------------------+"
        )


student1 = Student("Vladyslav", "Radchuk", "IT-32", 2007)
student2 = Student("Ivan", "Petrenko", "IT-32", 2006)

print(student1.card())
print()
print(student2.card())
