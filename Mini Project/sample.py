import speech_recognition as sr
import tkinter as tk

def speech_to_text(text_box):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Recognizing...")

        try:
            text = recognizer.recognize_google(audio)
            print("You said: {}".format(text))
            text_box.insert(tk.END, "You said: {}\n".format(text))
        except sr.UnknownValueError:
            print("Could not understand audio")
            text_box.insert(tk.END, "Could not understand audio\n")
        except sr.RequestError as e:
            print("Error with the speech recognition service; {0}".format(e))
            text_box.insert(tk.END, "Error with the speech recognition service; {0}\n".format(e))

def on_mic_button_click(text_box):
    speech_to_text(text_box)

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Speech to Text")

    # Create a button to trigger speech recognition
    mic_button = tk.Button(root, text="Start Microphone", command=lambda: on_mic_button_click(text_box))
    mic_button.pack(pady=20)

    # Create a text box to display output
    text_box = tk.Text(root, height=10, width=40)
    text_box.pack()

    # Run the Tkinter event loop
root.mainloop()