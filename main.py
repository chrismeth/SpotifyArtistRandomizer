import randomizer as r
import json
import os
import sys
import re


def authenticate_spotify(username):
    try:
        auth = r.SpotifyAuth(username)
        auth.wait_for_auth()
    except r.FailedAuth:
        print("Authentication failed")
        sys.exit()
    auth.stop_server()
    return auth


def lambda_handler(event, context):

    if os.environ["USER"]:
        username = os.environ["USER"]
    else:
        if len(sys.argv) > 1:
            username = sys.argv[1]
        else:
            username = input("Please type in your username: ")

    auth = authenticate_spotify(username)
    randomizer = r.SpotifyArtistRandomizer(username, auth.get_spotify())

    randomizer.top10_artist_tracks_playlist()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == "__main__":
    lambda_handler(None, None)
