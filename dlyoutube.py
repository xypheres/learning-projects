from pytube import YouTube
from sys import argv
from moviepy.editor import VideoFileClip, AudioFileClip

link = argv[1]
yt = YouTube(link)
filepath = "J:\yt vids"

yvf = yt.streams.filter(adaptive=True)
yv = yt.streams.get_by_itag(137)
ya = yt.streams.get_audio_only()

yv.download(filepath,filename="VID"+yt.title+".mp4")
ya.download(filepath,filename="AUD"+yt.title+".mp4")

audioonly = AudioFileClip(filepath+"\\"+"AUD"+yt.title+".mp4")
vidonly = VideoFileClip(filepath+"\\"+"VID"+yt.title+".mp4")

combinedvid = vidonly.set_audio(audioonly)
combinedvid.write_videofile(filepath+"\\"+yt.title+".mp4",codec='libx264')