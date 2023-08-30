const fs = require("fs");
const input = fs
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split()
  .map(Number);

const N = input[0];
const arr = Array(267 * 10000)
  .fill()
  .map((v, i) => i + 1);

let i = 0;
let ans = 0;

for (const [i, value] of arr.entries()) {
  if (String(value).includes("666")) i++;
  if (N === i) {
    ans = value;
    break;
  }
}
console.log(ans);
