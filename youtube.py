from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(save_path)
        print("Download completed!")
    
    except Exception as e:
        print(e)
        print("Download failed!")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk() # create a root window
    root.withdraw() # hide the root window

    video_url = input("Enter the video url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Downloading...be patient!")
        download_video(video_url, save_dir)
    else:
        print("No folder selected!")