var express = require('express');
var path = require('path');
var routes = require('./routes/index');

// App setup
var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
// Static files
app.use(express.static(path.join(__dirname, 'public')));
// Routes setup
app.use('/', routes);



module.exports = app;