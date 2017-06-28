def get_cook_book():
	cook_book = {}
	with open('recipe.txt', 'r') as f:
		for line in f:
			dish = line.lower().strip()
			ing_list = []
			cook = []
			for s in range (int(f.readline().strip())):
				e = f.readline().strip().split(' | ')
				ing_list = list(map(str.strip, e))
				elements = {}
				elements['ingridient_name'] = ing_list[0]
				elements['quantity'] = int(ing_list[1])
				elements['measure'] = ing_list[2]
				cook.append(elements)
			cook_book[dish] = cook
			f.readline()
	return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book = get_cook_book()):
	shop_list = {}
	for dish in dishes:
		for ingridient in cook_book[dish]:
			new_shop_list_item = dict(ingridient)
			new_shop_list_item['quantity'] *= person_count
			if new_shop_list_item['ingridient_name'] not in shop_list:
				shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
			else:
				shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
	return shop_list

def print_shop_list(shop_list):
      for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
      person_count = int(input('Введите количество человек: '))
      dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
      shop_list = get_shop_list_by_dishes(dishes, person_count)
      print_shop_list(shop_list)

create_shop_list()