# by Kami Bigdely
# Extract Class

class Recipe:

    def __init__(self, name, prep_time, is_veggie, food_type, cuisine, items, instructions):
        self.name = name
        self.prep_time = prep_time
        self.is_veggie = is_veggie
        self.food_type = food_type
        self.cuisine = cuisine
        self.instructions = instructions
        self.items = items

    def __repr__(self):
        item_string = ''
        for item in self.items:
            item_string += f'{item}\n'
        return f'Name: {self.name}\n Prep Time: {self.prep_time}\n Is Veggie: {self.is_veggie}\n\
                 Food Type: {self.food_type}\n Ingredients: {item_string} \n\
                 Recipe: {self.instructions}\n ***'


foods = {'butternut squash soup': [45, True, 'soup', 'North African',
                                   ['butter squash', 'onion', 'carrot', 'garlic', 'butter', 'black pepper', 'cinnamon',
                                       'coconut milk'], '1. Grill the butter squash, onion, carrot and garlic in the oven until'
                                   'they get soft and golden on top 2. Put all in blender with'
                                   'butter and coconut milk. Blend them till they become puree. Then move the content into a pot'
                                   '. Add coconut milk. Simmer for 5 mintues.'],
         'shirazi salad': [5, True, 'salad', 'Iranian', ['cucumber', 'tomato', 'onion', 'lemon juice'],
                           '1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt'
                           '4. Mixed them thoroughly'],
         'Home-made Beef Sausage': [60, False, 'deli', 'All', ['sausage casing', 'regular ground beef', 'garlic',
                                                               'corriander seeds', 'black pepper seeds', 'fennel seed', 'paprika'], '1. In a blender,'
                                    ' blend corriander seeds, black pepper seeds, fennel seeds and garlic to make'
                                    'the seasonings 2. In a bowl, mix ground beef with the'
                                    'seasoning 3. Add all the content to a sausage stuffer. Put the casing on'
                                    "the stuffer funnel. Rotate the stuffer's handle (or turn it on) to make your yummy sausages!"]}

recipes = []
for key, value in foods.items():
    recipe = Recipe(key, value[0], 'Yes' if value[1] else "No",
                    value[2], value[3], value[4], value[5])
    recipes.append(recipe)
    print(recipe)
