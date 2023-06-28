let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

if (input.includes('')) console.log(input.length - 1);
else console.log(input.length);