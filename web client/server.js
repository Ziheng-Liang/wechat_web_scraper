var express = require('express');
var bodyParser = require('body-parser');
var app     = express();

//Note that in version 4 of express, express.bodyParser() was
//deprecated in favor of a separate 'body-parser' module.
app.use(bodyParser.urlencoded({ extended: true })); 

//app.use(express.bodyParser());


app.post('/ada', function(req, res) {
	//start.js
	var spawn = require('child_process').spawn,
	    py    = spawn('python', ['translate.py']),
	    // data = [1,2,3,4,5,6,7,8,9],
	    data = [req.body.title, req.body.author, getDateTime(), req.body.description]
	    resultString = '',
	    log = '';

	log += "The article's title: " + req.body.title + "<br>";
	log += "The author: " + req.body.author + "<br>";
	log += "The texts you enter: " + req.body.description + "<br>";

	py.stdout.on('data', function(data){
	  resultString += data.toString();
	});
	py.stdout.on('end', function(){
	  // console.log('Translated texts: ', resultString);
	  log += resultString;
	  res.send(log);
	});
	py.stdin.write(JSON.stringify(data));
	py.stdin.end();




});

app.listen(8080, function() {
  console.log('Server running at http://127.0.0.1:8080/');
});

/*
  Format current time to: "YYYY:MM:DD:HH:MM:SS".
 */
function getDateTime() {

    var date = new Date();

    var hour = date.getHours();
    hour = (hour < 10 ? "0" : "") + hour;

    var min  = date.getMinutes();
    min = (min < 10 ? "0" : "") + min;

    var sec  = date.getSeconds();
    sec = (sec < 10 ? "0" : "") + sec;

    var year = date.getFullYear();

    var month = date.getMonth() + 1;
    month = (month < 10 ? "0" : "") + month;

    var day  = date.getDate();
    day = (day < 10 ? "0" : "") + day;

    return year + ":" + month + ":" + day + ":" + hour + ":" + min + ":" + sec;

}