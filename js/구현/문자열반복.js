let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = Number(input[0]);
for (let i = 1; i <= T; i++) {
    let [R, S] = input[i].split(' ');
    let P = "";
    for (let s of S) {
        P += s.repeat(Number(R));
    }
    console.log(P);
}