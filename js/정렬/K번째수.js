const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

[N, K] = input[0].split(" ").map(Number);
let arr = input[1].split(" ").map(Number);
arr.sort((a, b) => a - b);
console.log(arr[K - 1]);
