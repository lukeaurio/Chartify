const request = require('request');
const fs = require('fs');
var rawdata = fs.readFileSync('config.json','utf8') 
var keys = JSON.parse(rawdata)



module.exports = {
    getBearerAuthToken: function(){
        var ret
         var auth = keys.clientId +':'+keys.clientSecret
        return new Promise(function(resolve, reject) { 
        request.post(
            options={
                uri:'https://accounts.spotify.com/api/token',
                headers:{
                    Authorization:'Basic '+ new Buffer.from(auth).toString('base64')
                },                 
                form:{grant_type:'client_credentials'},
                json:true
            },
            (err, res, body) => {
                if (err) {  console.log(err); return reject(err); }
                ret = "Bearer " + body.access_token
                resolve(ret)
            });
        });
    }
};