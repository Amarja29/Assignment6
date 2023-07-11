from APPLICATION.Application import Application
from APPLICATION.Course import Course

class NumberOfCourses(Application,Course):
    total_count=0

    def __CourseCountProg(self):
        #total_count=0
        _Prog_count = Course.ProgrammingCourse(Course)

        if _Prog_count!=1 and _Prog_count!=2 and _Prog_count!=3:
            _Prog_count = 0

        if _Prog_count == 1 or _Prog_count==2:
            self.total_count+=1
        if _Prog_count == 3:
            self.total_count+=2
        return self.total_count

    def __CourseCountDesign(self):
        #total_count=0
        _Design_count = Course.DesignCourse(Course)
        if _Design_count!=1 and _Design_count!=2 and _Design_count!=3:
            _Design_count=0
        if _Design_count == 1 or _Design_count == 2:
            self.total_count += 1
        if _Design_count == 3:
            self.total_count += 2
        return self.total_count


    def Welcome(self):
        print(f"Welcome! You have erolled {self.total_count} courses ")
        return self.total_count