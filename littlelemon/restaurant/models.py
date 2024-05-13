from django.db import models


# Problem: MySQLdb.OperationalError: (1071, 'Specified key was too long; max key length is 1000 bytes')
# Solution: on mysql my.ini change this line:
# default-storage-engine=MYISAM
# with this:
# default-storage-engine=InnoDB
# and restart mysql service



# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 255)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured = models.BooleanField(db_index=True)
    inventory = models.IntegerField(default=False)

    # def __str__(self)-> str:
    #     return self.title
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    

    
    