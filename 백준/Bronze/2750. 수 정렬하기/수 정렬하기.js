const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

input.shift();
const sorted = input.sort((a, b) => a - b);
for (let value of sorted) console.log(value);
