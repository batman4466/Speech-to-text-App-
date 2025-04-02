import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyaudio
# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def convert_speech_to_text():
    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...")
            root.update()
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            status_label.config(text="Processing...")
            root.update()
            text = recognizer.recognize_google(audio)
            text_area.insert(tk.END, text + "\n")
            status_label.config(text="Speech Converted Successfully!")
    except sr.UnknownValueError:
        status_label.config(text="Could not understand the audio. Try again.")
    except sr.RequestError:
        status_label.config(text="Error: Speech service unavailable.")

# Function to clear text area
def clear_text():
    text_area.delete('1.0', tk.END)

# Create GUI window
root = tk.Tk()
root.title("Speech-to-Text Converter")
root.geometry("500x400")
root.config(bg="lightblue")

# Create buttons and labels
title_label = tk.Label(root, text="Speech-to-Text Converter", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

status_label = tk.Label(root, text="Press 'Start Recording' to begin", font=("Arial", 12), bg="lightblue")
status_label.pack(pady=5)

start_button = tk.Button(root, text="🎙 Start Recording", font=("Arial", 12), command=convert_speech_to_text)
start_button.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, width=50, height=10, font=("Arial", 12))
text_area.pack(pady=10)

clear_button = tk.Button(root, text="🗑 Clear Text", font=("Arial", 12), command=clear_text)
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="❌ Exit", font=("Arial", 12), command=root.quit)
exit_button.pack(pady=10)

# Run the app
root.mainloop()
