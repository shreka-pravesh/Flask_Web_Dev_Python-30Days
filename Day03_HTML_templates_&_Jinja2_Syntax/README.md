Day 03 – HTML Templates & Jinja2 Syntax

Concept Learned:

Today we learned how to connect HTML templates with Flask using Jinja2 syntax.
Jinja2 helps us send data from Python to HTML and display it dynamically.

I used:

  > {{ variable }} → to show data from Flask
  > {% for %} → to loop through lists or dictionaries
  > {% if %} → to show or hide content based on conditions

This is how real web pages display live data instead of static text!

Programs Covered

1. student_info.py

Concept: Sending variables from Flask to HTML.
What it does: Displays student details (name, age, course).

HTML File: student.html
What it does: Shows data using Jinja2 variables.

2. subject_list.py

Concept: Using Jinja2 loops.
What it does: Lists subjects dynamically from a Python list.

HTML File: subjects.html
What it does: Displays subjects in a simple bullet list.

3. grade_checker.py

Concept: Using if-else conditions in templates.
What it does: Checks if a student passed or failed based on marks.

HTML File: grade.html
What it does: Shows pass/fail message using {% if %}.

 4. score_table.py

Concept: Looping through dictionaries.
What it does: Displays subjects and marks in a table format.

HTML File: scores.html
What it does: Creates a clean table using Jinja2.

5. greeting_page.py

Concept: Sending multiple variables.
What it does: Displays a custom greeting with the user’s name.

HTML File: greeting.html
What it does: Shows message like “Good Morning, Leena!” dynamically.

6. average_calculator.py

Concept: Combining loops and conditions.
What it does: Calculates average marks and displays a short message.

HTML File: average.html
What it does: Shows marks, average, and “Passed” or “Try Again.”

New Concept Learned Today: Jinja2 Template Engine

Symbol Meaning	Example

  * {{ }}	Display data	{{ name }} shows name from Flask
  * {% %}	Run logic (loops/conditions)	{% for x in items %} loops items
  * {# #}	Add comments in template	{# This won’t show in output #}

Jinja2 helps build dynamic, reusable, and interactive web pages — just like professional websites.
