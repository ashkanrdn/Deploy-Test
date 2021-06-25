const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const controlSchema = new Schema({
    // Update Schema

    conTopic: { type: Number },
    conTitle: { type: String },
    conHost: { type: String },
    conDetails: { type: String },
    conLocation: { type: String },
    conDate: { type: String },
    conStart: { type: String },
    conEnd: { type: String }

}, { timestamps: true });

const ControlsState = mongoose.model('ControlsState', controlSchema);

module.exports = ControlsState;