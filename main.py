from Protain import Protain
from Calories import Calories
from Carb import Carb
from Fat import Fat
from Water import Water


def main():
    weight = float(input("Please enter your weight:\n"))
    x = int(input("Are you : 1-lightly_active, 2-moderately_active, 3-very_active, please enter 1, 2, or 3\n"))
    y = int(input("Are you : 1-building_body, 2-normal_body, please enter 1 or 2\n"))
    # create an object from calories
    calories_obj = Calories()
    current_calories = calories_obj.calc_calories(weight, x)
    # create an object protain
    protain_obj = Protain()
    protain_you_need = protain_obj.calc_protain(weight, y)
    # create an object from carb
    carb_obj = Carb()
    carb = carb_obj.calc_carb(weight, x)
    # create an object from fat
    fat_obj = Fat()
    fat = fat_obj.calc_fat(weight, x)
    # create an object from water
    water_obj = Water()
    water_you_need = water_obj.calc_water(weight)
    print("you need", current_calories, "calories per day")
    print("you need", protain_you_need, "gram protain per day")
    print("you need", carb, "gram carbs per day")
    print("you need", fat, "gram fats per day")
    print("you need", water_you_need, "liter per day")


if __name__ == '__main__':
    main()
