# importing Libraries
from pytube import YouTube, Playlist
import time

# Simple function to be used to show that video dowloaded
def finish():
    print('Video Downloaded')


while True:
    # getting input from the user
    inp = input("Link: ")
    
    # exitting when pressing enter or writing done
    if inp.lower() == 'done' or len(inp) < 1 : break
    
    # different input types 
    type_link = input('Enter:\n 1 for Video\n 2 for Playlist\n 3 for Audio\n 4 for Audio Playlist\n')
    
    # Getting output path from the user if pressing enter putting it in the default directory
    output_path = input('Enter Your Directory Path: ').strip()
    
    # Default directory you can chamge it if you like
    if len(output_path) < 1: output_path = 'D:\Courses'    
    
    # downloading a video
    if int(type_link) == 1:
        yt = YouTube(inp)
        
        # printing video tiltle & thumnail url
        print(yt.title) 
        print(yt.thumbnail_url)
        
        # trying to download the video first, with 720p 
        #if not getting the highest resolution
        try:
            #'Default resolution is 720p you can chamge it if you like'
            yt.streams.filter(progressive=True, res='720p').first().download(output_path=output_path)
            # printing video downloaded when finished
            yt.register_on_complete_callback(finish()) 
            
        except:
            # trying to get the highest resolution
            yt.streams.get_highest_resolution().download(output_path=output_path)
            yt.register_on_complete_callback(finish())
    
    # downloading a playlist
    elif int(type_link) == 2:
        p = Playlist(inp)
        # printing play list name
        print(p.title)
        
        # Allowing the user to chose a video to start downloading at by entering its index
        num_playlist_start = input('Enter the number of the video to start at or press Enter for All \n')
        
        # if the user pressed enter, start downloading from the first one
        if len(num_playlist_start) < 1:
            x = 0
        else:
            x = int(num_playlist_start) - 1   
        '''
        - Downloading each video in the default quality 720p if not grtting the highest one.
        - All the playlist videos will be added to a new folder that has the playlist name.
        - Each downloaded video wil be named with the index of video followed by its name.
        which make the downloaded videos in the right order.
        - After each video is downloaded, a message print out on the screen with the video name and its index.
        - Adding a sleep for 5 sec after each video, to avoid connection problems.
                '''
        # looping through the playlist
        for video in list(p.videos)[x:]:
            try:
                x+=1
                # downloading the file
                video.streams.filter(progressive=True, res='720p').first().download(
                    output_path= f"{output_path}\\{p.title.replace('|', '')}",
                    filename='{} {}'.format(x, video.title))
                # finished message
                video.register_on_complete_callback(finish())
                print(x)
                print(video.title)
                # sleeping for connection problems
                time.sleep(5)
                
            except:
                try:
                    # downloading the file
                    video.streams.get_highest_resolution().download(
                        output_path= f"{output_path}\\{p.title.replace('|', '')}",
                        filename='{} {}'.format(x, video.title))
                    # finished message                    
                    video.register_on_complete_callback(finish())
                    print(x)
                    print(video.title)
                    # sleeping for connection problems
                    time.sleep(5)
                    
                except:
                    # if failed, continue with the next video
                    continue
                    
    # downloading a Video as an Audio
    elif int(type_link) == 3:
        yt = YouTube(inp)
        # printing video tiltle
        print(yt.title)
        
        # downloading as mp4 128kbs
        yt.streams.filter(only_audio=True, mime_type="audio/mp4", abr="128kbps").first().download(
            output_path=output_path)
        # printing video downloaded when finished
        yt.register_on_complete_callback(finish())
    
    # downloading a playlist as audio
    elif int(type_link) == 4:
        p = Playlist(inp)
        #printing play list name
        print(p.title)
        '''
        - Downloading each video as an audio (mp4 128kbs).
        - All the playlist videos will be added to a new folder that has the playlist name.
        - Each downloaded video wil be named with the index of video followed by its name.
        which make the downloaded videos in the right order.
        - After each video is downloaded, a message print out on the screen with the video name and its index.
        - Adding a sleep for 5 sec after each video, to avoid connection problems.
                '''

        # Allowing the user to chose a video to start downloading at by entering its index
        num_playlist_start = input('Enter the number of the video to start at or press Enter for All \n')
        # if the user pressed enter, start downloading from the first one
        if len(num_playlist_start) < 1:
            x = 0
        else:
            x = int(num_playlist_start) - 1
            
        # looping through the playlist    
        for video in list(p.videos)[x:]:
            x+=1
            # downloading the file
            video.streams.filter(only_audio=True, mime_type="audio/mp4", abr="128kbps").first().download(
                output_path=f"{output_path}\\{p.title}", filename='{} {}'.format(x, video.title))
            # finished message
            video.register_on_complete_callback(finish())
            print(x)
            print(video.title)
            # sleeping for connection problems
            time.sleep(5)
    break