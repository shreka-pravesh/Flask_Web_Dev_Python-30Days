Day 06 – URL Parameters & Redirects

Concept Learned:

  Today we learned how to use URL parameters to send data through the web address and how to redirect users to another route or webpage.
  This makes navigation dynamic — like when you click on a username and visit their profile page!

New Topics We Learned Today

1. URL Parameters

  * We can send information inside the URL using < >.
  * @app.route('/user/<name>')
  * This means /user/Leena will show Leena’s page.

2. Redirects

  * We use redirect() and url_for() to move users from one page to another.
  * return redirect(url_for('welcome'))
  * Useful after form submissions or when pages are renamed.

Programs Overview

1. greet_user.py

Concept: Passing name in URL.
What it does: Shows a personalized greeting from the URL.

2. show_age.py

Concept: Multiple parameters in URL.
What it does: Displays both name and age from the URL.

3. redirect_example.py

Concept: Basic page redirection.
What it does: Redirects users from /home to /welcome.

4. form_redirect.py

Concept: Redirect after submitting form.
What it does: Takes name from a form and redirects to profile page.

5. mini_link_shortener.py (Bonus)

Concept: Redirecting with short codes.
What it does: Acts like a mini URL shortener (e.g. /go/yt → YouTube).

What We Achieved Today

  > Learned to use < > in routes for dynamic URLs
  > Learned how redirect() and url_for() work together
  >  Built routes that behave like real user profiles and short links
  >  Created 5 unique and working programs
