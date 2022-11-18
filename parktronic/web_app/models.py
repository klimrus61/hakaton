from django.db import models

class ElectroCar(models.Model):
    """электрокар"""
    car_model = models.TextField()
    car_number = models.TextField()

    def __str__(self):
        return self.car_number



class Person(models.Model):
    SEX = (
        ('M', 'Мужской'),
        ('Ж', 'Женский')
    )
    full_name = models.TextField()
    list_cars = models.ForeignKey(ElectroCar, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars')
    birth = models.DateField()
    gender = models.CharField(max_length=10, choices=SEX)

    def __str__(self):
        return self.full_name

# фио, модель машины, номер машины, год рж, пол
