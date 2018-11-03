const request = require('request');
const fs = require('fs');
var rawdata = fs.readFileSync('config.json','utf8') 
var keys = JSON.parse(rawdata)

AppAuth = function(func){
    ret = ""
     var auth = keys.clientId +':'+keys.clientSecret
     
    request.post(
        options={
            uri:'https://accounts.spotify.com/api/token',
            headers:{
                Authorization:'Basic '+ new Buffer(auth).toString('base64')
            },                 
            form:{grant_type:'client_credentials'},
            json:true
        },
        (err, res, body) => {
            if (err) { return console.log(err); }
            console.log(body.access_token)
            ret = body.access_token
            func(token = ret)
        }
    )
}


searchResult = function(searchParams,token){
    searchParams.replace(" ","%20")
    request.get( 
        options = {
            uri:'https://api.spotify.com/v1/search',
            headers:{authorization:token},
            qs:{
                q:searchParams,
                type:'albums',
                limit:10
                },
            json:true
        }, (err, res, body) => {
        if (err) { return console.log(err); }
        console.log(body);
        return body
        })
    }

module.exports = {
    AlbumSearch: function(params){
        return params
    }
};

