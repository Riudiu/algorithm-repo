const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const setArr = new Set(arr);

// 시간 초과 안 나게 sort와 map 활용(정렬(sort) -> O(NlogN) / 해시테이블(map) -> O(1))
const sorted = [...setArr];
sorted.sort((a, b) => a - b); // 위에서 중복값 없앤 다음 오름차순 정렬

const mapping = new Map();
sorted.filter((v, i) => {
  mapping.set(v, i); // 좌표의 값이 key, 인덱스가 곧 value가 될 수 있다
});

let ans = "";
arr.forEach((e) => {
  const value = mapping.get(e);
  ans += `${value} `;
});
console.log(ans);
