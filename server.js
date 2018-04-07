var express = require('express');
var path = require('path');
var app = express();
var mongoose = require("mongoose");
var cors = require('cors');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var routes = require('./routes/index');
var narmad = require('./routes/narmad');

app.listen(3000, function () {
	// body...
	console.log('App running on port 3000')
})

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs')

app.use('/', routes);
app.use('/narmad', narmad);

// database
var schemaName = new Schema({
	firstName : String,
	lastName : String,
	registration_number : String,
	toDate : {type: Date},
	fromDate : {type: Date},
	firstName : String,
	no_persons: {type: Number, min: 0},
	person_name: String,
	person_age: Number,

},{
	collection: 'collectionName'
});

var Model = mongoose.model('Model', schemaName);
mongoose.connect('mongodb://localhost:27017/dbName');

app.post('/narmad', function(req, res) {
	var savedata = new Model({
		'request': query,
		'time': Math.floor(Date.now() / 1000) // Time of save the data in unix timestamp format
	}).save(function(err, result) {
		if (err) throw err;

		if(result) {
			res.json(result)
		}
	})
})

app.get('/find/:query', cors(), function(req, res) {
	var query = req.params.query;

	Model.find({
		'request': query
	}, function(err, result) {
		if (err) throw err;
		if (result) {
			res.json(result)
		} else {
			res.send(JSON.stringify({
				error : 'Error'
			}))
		}
	})
})

if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

/// catch 404 and forwarding to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});
