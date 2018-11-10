const request = require('request');
const auth = require('./SpotifyAuth')

module.exports = {
    GetAlbum: async function (AlbumID){
        var token = await auth.getBearerAuthToken()
        var albumResult
        return new Promise(function(resolve, reject) {
        request.get( 
            options = {
                uri:'https://api.spotify.com/v1/albums/',
                headers:{Authorization:token},
                qs:{
                    id:AlbumID
                    },
                json:true
            }, (err, res, body) => {
            if (err) {  console.log(err); return reject(err); }
            albumResult = body
            resolve(albumResult) 
            });
        });
    }
};