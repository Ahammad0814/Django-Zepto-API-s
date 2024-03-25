from django.db import models

# Create your models here.

class Category(models.Model):
    ImageSrc = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)

class BaseItemsData(models.Model):
    Discount = models.IntegerField(default=0)
    ImageSrc = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Info = models.CharField(max_length=255)
    Actual_Price = models.IntegerField(default=0)
    Price = models.IntegerField()
    Quantity = models.IntegerField(default=0)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.Name
    
class ForYouItems(BaseItemsData):
    pass
    
class Fruits_Vegetables(BaseItemsData):
    pass

class Atta_Oil(BaseItemsData):
    pass

class Masala_Dryfruits(BaseItemsData):
    pass

class Sweet_Craving(BaseItemsData):
    pass

class Frozen_Food(BaseItemsData):
    pass

class Packed_Food(BaseItemsData):
    pass

class Dairy_Food(BaseItemsData):
    pass

class Cool_Drinks(BaseItemsData):
    pass

class Munchies(BaseItemsData):
    pass

class Meat_Fish_Egg(BaseItemsData):
    pass

class Breakfast_Sauces(BaseItemsData):
    pass

class Tea_Coffee(BaseItemsData):
    pass

class Biscuits_Cookies(BaseItemsData):
    pass

class Makeup_Skincare(BaseItemsData):
    pass

class Bath_Body_Hair(BaseItemsData):
    pass

class Cleaning(BaseItemsData):
    pass

class Home_Needs(BaseItemsData):
    pass

class Electronics(BaseItemsData):
    pass

class Grooming(BaseItemsData):
    pass

class Hygiene(BaseItemsData):
    pass

class Baby_Care(BaseItemsData):
    pass

class Pet_Care(BaseItemsData):
    pass

class Paan_Corner(BaseItemsData):
    pass