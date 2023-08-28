const fs = require("fs");
const N = fs.readFileSync("/dev/stdin").toString().trim();
const arr = [];

for (let v of N) {
  arr.push(Number(v));
}
let ans = "";
arr
  .sort((a, b) => Number(b) - Number(a))
  .forEach((e) => {
    ans += String(e);
  });
console.log(ans);
