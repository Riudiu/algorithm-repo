const fs = require("fs");
const arr = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

arr.shift();
arr.sort((a, b) => {
  if (a.length === b.length) {
    if (a > b) return 1;
    else return -1;
  }
  return a.length - b.length;
});

const setArr = new Set(arr);
for (let v of setArr) {
  console.log(v);
}
