Day 21 – Working With APIs, JSON & Secure Endpoints

Learnt building and interacting with different types of APIs in Flask.
We learned how to send JSON, receive JSON, consume our own API, and protect routes with API keys.
These concepts are very important for backend development and real-world web apps.

New Concepts Learned Today

1. JSON APIs

 We learned how Flask can send and receive JSON data using request.get_json() and jsonify().

2. Service Endpoints

 We created small API services (like tip calculator) that return structured JSON responses.

3. Local API Consumption

 We learned how one Flask app can call another route inside the same app using the requests module.

4. JSON POST Receiver

 We practiced reading JSON data sent from tools, apps, or even from another backend.

5. API Key Protected Routes

 A simple form of security where only requests with a correct key can access the API.

Programs Overview

1. notes_api.py

Concept: Creating a simple API that stores and returns note entries.
What it does: Stores notes in memory and returns them as JSON when requested.

2. tip_service.py

Concept: Building a calculation API.
What it does: Accepts a bill amount and returns the calculated 10% tip as JSON.

3. consume_local_api.py

Concept: Calling a local API from another endpoint.
What it does: Internally sends a request to another Flask route and shows the fetched response.

4. json_receiver.py

Concept: Handling POST requests with JSON input.
What it does: Reads JSON data sent by the user and returns a confirmation response.

5. key_protected_api.py

Concept: Adding basic API key security to an endpoint.
What it does: Only allows access when the client sends the correct API key.


Summary

 > Learned how to build API routes in Flask

 > Practiced sending and receiving JSON

 > Created a local API consumer

 > Added basic API-key protection

 > Built small but practical backend tools
