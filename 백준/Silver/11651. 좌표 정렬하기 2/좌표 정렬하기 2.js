const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input.shift());

let arr = [];
for (let i = 0; i < N; i++) {
  const nums = input[i].split(" ").map(Number);
  arr.push(nums);
}

let ans = "";
arr
  .sort((a, b) => {
    if (a[1] !== b[1]) return a[1] - b[1];
    return a[0] - b[0];
  })
  .forEach((value) => {
    ans += `${value[0]} ${value[1]}\n`;
  });
console.log(ans);
