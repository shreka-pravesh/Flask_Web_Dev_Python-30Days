Day 16 – Interactive & Personal Utility Apps with Flask

Today’s focus was on building small, interactive Flask applications that help users track, record, organize, and interact with simple data.
These programs are lightweight, beginner-friendly, and perfect for building real-world logic step by step.

Programs Covered

1. Number Sorting Tool

Concept: Sorting a list of numbers sent by the user.
What it does: Takes comma-separated numbers from the user, sorts them, and shows the sorted result.

2. Simple Habit Tracker

Concept: Storing small daily habits in a list.
What it does: Lets users add habits (like drink water, read 10 mins) and displays all saved habits.

3. Mini Notes Drawer

Concept: Saving short text notes in memory.
What it does: Users type a small note, and it gets added to a list of notes displayed on the page.

4. Quick Math Quiz

Concept: Generating random questions using Python.
What it does: Shows a random two-number addition question, checks the user’s answer, and shows if it's correct.

5. Mood Recorder

Concept: Storing mood entries to track how the user feels.
What it does: User selects their mood (happy/sad/etc.) and the page stores and displays all previous mood entries.

Concepts Learned 

1. Using Python Lists as Temporary Storage

 We used simple lists inside the Flask app to store:

  * Habits
  * Notes
  * Moods
  * This helps us understand how backend stores data before we move to databases.

2. Handling User Input with Forms

 All programs used HTML forms that send data to Flask using POST method:

  * Text input
  * Number fields
  * Dropdowns
  * Buttons
  * This helps us accept and process real user data.

3. Random Module for Dynamic Logic

 For the Quick Math Quiz, we used:

  * import random
  * to generate dynamic questions each time.


4. Splitting and Cleaning User Text Input

 In Number Sorting Tool, we learned how to:

  * Take comma-separated numbers
  * Split them
  * Convert to integers
  * Sort them
  * This is useful for processing custom user inputs.

📌 Summary

 > Sorted numbers
 > Tracked simple habits
 > Stored small notes
 > Generated math quizzes
 > Recorded daily moods
