const request = require('request');
const auth = require('./SpotifyAuth')

async function _getAllTracks(page){
    
}
async function _getNextTrack(page){
    var token = await auth.getBearerAuthToken()
    var page
    if(page.next){
    return new Promise(function(resolve, reject) {
        request.get( 
            options = {
                uri:page.next,
                headers:{Authorization:token},
                json:true
            }, (err, res, body) => {
            if (err) {  console.log(err); return reject(err); }
            pageResult = body
            resolve(pageResult) 
            });
        }
    }
}

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