let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let [A, B] = input;

let tmp = "";
for (let i = A.length - 1; i >= 0; i--) {
    tmp += A[i];
}
A = Number(tmp);
tmp = "";
for (let i = B.length - 1; i >= 0; i--) {
    tmp += B[i];
}
B = Number(tmp);

if(A > B) console.log(A);
else console.log(B);