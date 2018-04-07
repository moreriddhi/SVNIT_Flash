var express = require('express')
var app = express()

app.get('/', function (req, res) {
	res.render('index');
})

app.listen(3000, function () {
	// body...
	console.log('App running on port 3000')
})

app.set('view engine', 'ejs')
