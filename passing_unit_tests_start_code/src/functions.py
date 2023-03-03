def greet_catalan(name):
    return f"Hola, {name}"

def  greet_mandarin(name):
    return f"Ni hao, {name}"

def count_eggs(list):
    total_eggs = 0
    for item in list:
        total_eggs += item["eggs"]
    
    return total_eggs

def find_chicken_by_name(list, chicken_name):
    for chicken in list:
        if chicken["name"] == chicken_name:

            return chicken
        
        