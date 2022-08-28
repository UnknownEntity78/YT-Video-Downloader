
from pytube import YouTube
from sys import argv

print("Instant Downloader v2.0")
print("made by DevBoii")
print("link to youtube channel -> https://www.youtube.com/channel/UCbEchd6vaPxIhlBXEeeRZiA")


link = input("Link:")
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE 
yd.download('C:/Users/vivaa/Desktop/')

#-----------------------------------------------------------------------------#