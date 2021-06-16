const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const controlSchema = new Schema({


    conTopic: { type: String, required: true },
    conTitle: { type: String, required: true },
    conHost: { type: String, required: true },
    conDetails: { type: String, required: true },
    conLocation: { type: String, required: true },
    conDate: { type: String, required: true },
    conStart: { type: String, required: true },
    conEnd: { type: String, required: true },
    conImgURL: {
        type: String,
        default: 'https://www.signalconnect.com/wp-content/uploads/2018/02/DIRECTV-for-Fast-Food-Restaurants.jpg'
    }

});

const Controlsdb = mongoose.model('Controlsdb', controlSchema);

module.exports = Controlsdb;