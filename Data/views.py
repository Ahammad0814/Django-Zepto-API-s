from . models import Category,ForYouItems,Fruits_Vegetables,Atta_Oil,Masala_Dryfruits,Frozen_Food,Sweet_Craving,Packed_Food,Dairy_Food,Cool_Drinks,Munchies,Meat_Fish_Egg,Breakfast_Sauces,Tea_Coffee,Biscuits_Cookies,Makeup_Skincare,Bath_Body_Hair,Cleaning,Home_Needs,Electronics,Grooming,Hygiene,Baby_Care,Pet_Care,Paan_Corner
from .serializer import CategorySerializer,ForYouSerializer,F_VSerializer,Atta_OilSerializer,Masala_DryfruitSerializer,Sweet_CravingSerializer,Frozen_FoodSerializer,Packed_FoodSerializer,Dairy_FoodSerializer,Cool_DrinksSerializer,MunchiesSerializer,Meat_Fish_EggSerializer,Breakfast_SaucesSerializer,Tea_CoffeeSerializer,Biscuits_CookiesSerializer,Makeup_SkincareSerializer,Bath_Body_HairSerializer,CleaningSerializer,Home_NeedsSerializer,ElectronicsSerializer,GroomingSerializer,HygieneSerializer,Baby_CareSerializer,Pet_CareSerializer,Paan_CornerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED

# Create your views here.

def Choose_Data(request):
    if request.resolver_match.url_name == 'ForyouData':
        Main_Data = ForYouItems.objects.all()
    elif request.resolver_match.url_name == 'F_V_Data':
        Main_Data =  Fruits_Vegetables.objects.all()
    elif request.resolver_match.url_name == 'A_O_Data':
        Main_Data =  Atta_Oil.objects.all()
    elif request.resolver_match.url_name == 'M_D_Data':
        Main_Data =  Masala_Dryfruits.objects.all()
    elif request.resolver_match.url_name == 'S_C_Data':
        Main_Data =  Sweet_Craving.objects.all()
    elif request.resolver_match.url_name == 'F_F_Data':
        Main_Data =  Frozen_Food.objects.all()
    elif request.resolver_match.url_name == 'P_F_Data':
        Main_Data =  Packed_Food.objects.all()
    elif request.resolver_match.url_name == 'D_F_Data':
        Main_Data =  Dairy_Food.objects.all()
    elif request.resolver_match.url_name == 'C_D_Data':
        Main_Data = Cool_Drinks.objects.all()
    elif request.resolver_match.url_name == 'M_Data':
        Main_Data = Munchies.objects.all()
    elif request.resolver_match.url_name == 'M_F_E_Data':
        Main_Data = Meat_Fish_Egg.objects.all()
    elif request.resolver_match.url_name == 'B_S_Data':
        Main_Data = Breakfast_Sauces.objects.all()
    elif request.resolver_match.url_name == 'T_C_Data':
        Main_Data = Tea_Coffee.objects.all()
    elif request.resolver_match.url_name == 'B_C_Data':
        Main_Data = Biscuits_Cookies.objects.all()
    elif request.resolver_match.url_name == 'M_S_Data':
        Main_Data = Makeup_Skincare.objects.all()
    elif request.resolver_match.url_name == 'B_B_H_Data':
        Main_Data = Bath_Body_Hair.objects.all()
    elif request.resolver_match.url_name == 'C_Data':
        Main_Data = Cleaning.objects.all()
    elif request.resolver_match.url_name == 'H_N_Data':
        Main_Data = Home_Needs.objects.all()
    elif request.resolver_match.url_name == 'E_Data':
        Main_Data = Electronics.objects.all()
    elif request.resolver_match.url_name == 'G_Data':
        Main_Data = Grooming.objects.all()
    elif request.resolver_match.url_name == 'H_Data':
        Main_Data = Hygiene.objects.all()
    elif request.resolver_match.url_name == 'Baby_Care_Data':
        Main_Data = Baby_Care.objects.all()
    elif request.resolver_match.url_name == 'Pet_Care_Data':
        Main_Data = Pet_Care.objects.all()
    elif request.resolver_match.url_name == 'P_C_Data':
        Main_Data = Paan_Corner.objects.all()
    return Main_Data

@api_view(['GET'])
def CategoryData(request):
    if request.method == 'GET':
        Item_Data = Category.objects.all()
        serializer = CategorySerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        Data = CategorySerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status= HTTP_201_CREATED)

@api_view(['GET'])
def ForYouData(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = ForYouSerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        Data = ForYouSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status= HTTP_201_CREATED)
       
@api_view(['GET'])
def F_V_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = F_VSerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        Data = F_VSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status= HTTP_201_CREATED)
    
@api_view(['GET'])
def Atta_Oil_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Atta_OilSerializer(Item_Data, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        Data = Atta_OilSerializer(data = request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)
    
@api_view(['GET'])
def M_D_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Masala_DryfruitSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Masala_DryfruitSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)
    
@api_view(['GET'])
def S_C_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Sweet_CravingSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Sweet_CravingSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)
    
@api_view(['GET'])
def F_F_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Frozen_FoodSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Frozen_FoodSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)
    
@api_view(['GET'])
def P_F_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Packed_FoodSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Packed_FoodSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)
    
@api_view(['GET'])
def D_F_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Dairy_FoodSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Dairy_FoodSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)
    
@api_view(['GET'])
def C_D_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Cool_DrinksSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Cool_DrinksSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)
    
@api_view(['GET'])
def M_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = MunchiesSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = MunchiesSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def M_F_E_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Meat_Fish_EggSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Meat_Fish_EggSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def B_S_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Breakfast_SaucesSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Breakfast_SaucesSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def T_C_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Tea_CoffeeSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Tea_CoffeeSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def B_C_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Biscuits_CookiesSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Biscuits_CookiesSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def M_S_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Makeup_SkincareSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Makeup_SkincareSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def B_B_H_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Bath_Body_HairSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Bath_Body_HairSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)
    
@api_view(['GET'])
def C_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = CleaningSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = CleaningSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)
    
@api_view(['GET'])
def H_N_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Home_NeedsSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Home_NeedsSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def E_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = ElectronicsSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = ElectronicsSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def G_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = GroomingSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = GroomingSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def H_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = HygieneSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = HygieneSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def Baby_Care_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Baby_CareSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Baby_CareSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def Pet_Care_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Pet_CareSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Pet_CareSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)

@api_view(['GET'])
def P_C_Data(request):
    if request.method == 'GET':
        Item_Data = Choose_Data(request)
        serializer = Paan_CornerSerializer(Item_Data, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        Data = Paan_CornerSerializer(data=request.data)
        if Data.is_valid() == True:
            Data.save()
        return Response(status=HTTP_201_CREATED)