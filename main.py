import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment

def process_audio_files(input_folder):
    # Create a unique output folder inside the selected folder
    output_folder = os.path.join(input_folder, "Processed_Audio_Files")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each .wav file in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            file_path = os.path.join(input_folder, filename)
            audio = AudioSegment.from_wav(file_path)

            # Splitting the audio into 30-second segments
            for i in range(0, len(audio), 30000):  # 30000 milliseconds = 30 seconds
                segment = audio[i:i+30000]
                segment_filename = f"{os.path.splitext(filename)[0]}_part_{i//30000}.wav"
                segment_path = os.path.join(output_folder, segment_filename)
                segment.export(segment_path, format="wav")

def select_folder():
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()  # Show the folder selection dialog
    if folder_selected:
        process_audio_files(folder_selected)

# Setting up the tkinter GUI
root = tk.Tk()
root.title("WAV File Splitter")
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=20)
root.mainloop()
