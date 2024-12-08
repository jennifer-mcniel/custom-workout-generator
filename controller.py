import workoutsDB



def generate_workout(user_input):
    prompt = f"Create a workout plan for a person with the following preferences: {user_input}"
    
    
    
    
    
    
    
    sample_response = [
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
            }
        ]
    return sample_response
