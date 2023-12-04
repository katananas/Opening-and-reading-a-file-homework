with open('recept.txt', encoding='utf-8') as file:

  cook_book = {}
  for i in file:
    recepie_name = i.strip()
    ingredients_count = file.readline()
    ingredients = []
    for p in range(int(ingredients_count)):
        recepie = file.readline().strip().split(' | ')
        product, quantity, word = recepie
        ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
    file.readline()
    cook_book[recepie_name] = ingredients
  

print(cook_book)

print()

def get_shop_list_by_dishes(dishes, person_count):
    new_cook = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                
               num = int(ingredient['quantity'])
               num *= person_count
               ingredient['quantity'] = str(num)
               ingredient_1 = ingredient['product'] 
               del ingredient['product']

               if ingredient_1 in new_cook:
                   ingr = (new_cook[ingredient_1])
                   num = int(ingr['quantity'])
                   num *= person_count
                   ingr['quantity'] = str(num)
               else: 
                   new_cook.setdefault(ingredient_1,  ingredient)
               
               
    print()           
    print(new_cook)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)