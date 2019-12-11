import sys
import youtube_dl
import os

def youtube2mp3(url=None, save_folder="downloads"):

    if url == None:
        print("No URL detected! Please enter valid URL")
        exit()
    # just the way it is youtube link
    # url = "https://www.youtube.com/watch?v=WyYC9qRlJxY"
    # url = "https://www.youtube.com/watch?v=PivWY9wn5ps"
    options = {
      'format': 'bestaudio/best',
      'extractaudio' : True,  # only keep the audio
      'audioformat' : "mp3",  # convert to mp3 
      'outtmpl': save_folder + '/%(title)s.mp3',    # name the file the ID of the video
      'noplaylist' : True,    # only download single song, not playlist
    }

    import youtube_dl

    # download metadata
    ydl = youtube_dl.YoutubeDL(options)
    r = None

    with ydl:
        # don't download, much faster 
        r = ydl.extract_info(url, download=True)  
        title = r['title']
        artist = r['uploader']
        print("title = ", title, " by ", artist)
        # os.rename(r['title'], save_folder)
        print ("Downloaded and converted %s successfully!" % save_folder)

    # print some typical fields
    print ("%s uploaded by '%s', has %d views, %d likes, and %d dislikes" % (r['title'], r['uploader'], r['view_count'], r['like_count'], r['dislike_count']))

    output = save_folder + '/' + title + '.mp3'
    print("file saved to ", output)
    return output 

if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=PivWY9wn5ps"
    youtube2mp3(url=url)
