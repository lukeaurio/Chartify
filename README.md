
# Chartify
A simple app used to show the Emotional flow of albums and playlists
Based off of an Idea by RCharlie <https://www.rcharlie.com/post/fitter-happier/>

Will connect to Spotify and use Plotly in order to create and build charts
Can be used to graph and analyze albums, songs and (eventually) playlists 
for their emotional highs and lows for proper playlist development.
will eventually allow creation of playlists via Spotify's User API

Haven't figured out how to chart the data yet for super long playlists but that's a problem for later

Eventually it may do sentiment analysis using Lyric data but that's far off in the future

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
#  Configuration

you'll need to make a [Spotify Developer Account][4] and [generate an application][5] in order to run Chartify. 

After doing so, fill out the 
    chartify.env.sample
file and rename it to the proper 
    chartify.env
or you could set them your environment variables in your bash profile but that'd be overkill. Right?

[4]: <https://developer.spotify.com/documentation/web-api> "The Documentation"
[5]: <https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token> "How to generate an application / get client_id and client secret"

#  Firing it Up!

to run the app, it's as simple as setting environment variables like those in 
    chartify.env
and then calling

    flask run

#  Containerized This time!

or better yet you can run it via containers

    docker build -t <somerepo>/chartify:tag .
    docker run --name ChartifyAPI --env-file <./path_to_chartify.env> -d -p <available port>:5000 <somerepo>/chartify:tag 

#  What if I'm scared of Command Lines?

Then there's a shell script! simply call

    chmod +x ./build_and_run.sh
    ./build_and_run.sh <preferred_name_of_tag_or_leave_blank_for_latest>
It will perform the build, kill and remove the running container (if used before) and then run your new build!

and then to test one of the charting methods simply enter the following in your browser

http://localhost:5000/analysis/playlist/43M6s8VIc1duJg6MXDyXUV


So go ahead

Happy Hunting!