import random

ingredient_doc = list(map(lambda x: x.rstrip('\n'),list(open('./testingredients.txt'))))


def select_ingredients_from_list(list, count):
    count = int(count)
    if count == 0:
        return ''
    ingred = ''
    _ = 0
    while _ < count:
        current_ingred = list[random.randint(1, len(list)-1)]
        if _ == count - 1:
            ingred += ' ' + current_ingred
        else:
            ingred += ' ' + current_ingred+','
        _+=1
    return ingred


def generate_salad(ingredients,veggie_count=3,protein_count=1,carb_count=1,topping_count=1):
    ingredient_list = []

    for i in ingredients:
        ingredient_list.append(i.split(','))

    #select single ingredients
    leafy = ingredient_list[0][random.randint(1, len(ingredient_list[0])-1)]
    dressing = ingredient_list[5][random.randint(1, len(ingredient_list[5])-1)]

    #select multi ingredients
    veggie = select_ingredients_from_list(ingredient_list[1], veggie_count)
    protein = select_ingredients_from_list(ingredient_list[2], protein_count)
    carbs = select_ingredients_from_list(ingredient_list[3], carb_count)
    topping = select_ingredients_from_list(ingredient_list[4], topping_count)

    salad_name = f'Your salad base is {leafy} with{carbs},{veggie} and{protein} topped with{topping} and {dressing} dressing'
    if random.randint(1,1000) == 1:
        salad_name = 'FLEISCHSALAT!!!'
    if random.randint(1,1000) == 1:
        salad_name = 'Francuska salata'
    return salad_name


if __name__ == '__main__':
    veg = input('Enter the number of different veggies:')
    prot = input('Enter the number of different protein:')
    carb = input('Enter the number of different carbs:')
    top = input('Enter the number of different toppings:')
    print(generate_salad(ingredient_doc, veg, prot, carb, top))
