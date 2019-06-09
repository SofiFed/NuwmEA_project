from django.db import models

class Manager(models.Model):

  COLDWATER_MANAGER = 1
  HOTWATER_MANAGER = 2
  WARM_MANAGER = 3
  ELECTRICITY_MANAGER = 4
  TEMPERATURE_MANAGER = 5
  ROLE_CHOICES = (
      (COLDWATER_MANAGER, 'coldwater_manager'),
      (HOTWATER_MANAGER, 'hotwater_manager'),
      (WARM_MANAGER, 'warm_manager'),
      (ELECTRICITY_MANAGER, 'electricity_manager'),
      (TEMPERATURE_MANAGER, 'temperature_manager'),
  )
  manager_email = models.EmailField(max_length=254, blank=False, unique=True)
  role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True, default=1)
  is_staff = models.BooleanField(default=True)

  def __str__(self):
    return str(self.manager_email)






    
  

  








