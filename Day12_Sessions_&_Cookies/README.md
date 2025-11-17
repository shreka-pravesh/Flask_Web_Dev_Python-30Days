Day 12 – Working With Cookies & Sessions in Flask

Learned how to store data inside the browser using cookies and sessions.
These tools help websites remember user information, even if the page is refreshed.

New Concepts Learned

1. Cookies

 * Small pieces of data stored in the user's browser.
 * Used to remember preferences like theme, cart items, visit count, etc.
 * Set using response.set_cookie().

2. Sessions

 * Server-side storage linked to each user.
 * Used for private or login-related data.
 * Access using session['key'].


3. Persistent User Data

Data stays even after refresh.

Used for:

 * login authentication
 * visit tracking
 * theme selection
 * saving items

Program Descriptions

1. store_name.py

Concept: Uses cookies to save a user’s name.
What it does: Stores the name in the browser and shows it on every visit.

HTML (store_name.html):
Simple form to enter your name and display the saved name.

2. visit_counter.py

Concept: Uses cookies to count how many times a user visited the page.
What it does: Increases the counter on every refresh.

HTML (counter.html):
Shows the current visit count.

3. theme_session.py

Concept: Stores theme preference (light/dark) using sessions.
What it does: Remembers selected theme across page reloads.

HTML (theme.html):
Button to switch theme + displays current theme.

4. login_session.py

Concept: Uses sessions to store login state.
What it does: Allows user to log in once and stay logged in until logout.

HTML (login.html):
Simple login form + shows login status.

5. shopping_cart_cookie.py

Concept: Stores items in the shopping cart using cookies.
What it does: Adds items and keeps them saved in the browser.

HTML (cart.html):
Form to add items + displays saved cart list.

Summary

> Store data in cookies
> Keep session data safe on the server
> Build login systems
> Remember theme preferences
> Track visits
> Save shopping cart items
