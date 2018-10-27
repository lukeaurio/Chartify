const express = require('express')
const bodyParser = require('body-parser');
const charts = require('chartjs');
const app = express()
app.use(express.static('public'))
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs')

app.get('/index.html',function (req,res){
    res.render('index')
})

app.post('/index.html',function (req,res){
    console.log(req.body.searchdata);
    res.render('index');
  })

app.get('/', function (req, res) {
  res.render('index')
})

app.post('/',function (req,res){
  console.log(req.body.searchdata);
  res.render('index');
})

app.get('/dashboard', function (req, res) {
  res.render('dashboard')
})

app.post('/dashboard',function (req,res){
  console.log(req.body.searchdata);
  res.render('dashboard');
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})