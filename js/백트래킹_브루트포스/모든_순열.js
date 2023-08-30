const input = require("fs").readFileSync("/dev/stdin").toString().trim();
const N = Number(input);

let visited = new Array(N + 1).fill(false);
let selected = [];
let result = "";

function dfs(depth) {
  if (depth == N) {
    result += `${selected.join(" ")}\n`;
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
