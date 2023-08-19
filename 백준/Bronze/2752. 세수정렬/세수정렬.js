const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

let arr = [];
for (let value of input) {
  arr.push(Number(value));
}

const sorted = arr.sort((a, b) => a - b);
console.log(...sorted);
