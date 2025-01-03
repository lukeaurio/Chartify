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

To install all dependencies and set up the environment, run the following script:

    ./setup.sh

This script will set up `pyenv`, create a virtual environment, install the required packages from `requirements.txt`, and start the Flask application.

# Configuration

You'll need to make a [Spotify Developer Account][4] and [generate an application][5] in order to run Chartify. 

After doing so, fill out the 
    chartify.env.sample
file and rename it to the proper 
    chartify.env
or you could set them your environment variables in your bash profile but that'd be overkill. Right?

[4]: <https://developer.spotify.com/documentation/web-api> "The Documentation"
[5]: <https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token> "How to generate an application / get client_id and client secret"

# Firing it Up!

To run the app, it's as simple as setting environment variables like those in 
    chartify.env
and then calling

    flask run

To deactivate the virtual environment, use the following command:

    pyenv deactivate

# Containerized This time!

Or better yet you can run it via containers

    docker build -t <somerepo>/chartify:tag .
    docker run --name ChartifyAPI --env-file <./path_to_chartify.env> -d -p <available port>:5000 <somerepo>/chartify:tag 

# What if I'm scared of Command Lines?

Then there's a shell script! Simply call

    chmod +x ./build_and_run.sh
    ./build_and_run.sh <preferred_name_of_tag_or_leave_blank_for_latest>
It will perform the build, kill and remove the running container (if used before) and then run your new build!

And then to test one of the charting methods simply enter the following in your browser

http://localhost:5000/analysis/playlist/43M6s8VIc1duJg6MXDyXUV

So go ahead

Happy Hunting!