const [N, M] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let visited = new Array(N + 1).fill(false); // 각 원소 인덱스별 방문 여부
let selected = []; // 현재 순열에 포함된 원소

let result = "";
//순열
function dfs(depth) {
  if (depth == M) {
    result += `${selected.join(" ")}\n`; // array.join() - 배열의 모든 요소를 연결해 하나의 문자열로 생성
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (visited[i]) continue; // 중복 방지, 이미 처리된 원소 무시

    visited[i] = true; // 현재 원소 방문 처리
    selected.push(i); // 현재 원소 선택
    dfs(depth + 1);

    selected.pop();
    visited[i] = false;
  }
}

dfs(0);
console.log(result);
