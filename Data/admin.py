from django.contrib import admin
from . models import Category,ForYouItems,Fruits_Vegetables,Atta_Oil,Masala_Dryfruits,Frozen_Food,Sweet_Craving,Packed_Food,Dairy_Food,Cool_Drinks,Munchies,Meat_Fish_Egg,Breakfast_Sauces,Tea_Coffee,Biscuits_Cookies,Makeup_Skincare,Bath_Body_Hair,Cleaning,Home_Needs,Electronics,Grooming,Hygiene,Baby_Care,Pet_Care,Paan_Corner

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category,CategoryAdmin)

class ForYouItemsAdmin(admin.ModelAdmin):
    pass
admin.site.register(ForYouItems, ForYouItemsAdmin)

class FruitsVegetablesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Fruits_Vegetables,FruitsVegetablesAdmin)

class Atta_OilAdmin(admin.ModelAdmin):
    pass
admin.site.register(Atta_Oil,Atta_OilAdmin)

class Masala_DryfruitsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Masala_Dryfruits, Masala_DryfruitsAdmin)

class Frozen_FoodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Frozen_Food,Frozen_FoodAdmin)

class Sweet_CravingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sweet_Craving,Sweet_CravingAdmin)

class Packed_FoodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Packed_Food,Packed_FoodAdmin)

class Dairy_FoodAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dairy_Food,Dairy_FoodAdmin)

class Cold_DrinksAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cool_Drinks,Cold_DrinksAdmin)

class MunchiesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Munchies,MunchiesAdmin)

class Meat_Fish_EggAdmin(admin.ModelAdmin):
    pass
admin.site.register(Meat_Fish_Egg,Meat_Fish_EggAdmin)

class Breakfast_SaucesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Breakfast_Sauces,Breakfast_SaucesAdmin)

class Tea_CoffeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tea_Coffee,Tea_CoffeeAdmin)

class Biscuits_CookiesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Biscuits_Cookies,Biscuits_CookiesAdmin)

class Makeup_SkincareAdmin(admin.ModelAdmin):
    pass
admin.site.register(Makeup_Skincare,Makeup_SkincareAdmin)

class Bath_Body_HairAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bath_Body_Hair,Bath_Body_HairAdmin)

#########################################
class CleaningAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cleaning,CleaningAdmin)

class Home_NeedsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Home_Needs,Home_NeedsAdmin)

class ElectronicsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Electronics,ElectronicsAdmin)

class GroomingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Grooming,GroomingAdmin)

class HygieneAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hygiene,HygieneAdmin)

class Baby_CareAdmin(admin.ModelAdmin):
    pass
admin.site.register(Baby_Care,Baby_CareAdmin)

class Pet_CareAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pet_Care,Pet_CareAdmin)

class Paan_CornerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Paan_Corner,Paan_CornerAdmin)