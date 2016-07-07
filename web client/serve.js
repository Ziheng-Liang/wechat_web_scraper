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
	    data = req.body.description
	    dataString = '';

	py.stdout.on('data', function(data){
	  dataString += data.toString();
	});
	py.stdout.on('end', function(){
	  console.log('Sum of numbers=',dataString);
	});
	py.stdin.write(JSON.stringify(data));
	py.stdin.end();

  res.send('You sent the name "' + req.body.name + '". ' + req.body.description + " " + dataString);
});

app.listen(8080, function() {
  console.log('Server running at http://127.0.0.1:8080/');
});