var express = require('express');
var router = express.Router();

router.get('/', function(req, res) {
  res.render('narmad');
});

module.exports = router;