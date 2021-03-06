This program creates a Spotify playlist from every followed artist's top 10 tracks.
It was inspired based on the SpotifyRandomizer (https://github.com/DanielsWrath/SpotifyRandomizer).

## Required packages

To use SpotifyRandomizer, you need [spotipy](https://github.com/plamere/spotipy).
You can install it using `pip`: `pip3 install spotipy`

## Setup

1. Create a spotify application so you can use `spotipy`. You can do this at the [Spotify developer website](https://developer.spotify.com/my-applications/).
2. Now you need to give the program your client ID & client secret. You can do this in 2 ways:
    1. Uncomment the lines in `randomizer.py` _(by removing the # in the beginning of the line)_ that set these variables and inputting yours.
       ```python
       os.environ["SPOTIPY_CLIENT_ID"] = "myclientid"
       os.environ["SPOTIPY_CLIENT_SECRET"] = "myclientsecret"
       ```
    2. Export those variables using your terminal. On windows:
    
       ```cmd
       SET SPOTIPY_CLIENT_ID=myclientid
       SET SPOTIPY_CLIENT_SECRET=myclientsecret
       ```
    
        On linux:
        ```bash
        export SPOTIPY_CLIENT_ID=myclientid
        export SPOTIPY_CLIENT_SECRET=myclientsecret
        ```
        
        You only need to do this once.
    
    The default redirect URL is `http://localhost:14523` for the local webserver.
3. Optionally, you can give the program the Spotify username. You can do this in 2 ways:
    1. In `randomizer.py`, set the following variable and inputting yours.
       ```python
       os.environ["USER"] = "myusername"
       ```
    2. Export that variable using your terminal. On windows:

       ```cmd
       SET USER=myusername
       ```

        On linux:
        ```bash
        export USER=myusername
        ```

        You only need to do this once.
4. You're done - you can basically change anything else you'd like.

## Run

The script can be ran by doing `python3 main.py`.
In this case the program will ask you for your username while running.
You can also give that information as an argument, like this `python3 main.py 1234567890`

When you run the program for the first time, it will open the spotify website for authorization. Then you need to copy the redirected URL into the commandline. After this, the program should work.

### Other

Also check out [the repo SpotifyNoDupes](https://github.com/stavlocker/spotifynodupes) if you want to get rid of your duplicate songs in playlists.
