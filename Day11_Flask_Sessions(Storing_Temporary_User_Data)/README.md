Day 11 – Flask Sessions (Storing Temporary User Data)

 * Learned how to use Flask sessions, which allow us to store small amounts of data temporarily for each user.
 * This helps us build features like login systems, counters, theme settings, and shopping carts.

New Concepts Learned

1. Flask Session

  > A built-in way to store user data temporarily.
  > Data stays until the browser closes or you remove it.

Example: session['username'] = name


2. Secret Key

  > Required to use sessions.
  > Protects session data.

Example: app.secret_key = "something_secret"


3. Session Operations

  > Set data → session['item'] = value
  > Get data → session.get('item')
  > Remove data → session.pop('item', None')
  > Clear session → session.clear()


4. Using Forms with Sessions

  > Store user input (like username, color theme, etc.)
  > Display it on another page or keep it for the session.

Programs Overview (Python + HTML)

Program	What It Does

1. store_name.py	Saves user's name in session and displays it.
   
2. counter.py	Increases count every time user refreshes.
   
3. theme_switcher.py	Saves light/dark theme preference using session.
 
4. login_session.py	Simple login system using session without a database.
 
5. shopping_cart.py	Adds items to a temporary cart stored in session.


HTML File Descriptions

File	Description

> store.html	Simple form to enter your name and display stored session name.

> counter.html	Shows the updated counter value each refresh.

> theme.html	HTML form to switch between Light/Dark themes.

> login.html	Login form for username and password.

> cart.html	Adds items and shows the session shopping cart list.

Summary of Day 11

  -> Learned how to use Flask sessions to store temporary user data.
  
  -> Created 5 fully working apps using session data.
  
  -> Used form submission and session management together.
  
  -> Built real-world features like login, cart, and theme selection.
