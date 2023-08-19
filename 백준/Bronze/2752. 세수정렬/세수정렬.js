const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const arr = input[0].split(" ").map(Number);
const sorted = arr.sort((a, b) => a - b);
console.log(...sorted);
