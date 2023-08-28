const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const setArr = new Set(arr);

// 시간 초과 안 나게 sort와 map 활용
const sorted = [...setArr];
sorted.sort((a, b) => a - b);

const mapping = new Map();
sorted.filter((v, i) => {
  mapping.set(v, i);
});

let ans = "";
arr.forEach((e) => {
  const value = mapping.get(e);
  ans += `${value} `;
});
console.log(ans);
