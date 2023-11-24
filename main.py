import customtkinter as ctk
import ffmpeg
from pytube import YouTube

videos = []
audios = []


def startDownload():
    return


def scanLink():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        streams = (
            ytObject.streams.filter(adaptive=True)
            .order_by("resolution")
            .desc()
        )
        for stream in streams:
            videos.append(stream)
        streams = ytObject.streams.filter(only_audio=True).order_by("abr").desc()
        for stream in streams:
            audios.append(stream)
        updateOptions()

    except:
        resetOptions()
        print("Invalid Link")

def resetArrays():
    videos.clear()
    audios.clear()

def updateOptions():
    tempvid = []
    tempaud = []
    for video in videos:
        tempvid.append("%s %s" % (video.resolution, video.mime_type))
    for audio in audios:
        tempaud.append(audio.abr)
    resolutionOptions.configure(values=tempvid, state="normal")
    resolutionOptions.set(tempvid[0])
    audioOptions.configure(values=tempaud, state="normal")
    audioOptions.set(tempaud[0])
    resetArrays()


def resetOptions():
    resolutionOptions.configure(values=[""], state="disabled")
    resolutionOptions.set("")
    audioOptions.configure(values=[""], state="disabled")
    audioOptions.set("")


def optionmenu_callback(choice):
    return


# System Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# App Frame
app = ctk.CTk()
app.geometry("500x400")
app.title("Youtube Downloader")
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure((1, 2), weight=1)

frame = ctk.CTkFrame(app, width=250)
frame.grid(row=0, column=0, rowspan=3, padx=0, pady=0, sticky="ns")

# Label
label = ctk.CTkLabel(
    app,
    text="Youtube Downloader",
    font=("TkDefaultFont", 18, "bold"),
    fg_color="#2b2b2b",
)
label.grid(row=0, column=0, padx=0, pady=0)

# Available downloads
resolutionOptions = ctk.CTkOptionMenu(
    app, values=[""], command=optionmenu_callback, bg_color="#2b2b2b", state="disabled"
)
resolutionOptions.grid(row=1, column=0, padx=10, pady=10, sticky="sew")

# Available downloads
audioOptions = ctk.CTkOptionMenu(
    app, values=[""], command=optionmenu_callback, bg_color="#2b2b2b", state="disabled"
)
audioOptions.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Link Input
url_var = "Insert link here..."
link = ctk.CTkEntry(app, placeholder_text=url_var)
link.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

# Scan button
scan = ctk.CTkButton(app, text="Scan", command=scanLink)
scan.grid(row=2, column=1, padx=10, pady=10, sticky="ew")


# Download Button
download = ctk.CTkButton(app, text="Download", command=startDownload)
download.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

# Run App
app.mainloop()
