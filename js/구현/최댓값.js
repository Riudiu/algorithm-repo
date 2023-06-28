let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let arr = input.map(Number);
let ans = [arr[0], 0];
for (let i = 1; i < arr.length; i++) {
    if (ans[0] < arr[i]) {
        ans[0] = arr[i];
        ans[1] = i;
    }
}
console.log(ans[0]);
console.log(ans[1] + 1);