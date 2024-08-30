import time
import random

# Mock vector database to simulate emergency responses
emergency_db = {
    "patient not breathing": "Perform CPR immediately. Place your hands on the chest and push down hard, 2 inches deep, at a rate of 100-120 compressions per minute. Give rescue breaths every 30 compressions.",
    "severe bleeding": "Apply direct pressure to the wound using a clean cloth. Elevate the injured area if possible. Keep applying pressure until the bleeding stops or help arrives.",
    # Add more emergencies and steps as needed
}

# Function to simulate database query with delay
def query_emergency_db(emergency):
    print("I am checking what you should do immediately...")
    time.sleep(15)  # Simulate delay
    return emergency_db.get(emergency.lower(), None)

# Main AI Receptionist function
def ai_receptionist():
    print("Hello! Are you experiencing an emergency, or would you like to leave a message?")
    
    user_input = input().strip().lower()
    
    if "emergency" in user_input:
        print("What is the emergency?")
        emergency = input().strip().lower()
        
        # Start the simulated database lookup
        emergency_response = query_emergency_db(emergency)
        
        # Continue the conversation while waiting for the lookup
        print("Meanwhile, can you tell me which area are you located right now?")
        location = input().strip()
        
        # Random estimated time of arrival
        eta = random.randint(5, 15)
        print(f"Dr. Adrin will be coming to your location immediately. Estimated time of arrival: {eta} minutes.")
        
        if emergency_response:
            # If the user is worried about the time
            print("If the arrival time is too late, please follow these steps:")
            print(emergency_response)
        else:
            # If no match is found in the database
            print("I'm sorry, I don't have specific instructions for that emergency. Please try to keep the patient stable while the doctor arrives.")
        
    elif "message" in user_input:
        print("Please leave your message for Dr. Adrin:")
        message = input().strip()
        print("Thanks for the message, we will forward it to Dr. Adrin.")
    
    else:
        print("I don’t understand that. Could you please clarify if it's an emergency or if you'd like to leave a message?")
        ai_receptionist()  # Restart the process if input is unclear

# Start the AI receptionist
ai_receptionist()

