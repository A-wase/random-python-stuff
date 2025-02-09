import tkinter as tk
from tkinter import filedialog
import pygame
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x300")
        
        # Initialise pygame mixer
        pygame.init()
        mixer.init()
        
        # Create GUI elements
        self.create_widgets()
        
        # Player state variables
        self.paused = False
        self.stopped = False

    def create_widgets(self):
        # Playlist listbox
        self.playlist = tk.Listbox(self.root, bg="black", fg="white", width=60)
        self.playlist.pack(pady=20)

        # Control buttons frame
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        # Add Song button
        add_btn = tk.Button(control_frame, text="Add Song", command=self.add_song)
        add_btn.grid(row=0, column=0, padx=10)

        # Play button
        play_btn = tk.Button(control_frame, text="Play", command=self.play_song)
        play_btn.grid(row=0, column=1, padx=10)

        # Pause button
        pause_btn = tk.Button(control_frame, text="Pause", command=self.pause_song)
        pause_btn.grid(row=0, column=2, padx=10)

        # Stop button
        stop_btn = tk.Button(control_frame, text="Stop", command=self.stop_song)
        stop_btn.grid(row=0, column=3, padx=10)

        # Volume control
        volume_label = tk.Label(self.root, text="Volume")
        volume_label.pack(pady=5)
        self.volume_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.1, 
                                    orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(0.5)
        self.volume_slider.pack()

    def add_song(self):
        songs = filedialog.askopenfilenames(
            title="Select Songs",
            filetypes=(("MP3 Files", "*.mp3"), ("WAV Files", "*.wav"))
        )
        for song in songs:
            self.playlist.insert(tk.END, song)

    def play_song(self):
        selected_song = self.playlist.get(tk.ACTIVE)
        if not selected_song:
            return
            
        if self.stopped or self.paused:
            mixer.music.load(selected_song)
            mixer.music.play()
            self.stopped = False
            self.paused = False
        else:
            mixer.music.unpause()

    def pause_song(self):
        if not self.paused:
            mixer.music.pause()
            self.paused = True
        else:
            mixer.music.unpause()
            self.paused = False

    def stop_song(self):
        mixer.music.stop()
        self.stopped = True

    def set_volume(self, val):
        volume = float(val)
        mixer.music.set_volume(volume)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()