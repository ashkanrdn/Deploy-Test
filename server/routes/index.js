var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
    res.render('index', { title: 'Maintenance Dashboard ' });
});

router.get('/schedule', function(req, res) {
    res.render('schedule', { title: 'Express' });
});


module.exports = router;