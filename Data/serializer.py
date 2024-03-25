from rest_framework.serializers import ModelSerializer
from . models import Category,ForYouItems,Fruits_Vegetables,Atta_Oil,Masala_Dryfruits,Frozen_Food,Sweet_Craving,Packed_Food,Dairy_Food,Cool_Drinks,Munchies,Meat_Fish_Egg,Breakfast_Sauces,Tea_Coffee,Biscuits_Cookies,Makeup_Skincare,Bath_Body_Hair,Cleaning,Home_Needs,Electronics,Grooming,Hygiene,Baby_Care,Pet_Care,Paan_Corner

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ForYouSerializer(ModelSerializer):
    class Meta:
        model = ForYouItems
        fields = '__all__'
        
class F_VSerializer(ModelSerializer):
    class Meta:
        model = Fruits_Vegetables
        fields = '__all__'
       
class Atta_OilSerializer(ModelSerializer):
    class Meta:
        model = Atta_Oil
        fields = '__all__'
        
class Masala_DryfruitSerializer(ModelSerializer):
    class Meta:
        model = Masala_Dryfruits
        fields = '__all__'
        
class Sweet_CravingSerializer(ModelSerializer):
    class Meta:
        model = Sweet_Craving
        fields = '__all__'

class Frozen_FoodSerializer(ModelSerializer):
    class Meta:
        model = Frozen_Food
        fields = '__all__'

class Packed_FoodSerializer(ModelSerializer):
    class Meta:
        model = Packed_Food
        fields = '__all__'

class Dairy_FoodSerializer(ModelSerializer):
    class Meta:
        model = Dairy_Food
        fields = '__all__'
        
class Cool_DrinksSerializer(ModelSerializer):
    class Meta:
        model = Cool_Drinks
        fields = '__all__'
        
class MunchiesSerializer(ModelSerializer):
    class Meta:
        model = Munchies
        fields = '__all__'
        
class Meat_Fish_EggSerializer(ModelSerializer):
    class Meta:
        model = Meat_Fish_Egg
        fields = '__all__'

class Breakfast_SaucesSerializer(ModelSerializer):
    class Meta:
        model = Breakfast_Sauces
        fields = '__all__'

class Tea_CoffeeSerializer(ModelSerializer):
    class Meta:
        model = Tea_Coffee
        fields = '__all__'

class Biscuits_CookiesSerializer(ModelSerializer):
    class Meta:
        model = Biscuits_Cookies
        fields = '__all__'

class Makeup_SkincareSerializer(ModelSerializer):
    class Meta:
        model = Makeup_Skincare
        fields = '__all__'

class Bath_Body_HairSerializer(ModelSerializer):
    class Meta:
        model = Bath_Body_Hair
        fields = '__all__'

class CleaningSerializer(ModelSerializer):
    class Meta:
        model = Cleaning
        fields = '__all__'
        
class Home_NeedsSerializer(ModelSerializer):
    class Meta:
        model = Home_Needs
        fields = '__all__'
        
class ElectronicsSerializer(ModelSerializer):
    class Meta:
        model = Electronics
        fields = '__all__'

class GroomingSerializer(ModelSerializer):
    class Meta:
        model = Grooming
        fields = '__all__'

class HygieneSerializer(ModelSerializer):
    class Meta:
        model = Hygiene
        fields = '__all__'

class Baby_CareSerializer(ModelSerializer):
    class Meta:
        model = Baby_Care
        fields = '__all__'

class Pet_CareSerializer(ModelSerializer):
    class Meta:
        model = Pet_Care
        fields = '__all__'

class Paan_CornerSerializer(ModelSerializer):
    class Meta:
        model = Paan_Corner
        fields = '__all__'