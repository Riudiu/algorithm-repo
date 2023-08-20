// readline 모듈보다는 fs(file system module)를 이용해 파일 전체를 읽어 들여 처리하기
const fs = require("fs");

// 하나의 값을 입력받을 때
const input = fs.readFileSync("/dev/stdin").toString().trim();

// 공백으로 구분된 한 줄의 값들을 입력받을 때
// const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

// 여러 줄의 값들을 입력받을 때
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = fs.readFileSync('input.txt').toString().trim().split('\n');
console.log(input);
