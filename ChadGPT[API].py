import openai
import tkinter as tk
from tkinter import scrolledtext

# Set up the API credentials for GPT-3.5 Turbo
openai.api_key = "YOUR_API_KEY"

# Create a function that generates the response using GPT-3.5 Turbo
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Check if the response is the example message
    if response.choices[0].finish_reason == "stop" and response.choices[0].text.strip() == 'Hello there, how may I assist you today?':
        return 'Hello there! How can I help you?'
    else:
        return response.choices[0].text.strip()

# Create a Tkinter window
window = tk.Tk()
window.title("ChatGPT Playground")
window.geometry("800x400")

# Create a left bar
left_bar = tk.Frame(window, width=150, bg="lightgray")
left_bar.pack(side=tk.LEFT, fill=tk.Y)

# Create a label for the left bar
label = tk.Label(left_bar, text="ChatGPT", font=("Arial", 20), bg="lightgray")
label.pack(side=tk.TOP, pady=10)

# Create a text box for the user to enter prompts
input_box = tk.Text(window, height=5, width=50, font=("Arial", 12))
input_box.pack(side=tk.TOP)

# Create a button to submit the prompt and generate a response
def generate_button_click():
    prompt = input_box.get("1.0", tk.END).strip()
    response = generate_response(prompt)
    output_box.insert(tk.END, "User: " + prompt + "\n")
    output_box.insert(tk.END, "ChatGPT: " + response + "\n\n")

generate_button = tk.Button(window, text="Generate", command=generate_button_click, font=("Arial", 12))
generate_button.pack(side=tk.TOP)

# Create a scrolled text box to display the conversation
output_box = scrolledtext.ScrolledText(window, height=15, width=70, font=("Arial", 12))
output_box.pack(side=tk.TOP)

# Start the Tkinter event loop
window.mainloop()
