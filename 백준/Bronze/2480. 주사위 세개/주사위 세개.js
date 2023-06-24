let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let [A, B, C] = input.map(Number);

if (A === B && B == C) console.log(10000 + A * 1000);
else if (A === B) console.log(ans = 1000 + A * 100);
else if (B === C) console.log(ans = 1000 + B * 100);
else if (A === C) console.log(ans = 1000 + C * 100);
else {
    M = Math.max(A, B, C);
    console.log(M * 100);
}