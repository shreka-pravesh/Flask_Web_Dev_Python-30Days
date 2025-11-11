Day 07 – Template Inheritance (Base Layouts)

What We Learned

  > Today we learned how to use template inheritance in Flask to create reusable page layouts.
  > It helps make websites look consistent and keeps our code cleaner.

New Concepts

  * base.html – a shared layout with header, footer, and navigation.
  * {% extends 'base.html' %} – lets other pages use the same layout.
  * {% block content %} – area where each page adds its own content.
  * Reusable design – we avoid repeating the same HTML code for every page.

Programs Overview

File	Description

 1. simple_layout.py:	Basic homepage using a shared layout.

 2. about_page.py:	Adds an “About Us” page with the same layout.

 3. contact_page.py:	Displays a simple contact section.

 4. mini_portfolio_layout.py:	Shows a small personal portfolio page.

 5. layout_bonus.py:	Demonstrates dynamic page titles using blocks.

HTML File Descriptions

File	Description

 1. base.html:	Main layout with header, footer, and navbar.
 
 2. home.html:	Extends base layout for homepage content.

 3. about.html:	Shows a short “About Us” section.

 4. contact.html: Displays simple contact info.

 5. portfolio.html:	Shows a small personal project list.

 6. base_title.html:	Layout that allows custom titles for pages.

 7. page.html:	Custom page with its own title and content.


Summary

  > Created reusable web layouts using template inheritance
  > Built multiple pages with one consistent design

Learned to use {% extends %} and {% block %} in Jinja2

Moved one step closer to building real, multi-page Flask websites 🚀
