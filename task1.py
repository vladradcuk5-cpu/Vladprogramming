
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def describe(self):
        return f"{self.name} {self.surname}"


class Student(Person):
    def __init__(self, name, surname, group):
        super().__init__(name, surname)
        self.group = group

    def describe(self):
        return f"{super().describe()}, {self.group}"


class GroupLeader(Student):
    def __init__(self, name, surname, group, phone):
        super().__init__(name, surname, group)
        self.phone = phone

    def describe(self):
        return f"{super().describe()}, group leader, {self.phone}"


student = Student("Vladyslav", "Radchuk", "IT-32")
leader = GroupLeader("Olena", "Koval", "IT-32", "+380 67 000 00 00")

print(student.describe())
print(leader.describe())
