Day 15 – Mini Projects with Advanced Routing & Data Handling

Today’s projects focus on organizing content, building multi-page structures, and storing user-generated data.
Each project introduces real-world concepts used in blogging platforms, media apps, bookmarking tools, and simple analytics.

New Concepts Learned 

1. Multi-Page Routing

  You learned how to create multiple pages inside one Flask project using separate routes.

2. Passing Data to Templates

  We used render_template() with variables to send lists, text, and objects to HTML.

3. Storing Items in Lists (Temporary Storage)

  Instead of databases, you practiced storing blog posts, images, bookmarks, code snippets, and visits in simple Python lists.

4. Basic POST Form Handling

  Some projects accept user input using HTML forms + Flask POST requests.

5. Dynamic Rendering

  HTML loops ({% for item in list %}) were used to show dynamic lists like gallery images, bookmarks, and logs.

Programs Overview

1. Personal Blog

  A simple blog where you can add titles & content. Posts are stored in a list and displayed on the homepage.

  Concept:
    Handles form submission, stores posts in memory, and displays them dynamically.

  What it Does:
    Lets users add blog posts and instantly see them listed.

  HTML Description:
    Contains a form to add posts and a section to display all blog entries.

2. Image Gallery

  A small gallery app where users add image URLs and the gallery updates automatically.

  Concept:
    Accepts image URLs via POST, stores them in a list, and sends them to the template.

  What it Does:
    Shows all added images like a simple online gallery.

  HTML Description:
     Displays images in a clean grid and has a form to add new image links.

3. Bookmark Manager

  A tool to save and display website links with titles.

  Concept:
    Takes title + URL input, stores bookmarks, and renders them as clickable links.

  What it Does:
     Creates a simple bookmark list like a browser's bookmarks.

  HTML Description:
     Form for adding bookmarks and a section showing all saved links.

4. Code Snippets

   A mini app to save and display short code pieces.

  Concept:
    Stores snippets with titles and code blocks, passes data to template for display.

  What it Does:
    Acts like a small coding notebook to save useful code.

  HTML Description:
    Form for adding snippets and a section that shows saved code in a styled block.

5. Visit Logger

  Tracks every visit and logs them with timestamp.

  Concept:
    Appends a timestamp to a list every time the page is visited.

  What it Does:
    Shows a running history of all visits.

  HTML Description:
    Displays all visit timestamps in a simple lists

Summary

  > Today you learned how to build small but powerful applications using:
  > Multi-page Flask routing
  > POST form handling
  > Dynamic lists and rendering

Storing temporary data without a database

HTML loops for dynamic output
