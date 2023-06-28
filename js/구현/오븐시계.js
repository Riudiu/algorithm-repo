let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let [A, B] = input[0].split(' ').map(Number);
let C = Number(input[1]);

B += C;
if (B > 59) {
    h = parseInt(B / 60);
    B %= 60;
    A += h;
    if (A > 23) A -= 24;
}
console.log(A, B);