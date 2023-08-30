const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const T = Number(input[0]);
let N = 0;
let arr = [];

function dfs(result, depth) {
  // 현재 순열 처리(중복 순열)
  if (depth == N - 1) {
    let str = ""; // 현재 수식 문자열
    for (let i = 0; i < N - 1; i++) str += arr[i] + result[i];
    str += arr[N - 1] + "";
    current = eval(str.split(" ").join("")); // 공백을 제거한 뒤 수식 계산
    if (current == 0) console.log(str); // 수식의 결과가 0일 경우 출력
    return;
  }
  for (let x of [" ", "+", "-"]) {
    result.push(x);
    dfs(result, depth + 1);
    result.pop();
  }
}

for (let t = 1; t <= T; t++) {
  N = Number(input[t]);
  arr = [];
  for (let i = 1; i <= N; i++) arr.push(i);
  dfs([], 0);
  console.log();
}
