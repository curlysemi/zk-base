let formatter = require('./formatter.js');
let fs = require('fs');
let path = require('path');
const filename = 'proof.json'

module.exports = function() {
    let file = fs.readFileSync(path.resolve(__dirname, filename));
    let proof = JSON.parse(file.toString());
    return formatter(proof);
}
