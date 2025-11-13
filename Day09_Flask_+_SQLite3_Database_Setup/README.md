Day 09 – Flask + SQLite3 Database Setup

What We Learned Today

  > Today we explored how Flask works with a real database (SQLite3) — this allows our apps to save, update, and display data permanently, even after restarting the program.
  > Earlier, our data disappeared when we stopped the server. But from now, it will stay saved just like real-world web apps.

New Concepts Explained

1. SQLite3 Database

   SQLite3 is a lightweight database that comes built-in with Python.
   We use it to store and manage information such as contacts, tasks, or student records.
   It creates a small .db file (like contacts.db) where all data is saved.

2. Database Connection

 We connect to the database using:
   con = sqlite3.connect("database_name.db") 
   This creates or opens a database file.
   After doing any task (like insert, read, delete), we must close it using con.close().

3. Creating Tables

Tables are like folders inside the database that hold data in columns and rows.
  We create one using:
   con.execute("CREATE TABLE IF NOT EXISTS table_name (id INTEGER PRIMARY KEY, name TEXT)")
  This creates the table only if it doesn’t already exist.

4. Inserting Data

  To save new information:
    cur.execute("INSERT INTO table_name (column1, column2) VALUES (?, ?)", (value1, value2))
  The question marks (?) are placeholders for the actual data — this keeps things safe and clean.

5. Fetching Data

  To show saved data on our web page:
    cur.execute("SELECT * FROM table_name")
    data = cur.fetchall()
  Then we pass this data to our HTML template using render_template().

6. HTML + Jinja2 Integration

  In the HTML templates, we use simple Jinja2 syntax to loop through the data and display it:

  {% for item in data %}
    <li>{{ item[1] }}</li>
  {% endfor %}

   This connects our Python database logic with what the user sees in the browser.

Projects You Built Today

  Project Name	Description

 1.	Contact Book	Add and view saved contact names and phone numbers.
 2.	Student Records Manager	Store student names with grades.
 3.	Task Tracker	Add and display daily tasks from the database.
 4. Feedback Collector	Collect feedback from users and display all responses.
 5.	Book List App	Save book titles and authors to build a reading list.


Each project includes:

  * main.py file (Flask backend)
  * templates/ folder with HTML file
  * A .db file automatically created when you run the app

How It All Works (Simple Flow)

  1. User fills the form in HTML (for example, adds a contact or task).

  2. Flask receives this form data using request.form.

  3. The data is stored in the SQLite3 database using SQL commands.

  4. Flask fetches the saved data and passes it to the HTML page.

  5. The browser displays the list of saved data neatly.


End Result

 By the end of Day 09, you now know how to:

   > Connect Flask with a real database.
   > Store and view data permanently.
   > Display that data dynamically using HTML templates.
   > Build mini real-world apps with CRUD foundations.
