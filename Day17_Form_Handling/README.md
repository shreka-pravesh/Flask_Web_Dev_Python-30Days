Day 17 – Form Handling Practice in Flask

Today’s focus was on creating interactive web pages where users type something, submit it, and instantly see a response.
We learned how Flask receives form data using POST requests, processes it, and returns clean results.

Concepts Covered

HTML Forms – how users enter data

POST Method – sending form data safely

request.form – reading values inside Flask

Rendering results dynamically – showing output based on user inputs.


Programs Covered

1. Simple Journal App

Concept:
Working with lists and forms to save text entries during a session.

What It Does:
Allows the user to type journal entries and displays all entries on the page.

2. Word Counter Tool

Concept:
Handles form submission and processes text on the backend.

What It Does:
Counts the total number of words typed by the user and shows the result.

3. Flashcard Learner

Concept:
Uses dictionaries and dynamic rendering to show questions and answers.

What It Does:
Shows a flashcard question and reveals the answer when clicked.

4. Personal Reminder

Concept:
Stores form data temporarily and displays reminders on the page.

What It Does:
Lets the user add reminders and shows the list of saved reminders.

5. Daily Rating Logger

Concept:
Processes numeric inputs and stores user ratings for the session.

What It Does:
User selects a rating (1–5) and it keeps a log of today’s ratings.

📄 HTML File Descriptions

 1. journal.html – Text box to rwite a journal entry

 2. counter.html – A textarea where the user types text

 3. flashcard.html – Flashcard question with a button to reveal the answer

 4. remainder.html - Small form to add remainders

 5. rating.html – Shows rating button and displays them


Summary

* Build forms in HTML
* Accept user input in Flask using POST
* Process and return results dynamically
* Create interactive mini-tools
