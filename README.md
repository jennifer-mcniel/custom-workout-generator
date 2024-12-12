# custom-workout-generator

Workout Generator App
Author: Jennifer McNiel

Overview

The Workout Generator App is a web application that generates personalized workout plans based on user inputs. This project is a semester long assignment for Green River College's SDEV 450 course in Artificial Intelligence. Users can submit their preferences through a form, and the app returns a tailored workout plan with descriptions and images. The application leverages Retrieval-Augmented Generation (RAG) and calls Groq's hosted LLMs to generate customized workouts.  

Features

Dynamic workout generation based on user input

Responsive workout table with descriptions and images

Clickable images that expand into a modal popup

Prerequisites

To set up and run this project locally, ensure you have the following installed:

Python (v3.8 or higher)

Flask (v2.0 or higher)

A modern web browser (e.g., Chrome, Firefox)

A code editor (e.g., VS Code)

Installation
1. clone the repository 
https://github.com/jennifer-mcniel/custom-workout-generator.git

2. install python  amd flask dependencies

Run the App
1. start the flask server 
    flask --app app run 

2. open browser and navigate to 127.0.0.1:5000

3. Fill in workout preferences and submit form to generate workout

Interacting with the App

Submit Form: Enter your preferences and click the submit button.

View Workout Plan: The workout plan will be displayed in a table with exercises, sets, reps, and instructions.

Expand Images: Click on the images in the table to open them in a modal popup.

File Structure

custom-workout-generator/
|--- static/         # static files
|--- templates/      # html templates
|--- app.py          # Flask application entry
|--- controller.py   # API layer, assembles LLM call
|--- exercise10.json # sample of exercises to load in DB
|--- exercises.json  # complete set of exercises to load in DB
|--- groqService.py  # layer that calls the Groq service
|--- README.md       # project documentation
|--- workoutsDB.py   # layer that assembles and queries the DB

API

The app interacts with the /api/generate-workout endpoint to retrieve workout data. Ensure the Flask server is running for the app to function correctly.

Request

Endpoint: /api/generate-workout

Method: POST

Content-Type: application/json

Body:

{
    "exerciseType": "strength",
    "duration": 30,
    "preferences": ["arms", "core"]
}

Response

Success (200):

{
    "WorkoutPlanDescription": "A customized workout plan for strength training.",
    "WorkoutJson": [
        {
            "name": "Push-Up",
            "sets": 3,
            "reps": 15,
            "instructions": ["Place your hands shoulder-width apart.", "Lower your body until your chest almost touches the floor.", "Push back to the starting position."],
            "images": ["pushup1.jpg", "pushup2.jpg"]
        }
    ]
}

Error (500): Server error message

Analysis
The workout generator app dynamically generates personalized workouts for users based on preferences. It is much more flexible and useful than a database alone limited to simple filters or searches. If a user doesn't spell something correctly or is unsure about requirements the app can adjust and accomodate them. Users interact with a clean form to input their preferences and recieve their results in an organized table with all of the essential information they need to complete their workout. 

This app relies heavily on external endpoints for sources. If the free exersize DB stops hosting image files or Groq's api endpoint becomes inconsistent the app's functionality may suffer.  The RAG implementation to supply the entire exercise database for the query uses more than the allowed token limits so the app is only set up to use a portion of the available exercise dataset. It also limits the number of calls to the Groq service per minute. So there could be errors if a user requests another workout too quickly. 

Potential Improvements
The usefullness of the app would improve greatly if token limits were increased by subscribing to a paid service with higher token limits. I also would like to implement a user login featre that would save user workouts to their profile. This could be expanded on even further to provide fitness tracking features like past and current weights for exercises and history of completed workouts. I would have also liked to have add more UI responsiveness to make it more mobile friendly. 


Acknowledgments

OpenAI ChatGPT for assistance with project development

Free Exercise DB https://github.com/yuhonas/free-exercise-db for exercise images and data