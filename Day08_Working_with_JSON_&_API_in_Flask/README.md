Day 08 – Working with JSON & APIs in Flask

What We Learned

  -> Today we explored how Flask works with JSON and APIs to fetch, display, and send real-time data.
  ->This is the base for creating data-driven web apps like weather dashboards, crypto trackers, and more.

New Concepts

  > JSON (JavaScript Object Notation): A lightweight format used for sending and receiving data.
  > External APIs: Connect Flask with real-world data from the internet.
  > Custom APIs: Create your own API endpoints using jsonify().
  > POST Requests: Send data from an HTML form to the Flask backend.

Programs Overview

File	Description

  * crypto_price_checker.py	Fetches live Bitcoin price in USD and displays it neatly.
  * fake_user_api.py	Returns fake user data as JSON using a Flask API route.
  * post_data_to_server.py	Accepts form input and returns a JSON response.
  * currency_converter_api.py	Converts USD to INR using a live exchange rate API.


HTML File Descriptions

File	Description

  * crypto.html	Displays live Bitcoin price and last updated time.
  * submit.html	Form for sending data to Flask (POST request).
  * currency.html	Shows live USD to INR conversion.

(No HTML needed for fake_user_api.py as it returns raw JSON.)

Summary

  > Connected Flask apps with live APIs
  > Learned to use requests for fetching data
  > Returned and displayed JSON data dynamically
  > Built interactive programs that simulate real-world backend logic
