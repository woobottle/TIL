const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const first = +input[0];
const second = +input[1];
console.log(first + second)