const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input.shift());

let arr = [];
for (let i = 0; i < N; i++) {
  const [age, name] = input[i].split(" ");
  arr.push([Number(age), name]);
}

let ans = "";
arr
  .sort((a, b) => a[0] - b[0])
  .forEach((e) => {
    ans += `${e[0]} ${e[1]}\n`;
  });
console.log(ans);
