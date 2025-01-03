if [[ -z "$1"  ]];
then tag="chartify:latest";
else tag=$(echo chartify:$1);
fi
echo $(docker build -t $tag .)
echo $(docker kill ChartifyAPI_Test)
echo $(docker rm ChartifyAPI_Test)
echo $(docker run --name ChartifyAPI_Test --restart unless-stopped --env-file ./chartify.env -d -p 5000:5000 $tag)