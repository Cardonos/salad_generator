import random

ingredient_doc = list(map(lambda x: x.rstrip('\n'),list(open('./testingredients.txt'))))


def select_ingredients_from_list(lists, count):
    count = int(count)
    ingred = ''
    _ = 0
    if count > len(lists):
        raise ValueError(f'Too many ingredients requested for {lists[0][:-1]}')
    if not count == 0:
        while _ < count:
            current_ingred = lists[random.randint(1, len(lists)-1)]
            lists.pop(lists.index(current_ingred))
            print(lists)
            if _ == count - 1:
                ingred += ' ' + current_ingred
            else:
                ingred += ' ' + current_ingred+','
            _ += 1
    return ingred


def generate_salad(ingredients,veggie_count=3,protein_count=1,carb_count=1,topping_count=1):
    ingredient_list = []
    for i in ingredients:
        ingredient_list.append(i.split(','))

    # select single ingredients
    leafy = ingredient_list[0][random.randint(1, len(ingredient_list[0])-1)]
    dressing = ingredient_list[5][random.randint(1, len(ingredient_list[5])-1)]

    # select multi ingredients
    veggie = select_ingredients_from_list(ingredient_list[1], veggie_count)
    protein = select_ingredients_from_list(ingredient_list[2], protein_count)
    carbs = select_ingredients_from_list(ingredient_list[3], carb_count)
    topping = select_ingredients_from_list(ingredient_list[4], topping_count)

    if topping:
        dressing = 'and ' + dressing
    if protein:
        protein = ' and' + protein

    salad_name = f'Your salad base is {leafy} with{carbs},{veggie}{protein} topped with{topping} {dressing} dressing'
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
