// 직접 값을 설정하여 초기화
let arr = [8, 1, 4, 5, 7];

// 길이가 5이고, 모든 원소의 값이 0인 배열 초기화
let arr2 = new Array(5).fill(0);
let arr3 = new Array(5).fill(false);

console.log(arr);
console.log(arr2);
console.log(arr3);

// concat() - 여러 개의 배열을 이어 붙여서 합친 결과를 반환 / O(N)
let arr4 = [1, 2, 3, 4, 5];
let arr5 = [6, 7, 8, 9, 10];
arr = arr4.concat(arr5, [11, 12], [13]);
console.log(arr);

// slice(left, right) - 특정 구간의 원소를 꺼낸 배열을 반환 / O(N)
arr = [1, 2, 3, 4, 5];
let result = arr.slice(2, 4);  // [3, 4]
console.log(result);

// indexOf() - 특정한 값을 가지는 원소의 첫째 인덱스 반환, 해당하는 원소가 없는 경우 -1 반환 / O(N)
arr = [7, 3, 5, 6, 6, 2, 1];
console.log(arr.indexOf(5));  // 2
console.log(arr.indexOf(6));  // 3
console.log(arr.indexOf(8));  // -1