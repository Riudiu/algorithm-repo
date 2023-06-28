let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let H = Number(input[0]);
let M = Number(input[1]);

M -= 45;
if (M < 0) {
    M += 60;
    H -= 1;
    if (H < 0) H += 24;
}
console.log(H, M);