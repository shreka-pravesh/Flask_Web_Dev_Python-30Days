Day 10 – Static Files, CSS Styling & Passing Data to Templates

What We Learned

 * Today we focused on using static files inside Flask and learned how to style our web pages using CSS.
 * We also practiced sending dynamic values from Python to HTML using Jinja2.
 * This is the foundation for building visually clean and modern Flask applications.

New Concepts

 Static Folder
 
  > A special directory (static/) used to store CSS, images, and other frontend files.
  > url_for() for Static Files
  > Used inside HTML to correctly load CSS or images:
    * {{ url_for('static', filename='styles.css') }}

Template Variables

  Send data from Python to HTML using:
   return render_template("index.html", title="Homepage")

And display it using:
  {{ title }}

Basic CSS Styling
Applied simple styles like colors, fonts, alignment, spacing, etc., to improve the UI.

Programs Covered

1. contact_manager.py

Concept:
Using lists to store user-submitted contact data and displaying it through a template.

What it does:
Adds contacts (name + email) and shows all saved contacts on a webpage.

2️. movie_collection.py

Concept:
Creating and managing a list of movies and passing it to HTML using render_template().

What it does:
Displays a small movie collection with title, year, and rating.

3️. task_manager.py

Concept:
Handling user form submissions using POST and storing tasks inside a Python list.

What it does:
Lets the user add simple tasks and shows the updated task list instantly.

4️. recipe_book.py

Concept:
Using dictionaries inside lists to store structured data (recipe name + ingredients).

What it does:
Shows a collection of recipes and the ingredients for each one.

5️. wishlist_app.py

Concept:
Working with simple data storage and passing dynamic lists to an HTML template.

What it does:
Allows users to add items to a wishlist and displays all added items.

HTML File Descriptions (Very Small & Simple)

contact.html:
 Shows all saved contacts in a clean list.

movies.html:
 Displays a list of movies with title, year, and rating.

tasks.html:
 Shows all added tasks and includes a small task submission form.

recipes.html:
 Displays recipes and their ingredients in a simple format.

wishlist.html:
 Shows all items added to the wishlist.

Summary

  > Used static folder for CSS and images
  > Loaded styles with url_for()
  > Passed dynamic data into templates
  > Created a simple styled page using Flask + HTML + CSS
  > Learned the basic structure of a front-end integrated Flask app
