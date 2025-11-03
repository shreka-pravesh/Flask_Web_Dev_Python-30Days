Day 02 – Routing Basics + Simple HTML Pages

I learned how to:

=> Create multiple pages in Flask using routes
=> Send data from Python to HTML
=> Build basic navigation between pages
=> Use templates to make the web app more organized

Programs in This Folder

1. visitor_counter.py

Concept: Counting visits using a global variable.
What it does: Increases the visitor count every time the page is refreshed.

HTML file: counter.html
What it does: Displays the current visitor number using the variable {{ count }} passed from Flask.

2. about_me.py

Concept: Passing variables from Python to HTML using render_template().
What it does: Displays your name and favorite hobby on a simple HTML page.

HTML file: about.html
What it does: Shows your name and hobby from the Flask backend.

3. simple_links.py

Concept: Linking multiple pages using Flask routes.
What it does: Creates a simple two-page website (Home and Contact) with navigation links.

HTML files:

 > home.html – Main page with a link to the Contact page
 > contact.html – Contact page with a link back to Home

4. user_profile.py

Concept: Dynamic routing using URL parameters.
What it does: Displays a username taken directly from the URL (like /user/Leena).

HTML file: profile.html
What it does: Shows the username dynamically using {{ username }}.

5. mini_website.py

Concept: Building a small website with multiple pages.
What it does: Has routes for Home, About, and Contact — each page rendered using HTML.

HTML files:

 > home.html – Welcome page
 > about_page.html – Simple about page
 > contact.html – Contact information page

6. random_message.py (Bonus Program)

Concept: Using Python’s random module in Flask routes.
What it does: Displays a random motivational message every time the page is refreshed.

Summary

 * Learned how routing connects URLs to functions
 * Used HTML templates with Flask
 * Passed data from backend to frontend
 * Built multiple pages with working links
 * Added fun logic like visitor count and random messages

HTML file: message.html
What it does: Shows the selected random message and a link to refresh for a new one.
