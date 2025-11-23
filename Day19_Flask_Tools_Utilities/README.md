Day 19 – Flask Tools Utilities Collection

I built a set of small but very useful Flask-based tools.
Each program focuses on taking user input, processing it, and showing a clear, simple output.
These types of tools are commonly seen in utility dashboards and productivity apps.

Concepts Covered Today

1. Handling User Input Through Forms

 You learned how Flask collects user data using:

 request.form.get("field_name")

 This is the base of all interactive web apps.

2. Basic Data Processing in Python

We practiced operations like:

 Time calculations

 Temperature formatting

 Splitting money

 Simple encryption

 Random data generation


3. Passing Results Back to HTML

You used:

 return render_template("index.html", result=value)

 This helps display processed results on the webpage.

4. Using Python Modules for Real Tasks

Such as:

 datetime → time difference

 random → random meal suggestions

 String operations → simple encryption

Programs Overview

 1. time_diff.py	- Calculates the time difference between two given times.

 2. temp_formatter.py -	Converts temperature between Celsius & Fahrenheit.

 3. budget_splitter.py -	Splits a total budget equally among people.

 4. simple_encryptor.py -	Encrypts text using a basic shifting method.

 5. meal_suggester.py -	Suggests a random meal from a list.

HTML File Descriptions


 1. time_diff.html -	Takes two time inputs and shows the difference.
  
 2. temperature.html -	Lets user convert temperature with one click.
 
 3. budget.html -	Input total amount + number of people and displays split result.
 
 4. encrypt.html -	Form to enter text and see encrypted output.
 
 5. meal.html -	Shows a random meal suggestion each reload or button press.

Summary

 > How to build real-world utility tools
 > How to handle form inputs clearly
 > How to perform calculations inside Flask

How to return processed results back to templates

How to structure code cleanly for multiple small tools
