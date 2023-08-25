const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = input.map(Number)[0];
const arr = [];
let ans = "";

for (let i = 1; i <= N; i++) {
  const nums = input[i].split(" ").map(Number);
  arr.push(nums);
}

arr
  .sort((a, b) => {
    if (a[0] !== b[0]) {
      return a[0] - b[0];
    }
    return a[1] - b[1];
  })
  .forEach((value) => (ans += `${value[0]} ${value[1]}\n`));

console.log(ans);
