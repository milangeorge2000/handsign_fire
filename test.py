import os
import speech_recognition as sr
from PIL import Image, ImageTk
import tkinter as tk

# Initialize the recognizer
r = sr.Recognizer()

# Create a Tkinter window
root = tk.Tk()
root.title("Image Viewer")

# Create a label for the image
image_label = tk.Label(root)

# Define the directory and image path dictionary
directory_dict = {'baby': 'baby', 'brother': 'brother', 'bont_Like': 'bont_Like', 'like': 'like',
'help': 'help', 'house': 'house', 'more': 'more', 'pay': 'pay', 'stop': 'stop', 
'yes': 'yes', 'fan on': 'fan on', 'fan off': 'fan off', 'light on': 'light on', 'light off': 'light off'}

# Continuously listen to the user input and display images
while True:
    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    # Convert speech to text
    try:
        text = r.recognize_google(audio)
        print(f"Converted text: {text}")
        
        # Get the directory and image path based on the recognized text
        directory = directory_dict.get(text.lower())
        if directory is None:
            raise ValueError(f"No directory found for recognized text '{text}'")
        image_path = os.path.join(directory, "image.jpg")
        
        # Display the image of the folder
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
        image_label.pack()
        
    except (sr.UnknownValueError, ValueError) as e:
        print(f"Error: {e}")
    except sr.RequestError as e:
        print("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))
    
    # Update the Tkinter window
    root.update()
    
    # Wait for user to press 'q' to exit the program
    if input("Press 'q' to quit or any key to continue: ").lower() == 'q':
        break

# Close the Tkinter window
root.destroy()
