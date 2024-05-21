from random import randint
import sys
import csv
import re
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from time import sleep

description_flag = False


def main():
    global description_flag
    # Checks commandline arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "-d":
            description_flag = True
        elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
            sys.exit(
                "Usage: Python project.py [-d] Description [-h --help] Help \n Selects a random recipe from a category. By default recipe description will be omitted"
            )
        else:
            sys.exit(
                "Usage: Python project.py [-d] Description [-h --help]"
            )
    welcome = Text("To exit press ctrl + D at any time", style="italic plum1")
    print(welcome)
    while True:
        try:
            selector = select_recipe()

        except EOFError:
            sys.exit("Goodbye :)")
        else:
            while True:
                path = get_recipe_path(selector)
                new_recipe = get_recipe(path)
                print()

                text = Text("", justify="center")
                text.append("\n")
                text.append("\n")
                text.append(new_recipe[1], style="cyan3")
                if len(new_recipe) == 7:
                    text.append(new_recipe[2], style="grey82")
                text.append(new_recipe[-4], style="salmon1")
                text.append(new_recipe[-3], style="plum1")
                text.append(new_recipe[-2], style="sky_blue1")

                title = Text(new_recipe[0], style="white")
                panel = Align(
                    Panel(
                        text,
                        border_style="bold white",
                        title=title,
                    ),
                    align="center",
                )
                print(panel)
                if not another_recipe():
                    break


def select_recipe():
    while True:
        print()
        menu = main_menu()
        print(menu)
        try:
            selector = int(input("Hit enter to submit: ").strip())
            if selector < 1 or selector > 6:
                raise ValueError
        except ValueError:
            print("Enter a number between 1-6 and press enter")
            continue
        else:
            return selector


def another_recipe():
    while True:
        # Style Prompt
        menu_prompt = options()
        print(menu_prompt, end="")
        for i in range(4):
            print()
        # User input
        answer = input("Type option and press Enter: ").lower()
        if answer == "n":
            bye = Text("(｡◕‿◕｡)'ﾉ''", style="plum1")
            print(bye, end="")
            sleep(0.5)
            print(".", end="")
            sleep(0.5)
            print(".", end="")
            sleep(0.5)
            print(".", end="")
            sleep(0.5)
            sys.exit()
        # Will get another recipe from same category
        elif answer == "y":
            for i in range(4):
                print()
            return True
        # Return to 'main menu' to select new category
        elif answer == "r":
            return False
        else:
            continue


# Style main menu
def main_menu():
    title = "Type in a number to select recipe"
    text = Text(
        "Main-course (1), Breakfast (2), Salads (3), Soups (4), Breads (5), Desserts (6)"
    )
    text.stylize("cyan3")
    text.stylize("white", 13, 14)
    text.stylize("white", 28, 29)
    text.stylize("white", 40, 41)
    text.stylize("white", 51, 52)
    text.stylize("white", 63, 64)
    text.stylize("white", 77, 78)
    options = Align(
        Panel(
            text,
            border_style="yellow",
            title=title,
        ),
        align="center",
    )
    return options


# Style options box
def options():
    text = Text("(Y) For another recipe | (N) To exit | (R) For main menu")
    text.stylize("green", 1, 2)
    text.stylize("red1", 26, 27)
    text.stylize("yellow", 40, 41)
    options = Align(
        Panel(
            text,
            border_style="cyan3",
            title="Options",
        ),
        align="center",
    )
    return options


def get_recipe_path(n):
    if n == 1:
        return "recipes/main-course.csv"
    elif n == 2:
        return "recipes/breakfasts.csv"
    elif n == 3:
        return "recipes/salads.csv"
    elif n == 4:
        return "recipes/soups.csv"
    elif n == 5:
        return "recipes/breads.csv"
    elif n == 6:
        return "recipes/desserts.csv"
    else:
        return None


def get_recipe(path):
    global description_flag
    recipes = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            recipes.append(row)

    # Generates a random number between 0 and length of recipe
    random_recipe = randint(0, len(recipes) - 1)

    # Filters out recipes missing titles
    while recipes[random_recipe]["title"].strip() == "":
        random_recipe = randint(0, len(recipes) - 1)

    recipes[random_recipe]["instructions"] = "\n" + format_instructions(
        recipes[random_recipe]["instructions"]
    )
    recipes[random_recipe]["ingredients"] = format_ingredients(
        recipes[random_recipe]["ingredients"]
    )
    if description_flag == True:
        selected_recipe = []
        selected_recipe.append(recipes[random_recipe]["title"])
        selected_recipe.append(recipes[random_recipe]["meta"])
        selected_recipe.append(recipes[random_recipe]["description"])
        selected_recipe.append(recipes[random_recipe]["servings"])
        selected_recipe.append(recipes[random_recipe]["ingredients"])
        selected_recipe.append(recipes[random_recipe]["instructions"])
        selected_recipe.append(recipes[random_recipe]["notes"])
        return selected_recipe
    else:
        selected_recipe = []
        selected_recipe.append(recipes[random_recipe]["title"])
        selected_recipe.append(recipes[random_recipe]["meta"])
        selected_recipe.append(recipes[random_recipe]["servings"])
        selected_recipe.append(recipes[random_recipe]["ingredients"])
        selected_recipe.append(recipes[random_recipe]["instructions"])
        selected_recipe.append(recipes[random_recipe]["notes"])
        return selected_recipe


def format_instructions(s):
    match = re.search(r"(\d\. \w)", s)
    if match:
        lines = re.sub(r"(\d\. \w)", r"\n\1", s)
        return lines
    else:
        lines = re.sub(r"(^\nInstructions:)", r"\1\n", s)
        return lines


def format_ingredients(s):
    lines = re.sub(r"(^Ingredients:)", r"\1\n", s)
    return lines


if __name__ == "__main__":
    main()
