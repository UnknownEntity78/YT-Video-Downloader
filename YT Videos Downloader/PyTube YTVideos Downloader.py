
from pytube import YouTube
from sys import argv

#LINK HERE
link = 'https://www.youtube.com/watch?v=G5RpJwCJDqc&ab_channel=8KWorld'

yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE 
yd.download('C:/Users/vivaa/Desktop/')

#-----------------------------------------------------------------------------#
