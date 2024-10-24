from abc import ABC, abstractmethod

class Students:
    def init (self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.completed_assignments = 0
        self.courses = []
        
    def enroll_in(self, course: 'Course'):
        self.courses.append(course)
        print(f"Enrolled in {course} course")
        
    def complete_assignment(self, assignment: 'Assignment'):
        if assignment.course in self.courses:
            self.completed_assignments += 1
            print(f"{self.name} completed {assignment.title}")
        else:
            print(f"{self.name} is not enrolled in {assignment.course.name}")
        
    def view_progress(self):
        print(f"{self.name} has completed {self.completed_assignments} assignments")

class Professors:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info 
        
    def create_course(self, course: 'Course'):
        return course 
        
    def manage_course(self, course: 'Course'):
        print(f"Professor {self.name} is managing the {course}")
        

        
class Course(ABC):
    def __init__(self, name, instructor: 'Professor', content):
        self.name = name
        self.instructor = instructor 
        self.content = content
        self.assignments = []
        

    @abstractmethod    
    def display_content(self):
        pass
    
    @abstractmethod
    def add_assignment(self):
        pass
    
    def __str__(self) -> str:
        return f"Course: {self.name}, Instructor: {self.instructor.name}"
        
        
class GraduateCourse(Course):
    def __init__(self, name, instructor, content):
        super().__init__(name, instructor, content)
        
    def display_content(self):
        print(f"Graduate Course Content: {self.content}")

    def add_assignment(self, assignment: 'Assignment'):
        self.assignments.append(assignment)
        print(f"Assignment '{assignment.title}' added to Graduate Course {self.name}")


class UnderGraduateCourse(Course):
    def __init__(self, name, instructor, content):
        super().__init__(name, instructor, content)
    
    def display_content(self):
        print(f"Undergraduate Course Content: {self.content}")
        
    def add_assignment(self, assignment: 'Assignment'):
        self.assignments.append(assignment)
        print(f"Assignment '{assignment.title}' added to UnderGraduate Course {self.name}")
  
class Assignments:
    def __init__(self, title, course: 'Course' ):
        self.title = title
        self.course = course
        
    def __str__(self):
        return f"{self.title} for {self.course.name}"
        
        
        
professor = Professors("Alan Wingate", "<alanwingate234@gmail.com")

course = GraduateCourse("Applied Mathematics", professor, "Differential Equation")
professor.manage_course(course)
