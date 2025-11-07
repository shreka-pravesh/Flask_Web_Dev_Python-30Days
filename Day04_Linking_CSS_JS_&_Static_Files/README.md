Day 04 – Linking CSS, JS & Static Files

Concept Learned:

  > Today we learned how to link CSS and JavaScript files in Flask using the static/ folder.
  > This helps us make our web pages look colorful, styled, and interactive — just like real-world websites!

Definition

1. Static Folder

All design files like CSS, JS, and images are stored inside a folder named static.
This keeps your project neat and organized.

Example:
   <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
   <script src="{{ url_for('static', filename='script.js') }}"></script>

This line tells Flask where to find your static files.

2. CSS (Cascading Style Sheets)

Used to make pages beautiful and readable — you can set colors, fonts, and layouts.

Example:
  button { background-color: #4CAF50; color: white; }

3. JavaScript (JS)

Used to make pages interactive — for example, when clicking a button or changing a theme.

Example:
  function changeColor() { document.body.style.backgroundColor = "lightblue"; }

Programs Overview

1. color_changer.py

Concept: Connect Flask with JS for interactivity.
What it does: Opens a page where clicking a button changes background color.

HTML File: color_changer.html
What it does: Shows a button that triggers color changes through JS.

2. mood_board.py

Concept: Combine Flask, CSS grid, and JS.
What it does: Displays mood cards that react when clicked.

HTML File: mood_board.html
What it does: Shows colorful, clickable cards arranged using CSS grid.

3. mini_portfolio.py

Concept: Use CSS for a neat and professional layout.
What it does: Displays a small personal portfolio with info cards.

HTML File: mini_portfolio.html
What it does: Shows name, intro, and styled cards for projects.

4. theme_toggle.py

Concept: Use JS to switch between dark and light modes.
What it does: Lets users toggle website theme colors.

HTML File: theme_toggle.html
What it does: Includes a button to activate dark or light mode.

5. inspiration_wall.py (Bonus)

Concept: Combine Flask random quotes with CSS design.
What it does: Displays a random motivational quote on every reload.

HTML File: inspiration_wall.html
What it does: Shows a styled quote box and refresh button.

Concepts Covered

* Learned to connect CSS and JS using url_for
* Made our Flask apps more colorful and fun
* Improved project structure with templates and static folders
* Added interactivity with JavaScript

End Result

  > By the end of Day 04, you can:
  > Build visually appealing web pages
  > Use JavaScript for simple dynamic effects
  > Create interactive Flask apps with proper folder structure
