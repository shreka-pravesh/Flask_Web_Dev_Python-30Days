Day 05 – Handling Forms & User Input

Concept Learned:

  Today we learned how to collect user input from HTML forms and process it in Flask using GET and POST methods.
  This is how websites take user data — like login, feedback, or search — and display results.

New Topics We Learned Today

1. HTML Forms

Forms allow users to enter text, numbers, or other input and send them to Flask.
  - <form action="/route" method="POST"> ... </form>
  - action → tells Flask which route to send data to.
  - method → defines how data is sent (GET or POST).

2. Flask request Object

We use request.form (for POST) or request.args (for GET) to get the values entered by users.

name = request.form['username']
query = request.args.get('query')

3. GET vs POST

GET: Sends data through the URL (good for search forms).
POST: Sends data secretly in the background (good for login or feedback).

Programs Overview

1. greeting_form.py

Concept: Taking user input through a form.
What it does: Asks for your name and displays a greeting.

2. feedback_form.py

Concept: Sending text data using POST method.
What it does: Collects feedback and thanks the user.

3. login_page.py

Concept: Basic form validation in Flask.
What it does: Checks username and password before login.

4. search_bar.py

Concept: Using GET method for search queries.
What it does: Takes a search word and shows what you searched.

5. simple_calculator.py

Concept: Handling multiple inputs from one form.
What it does: Adds two numbers and shows the total.

HTML Files Description

  * greeting_form.html → Takes your name and shows a greeting.
  * feedback_form.html → Collects feedback and displays a thank-you note.
  * login_page.html → Lets you enter login details and checks them.
  * search_bar.html → Takes a search word and shows what you searched.
  * simple_calculator.html → Adds two numbers and shows the result.

What We Achieved Today

  > Learned to build and process HTML forms in Flask
  > Understood the difference between GET and POST
  > Learned how to use request.form and request.args
  > Created 5 working Flask form-based apps
