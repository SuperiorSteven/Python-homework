# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_name):
    return pet_shop_name ["name"]
    
def get_total_cash(total):
    return total["admin"]["total_cash"]

def add_or_remove_cash(shop,amount_to_add):
    shop ["admin"]["total_cash"] += amount_to_add

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(shop, pets_to_add):
    shop ["admin"]["pets_sold"] += pets_to_add

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets =[]

    for pet in shop["pets"]:
        if pet ["breed"] == breed:
            pets.append(pet)
    return pets 
    
def find_pet_by_name(shop, name):

    for pet_name in shop ["pets"]:
        if pet_name["name"] == name:
         return pet_name
        
def remove_pet_by_name(shop, name):

    for pet_name in shop ["pets"]:
        if pet_name["name"] == name:
            