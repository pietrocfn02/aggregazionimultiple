from django.db import models

# Create your models here.
class Employee (models.Model):
    name = models.CharField(max_length=75)


    def __str__(self):
        return self.name


class Project (models.Model):
    project_name = models.CharField(max_length=75)

    def __str__(self):
        return self.project_name


class TimeReport (models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_reports")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_reports")
    day = models.DateField(auto_now_add=True, blank=True)
    number_of_hours = models.IntegerField()


    #def __str__(self):
    #    return str(self.day) + " "+ str(self.number_of_hours) + str(self.project.project_name) + str(self.employee.name)