
from task1 import Person, Student, GroupLeader

student = Student("Vladyslav", "Radchuk", "IT-32")
leader = GroupLeader("Olena", "Koval", "IT-32", "+380 67 000 00 00")

print("Перевірка isinstance():")
print("student, Person:", isinstance(student, Person))
print("student, Student:", isinstance(student, Student))
print("student, GroupLeader:", isinstance(student, GroupLeader))
print("leader, Person:", isinstance(leader, Person))
print("leader, Student:", isinstance(leader, Student))
print("leader, GroupLeader:", isinstance(leader, GroupLeader))

print("\nПеревірка issubclass():")
print("Student, Person:", issubclass(Student, Person))
print("GroupLeader, Person:", issubclass(GroupLeader, Person))
print("GroupLeader, Student:", issubclass(GroupLeader, Student))
print("Person, Student:", issubclass(Person, Student))

print("\nПорядок пошуку методів:")
print(GroupLeader.__mro__)
