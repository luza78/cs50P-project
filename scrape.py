import cloudscraper
import re
from bs4 import BeautifulSoup
import csv
from time import sleep


def main():
    # Sleep timer
    sleep_timer = 30

    # Variables for reading
    links = []

    # Variables for writing
    output = []

    # Meal types
    meals = [
        "breads",
        "soups",
        "breakfasts",
        "desserts",
        "main-course",
        "salads",
    ]

    for i in range(len(meals)):
        # Progress counter
        counter = 1

        path = "links/" + meals[i] + "-links.csv"

        with open(path) as file:
            reader = csv.reader(file)
            for row in reader:
                links.append(row[0])

        for link in links:
            # Progress
            print(f"Progress: {counter} out of {len(links)} for {meals[i]}")
            counter += 1
            # Every 200 scrapes, take a sleep
            if counter % 200 == 0:
                print(f"sleeping for {sleep_timer} seconds...")
                sleep(sleep_timer)

            # Initialize instances of scrape and soup object
            while True:
                try:
                    scraper = cloudscraper.create_scraper()
                    html = scraper.get(link).text
                except Exception:
                    print(
                        f"Connection Interrupted, Sleeping for {sleep_timer * 5} seconds, before retrying"
                    )
                    sleep(sleep_timer * 5)
                else:
                    break

            soup = BeautifulSoup(html, "lxml")

            # Parsing HTML

            # Recipe title
            recipe = soup.findAll(class_=("wprm-recipe-name"))
            title = clean_text(recipe)

            # Description
            recipe = soup.find(class_=("entry-content"))
            description = []
            for d in recipe.findAll("p"):
                description.append(d.text)
            description = "Description:\n" + "\n".join(description)

            # Cook time / prep / total
            recipe = soup.findAll(class_=("wprm-recipe-meta-container"))
            meta = clean_text(recipe)
            meta = remove_duplicates(meta)

            # Servings
            recipe = soup.findAll(class_=("wprm-recipe-servings-container"))
            servings = "\n" + clean_text(recipe)

            # Ingredients
            recipe = soup.findAll(class_=("wprm-recipe-ingredient-group"))
            ingredients = "Ingredients:" + clean_text(recipe)
            ingredients = ingredients.strip()

            # Instructions
            recipe = soup.findAll(class_=("wprm-recipe-instruction-group"))
            instructions = "\nInstructions:\n" + clean_text(recipe)

            # Notes
            recipe = soup.find(class_=("wprm-recipe-notes"))
            notes = []
            try:
                for note in recipe.findAll("span"):
                    notes.append(note.text + "\n")
                str_notes = "Notes:\n" + "".join(notes)
            except AttributeError:
                str_notes = ""

            # Add all values to a list of  dicts to prepare for writing
            output_dict = dict()
            output_dict["title"] = title
            output_dict["meta"] = meta
            output_dict["description"] = description
            output_dict["servings"] = servings
            output_dict["ingredients"] = ingredients
            output_dict["instructions"] = instructions
            output_dict["notes"] = str_notes
            output.append(output_dict)

        # New file name
        new_file_name = "recipes/" + meals[i] + ".csv"
        with open(new_file_name, "w") as output_file:
            headers = [
                "title",
                "meta",
                "description",
                "servings",
                "ingredients",
                "instructions",
                "notes",
            ]
            writer = csv.DictWriter(output_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(output)

        # Clears output list, and links before new category
        output.clear()
        links.clear()
        # Sleep before starting next scrape
        print(f"{meals[i]} complete, Sleeping for {sleep_timer * 10} second(s)...")
        sleep(sleep_timer * 10)


def clean_text(soup_object):
    cleaned_text = []
    for r in soup_object:
        try:
            text = r.text.strip()
            text = text.replace("View Recipe Comments", "")
            text = text.replace("SavePrintEmail", "")
            text = text.replace("▢", "\n-")
            text = re.sub(r"([^ ])([A-Z])", r"\1 \2", text)
        except Exception as e:
            print(e)
        else:
            cleaned_text.append(text)
            cleaned_text.append("\n\n")
    # Returns the cleaned text as a string
    return "".join(cleaned_text)


def remove_duplicates(s):
    # Mainly used in prep time
    split = s.split(" ")
    no_duplicates = []
    for index, _ in enumerate(split):
        if index != 0:
            if split[index] == split[index - 1]:
                continue
            else:
                no_duplicates.append(split[index])
        else:
            no_duplicates.append(split[index])
    # Returns a string with no (back to back) duplicate words
    return " ".join(no_duplicates)


if __name__ == "__main__":
    main()
