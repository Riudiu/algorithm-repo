let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

console.log(input[0] * input[1][2]);
console.log(input[0] * input[1][1]);
console.log(input[0] * input[1][0]);
console.log(input[0] * input[1]);