const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const N = Number(input);
let queens = [];

// 현재 놓인 퀸들의 위치와 비교해서 놓을 수 있는지 여부 확인
function possible(x, y) {
  for (let [a, b] of queens) {
    if (a == x || b == y) return false; // 행이나 열이 같은 경우
    if (Math.abs(a - x) == Math.abs(b - y)) return false; // 대각선에 위치하는 경우
  }
  return true;
}

let cnt = 0;
function dfs(row) {
  if (row == N) cnt += 1; // 퀸을 N개 배치할 수 있는 경우 카운트
  for (let i = 0; i < N; i++) {
    if (!possible(row, i)) continue; // 현재 위치에 놓을 수 없다면 무시
    queens.push([row, i]); // 현재 위치에 퀸 놓기
    dfs(row + 1);
    queens.pop(); // 현재 위치에서 퀸 제거
  }
}
dfs(0);
console.log(cnt);
