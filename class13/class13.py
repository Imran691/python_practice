class Teacher():
    def __init__(self, teacher_id: int, teacher_name: str) -> None:
        self.name: str = teacher_name
        self.id : int = teacher_id
        self.organization: str = "PIAIC"

    def subject(self, subject_name: str) -> None:
        print(f"{self.name} teaches {subject_name}")

teacher1 : Teacher = Teacher(1, "Qasim")

print(teacher1.id)
print(teacher1.name)
print(teacher1.organization)

print(teacher1.subject("Gen AI"))