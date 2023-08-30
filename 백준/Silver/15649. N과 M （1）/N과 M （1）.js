const [N, M] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let visited = new Array(N + 1).fill(false);
let selected = [];

let result = "";
function dfs(depth) {
  if (depth == M) {
    result += `${selected.join(" ")}\n`; // array.join() - 배열의 모든 요소를 연결해 하나의 문자열로 생성
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (visited[i]) continue;

    visited[i] = true;
    selected.push(i);
    dfs(depth + 1);

    selected.pop();
    visited[i] = false;
  }
}

dfs(0);
console.log(result);
