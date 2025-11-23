Day 20 – Daily Utility Mini-Apps

Today’s focus was on building small but meaningful Flask apps that help with everyday tasks.
We continued practicing HTML forms, POST requests, rendering results, and organizing pages with templates.

Concepts Covered Today

1. Handling User Input (Forms → Flask)

  We used HTML forms to collect user data and processed it inside Flask using POST methods.

2. Passing Values Back to Templates

  After performing simple calculations or storing data, we returned the result using render_template() with variables.

3. Managing Small Data Lists

  Some apps stored items temporarily in Python lists during runtime (idea bank, expense notes).

4. Basic Calculations in Flask

  We performed small computations like totals, differences, and progress percentages directly in the backend.

Programs Covered

1. Daily Expense Notepad

Concept: Collects text input and stores notes in a temporary list.
What it does: Lets users add small daily expense notes and displays them on the page.

2. Simple Goal Saver

Concept: Takes a goal and progress value through a form; calculates progress percentage.
What it does: Shows how much of the goal is completed in a simple visual output.

3. Quick Feedback Collector

Concept: Accepts feedback using POST and stores it in a Python list.
What it does: Lets users submit feedback and shows all feedback entries on the screen.

4. Simple Idea Bank

Concept: Stores typed ideas into an in-memory list.
What it does: Helps users save random ideas and view them like a mini idea-storage page.

5. Sleep Tracker

Concept: Calculates sleep duration from “sleep time” and “wake time”.
What it does: Shows how many hours the user slept based on input.

HTML File Descriptions

1. expense.html

 Simple form to add expense notes and a list to display saved notes.

2. goal.html

 A form to enter goal name + progress and a section to show completed percentage.

3. feedback.html

 A clean input box to submit short feedback and a list that displays all messages.

4. idea.html

 A single input field for ideas and a section showing all stored ideas.

5. sleep.html

 Two input fields for sleep and wake time, showing calculated sleep duration.

Summary

  > Working with POST forms
  > Storing and showing user-generated content
  > Performing simple backend calculations
  > Passing results back into HTML templates
  > Building human-friendly mini tools
