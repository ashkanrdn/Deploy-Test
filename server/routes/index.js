var express = require("express");
var router = express.Router();

const mongoose = require("mongoose");
const ControlsState = require("../models/ControlsStateModel");
/* GET home page. */
router.get("/", function(req, res) {
    res.render("index", { title: "Maintenance Dashboard " });
});

router.get("/schedule", function(req, res) {
    res.render("schedule", { title: "Express" });
});

router.get("/api", function(req, res) {
    ControlsState.find()
        .sort({ updatedAt: -1 })
        .limit(1)
        .then((result) => res.json(result));
});

module.exports = router;