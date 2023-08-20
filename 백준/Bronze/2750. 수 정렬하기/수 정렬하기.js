const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

input.shift();
const sorted = input.sort((a, b) => a - b);

let ans = "";
for (let value of sorted) ans += value + "\n";
console.log(ans);
