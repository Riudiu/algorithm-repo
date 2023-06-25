let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let N = Number(input[0]);
let arr = input[1].split(' ')
let str = arr[0];

let ans = 0;
for (let i = 0; i < N; i++) {
    ans += Number(str[i]);
}

console.log(ans);