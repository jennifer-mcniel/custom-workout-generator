from workoutsDB import retrieve_exercises
from groqService import generate_response, create_message
import json



def generate_workout(user_input):
    sample_response = { 
        
            "WorkoutPlanDescription": "SampleTextDescribing workout.",
            "WorkoutJson": [
                {
                    "name": "Push-Ups",
                    "sets": 3,
                    "reps": 15,
                    "instructions": [
                        "Start in a plank position.",
                        "Lower your body until your chest almost touches the floor.",
                        "Push back up to the starting position."
                    ],
                    "images": [
                        "Alternate_Hammer_Curl/0.jpg",
                        "Alternate_Hammer_Curl/1.jpg"
                    ]
                },
                {
                    "name": "90/90 Hamstring",
                    "sets": 3,
                    "reps": 10,
                    "instructions": [
                        "Lie on your back, with one leg extended straight out.",
                        "With the other leg, bend the hip and knee to 90 degrees. You may brace your leg with your hands if necessary. This will be your starting position.",
                        "Extend your leg straight into the air, pausing briefly at the top. Return the leg to the starting position.",
                        "Repeat for 10-20 repetitions, and then switch to the other leg."
                    ],
                    "images": [
                        "90_90_Hamstring/0.jpg",
                        "90_90_Hamstring/1.jpg"
                    ],
                }
            ]
        }
    
    context = getDBExercisesContext()

    prompt = f"""
    You are a personal training assistant. Create a workout plan for me by making selections from  
    the following exercises:
     
     {context}

    that matches with the following preferences: 
    
    {user_input}

    Your response should be in valid JSON format and include 2 keys/ parts. The first is a few 
    sentance description of the plan descripbing the workout and why it fits my preferences. The 
    second part should be a list of exercise JSON objects that match my preferences and are exact 
    copies of one of the exercises provided above. Ensure the response contains sets, reps, instructions 
    as an array of strings, name, and images as an array. Include no other text before or after the JSON objects. Here is an example of what your response 
    should look like please ensure your response matches the pattern and order of elements in the 
    example:

    {sample_response}
    """  
    # Return the results as valid JSON which includes a few sentance description of the plan 
    # describing the workout and why it fits my preferences and a list of Exercise JSON objects 
    # that fit the my preferences. Include no text before or after the JSON object. Here is an 
    # example of what the JSON object should look like: 
    # {sample_response}
    # """

    message = create_message(prompt)

    try:
        response = generate_response(message)
        if not response:
            raise ValueError("The response from generate_response is empty.")
    except Exception as e:
        return {"error": f"Failed to generate workout: {e}"}
    
    # format LLM response to proper JSON format
    json_object = json.loads(response)

    return json_object

# Helper function to get database info
def getDBExercisesContext():
    try:
        exercises, column_names = retrieve_exercises()

        if not exercises:
            raise ValueError("No Exercises Found.")
    except Exception as e:
        return {"error": f"Retrieving Database Exercises Failed: {e}"}

    context = "Here are the exercises to use when creating the workout plan:\n"
    for exercise in exercises:
        exercise_details = []
        for i in range(len(column_names)):
            exercise_details.append(f"{column_names[i]}: {exercise[i]}")

        context += ", ".join(exercise_details) + "\n"
         
    return context
