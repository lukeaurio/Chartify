
# Chartify
A simple app used to show the Emotional flow of albums and playlists
Based off of an Idea by RCharlie <https://www.rcharlie.com/post/fitter-happier/>

Will connect to Spotify and use Plotly in order to create and build charts
Can be used to graph and analyze albums, songs and (eventually) playlists 
for their emotional highs and lows for proper playlist development.
will eventually allow creation of playlists via Spotify's User API

Eventually it may do sentiment anaalysis using Lyric data but that's far of in the future

# Dependencies

to install all dependencies run the following command
install [Python 3.10.4][1], [VSCode][2] and the [python extension for VSCode][3] for easy debug.

[1]: <https://www.python.org/downloads/release/python-3104/> "python.org"
[2]: <https://code.visualstudio.com/Download> "or VSCodium if you're an open source fanatic"
[3]: <https://marketplace.visualstudio.com/items?itemName=ms-python.python> "I mean this one is in the marketplace but why not have it as a link"

`***Warning! (If you want to use WSL / linux It'll take like an hour but I'd be glad to give you some links on how to do and configure it to work with VPNs)***`

    pip install pip-system-certs spotipy flask plotly lyricsgenius

optionally you can use pandas dataframes really easily with plotly. Try with all thy might

as well make sure the following command is run in all terminals 

    set CURL_CA_BUNDLE="" python

#  Firing it Up!

to run the app, it's as simple as

    flask run

#  Containerized This time!

or better yet you can run it via containers

    docker build -t <somerepo>/chartify:tag .
    docker run --name spotipy -t -d -p <available port>:5000 <somerepo>/chartify:tag

and then to test one of the charting methods simply enter the following in your browser

http://localhost:5000/analysis/playlist/2YOvQj60ovUoJCsYxO7wzN



So go ahead

Happy Hunting!