// 최신 ES6 이상의 js 환경에서 사용 가능한 문법
// 한 줄로 2차원 배열 초기화 (4x5)
let arr = Array.from(Array(4), () => new Array(5));
console.log(arr);

// 반복문을 이용해 2차원 배열 초기화
let arr2 = new Array(3);
for (let i = 0; i < arr2.length; i++) {
    arr2[i] = Array.from({length: 4}, (undefined, j) => i * 4 + j);
}
console.log(arr2);