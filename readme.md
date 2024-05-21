    # 'wtc.py - What to cook ?'
    #### Video Demo: https://youtu.be/kAK-EK-awhs
    #### Description:
        $ 'WTC' is a python command-line appliction to assist the user in picking a recipe to cook.
        $ When run, it allows the user to pick a food category, the program will then select a random recipe
        $ for the user, including the recipe title, cooktime, quantity, ingredients, instructions.
        $ The program also had an optional flag to display the recipe descriptions.
        $ Each food category has hundreds of recipes, so lots of yummy stuff to get into!

        $ You can choose from the following categories:
            - Main-course (1) 
            - Breakfast (2)
            - Salads (3)
            - Soups (4)
            - Breads (5)
            - Desserts (6)
        
        $ Upon selecting a recipe, the program will serve a random recipe from that category.
        $ The user will then have the following options:
            - (Y) Serves another recipe from the same category
            - (N) Exits the application
            - (R) Returns to main menu

__________________________________________________________________________________________________________________
    
    ### Usage & Setup:
        $ Create a venv, using the requirements.txt which contains the package dependencies.
        $ navigate to the application root directory and type 'python project.py [-d] [-h --help]
        $ -d flag adds the desciption of the recipe.
        $ -h and/or --help display usage information
    
__________________________________________________________________________________________________________________
    
    ### Recipes & How:
        $ When researching my project, I could not find an API for recipes that met my needs.
        $ I took this opportunity to learn some basic webscraping.
        $ First I made a script for my favourite cookbook website, to scrape all the different url links for the
        $ different food categories. Thereafter I made another script that would use those links to scrape the html,
        $ and parse it using the Beautiful Soup 4 library, thereafter it was written into CSV files
        $ which are in the project/links folder.
        $ The project/recipes folder contains the csv files for all the recipes, which project.py uses.
        $ There's thousands of recipes to choose from.

__________________________________________________________________________________________________________________
    
    ### Copyright:
        $ All the recipes are copyright of TIEGHAN GERARD, https://www.halfbakedharvest.com.
        $ This is not meant for commercial distribution, and is for personal use only.

__________________________________________________________________________________________________________________
    
    ## Acknowledgements:
        ~ I want to take this opportunity to thank Dr. David Malan, and the CS50P team for
        ~ creating such a fantastic course, and making it so accessible.
        ~ CS50, and CS50P have had a huge impact in my life, and have inspired me to pursue
        ~ Computer Science further. Something I never would have believed possbile back in
        ~ January 2023.
        ~ From my whole heart, THANK YOU!
        
__________________________________________________________________________________________________________________

    ## Author:
        Luke Schaufuss
        lukeschaufuss@gmail.com
        www.lukeschaufuss.com

__________________________________________________________________________________________________________________
        
        
