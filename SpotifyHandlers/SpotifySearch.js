const request = require('request');
const auth = require('./SpotifyAuth')

module.exports = {
    AlbumSearch: async function (searchParams){
        var token = await auth.getBearerAuthToken()
        console.log(token)
        searchParams.replace(" ","%20")
        var albumResults
        return new Promise(function(resolve, reject) {
        request.get( 
            options = {
                uri:'https://api.spotify.com/v1/search',
                headers:{Authorization:"Bearer "+token},
                qs:{
                    q:searchParams,
                    type:'album',
                    limit:10
                    },
                json:true
            }, (err, res, body) => {
            if (err) {  console.log(err); return reject(err); }
            albumResults = body
            resolve(albumResults) 
            });
        });
    }
};

