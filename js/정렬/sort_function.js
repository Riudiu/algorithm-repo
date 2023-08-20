// JavaScript에서는 배열에 포함된 데이터를 정렬하는 sort() 함수를 제공한다.
// 최악의 경우 시간 복잡도 O(N log N)을 보장한다.
// 알고리즘 문제를 풀 때 정렬 기능이 필요하면, 단순히 sort() 함수를 사용하는 것을 권장한다.
// 만약 사용이 제한된다면, 병합 정렬과 같은 알고리즘을 직접 구현하자.

// JavaScript의 정렬 함수에서는 정렬 기준 함수가 사용된다. 이것을 통해 내림차순, 오름차순 등 구체적인 정렬 기준을 설정할 수 있다.
// 그리고 정렬 기준 함수를 사용하지 않으면, 각 원소는 문자열로 취급된다. 즉 유니코드 값 순서대로 정렬된다.
// 따라서, 항상 정렬 기준 함수를 명시하는 습관을 들일 필요가 있다.

// 두 개의 원소 a, b 입력 예시
// 반환 값이 0보다 작은 경우 -> a가 우선순위가 높아, 앞에 위치
// 반환 값이 0보다 큰 경우 -> b가 우선순위가 높아, 앞에 위치
// 반환 값이 0인 경우 -> a와 b의 순서를 변경하지 않는다

let arr = [1, 8, 5, 9, 21, 3, 32, 7, 2, 15];

/// 오름차순
function compareAscending(a, b) {
  return a - b;
}
// 곧바로 적용할 수도 있다
// arr.sort(function(a, b) {
//     return a - b;
// });

arr.sort(compareAscending);
console.log(arr); // [1, 2, 3, 5, 7, 8, 9, 15, 21, 32]

arr = [1, 8, 5, 9, 21, 3, 32, 7, 2, 15];

/// 내림차순
function compareDescending(a, b) {
  return b - a;
}

arr.sort(compareDescending);
console.log(arr); // [32, 21, 15, 9, 8, 7, 5, 3, 2, 1]

arr = ["fineapple", "banana", "durian", "apple", "carrot"];

/// 문자열 오름차순, 별도의 비교 함수를 사용하지 않으면 유니코드 순으로 정렬되므로 간단히 함수없이 문자열 정렬 수행 가능
arr.sort();
console.log(arr); // ['apple', 'banana', 'carrot', 'durian', 'fineapple']

arr = ["fineapple", "banana", "durian", "apple", "carrot"];

/// 문자열 내림차순
function compareDescending_string(a, b) {
  if (a > b) return -1;
  else if (a < b) return 1;
  else return 0;
}

arr.sort(compareDescending_string);
console.log(arr); // ['fineapple', 'durian', 'carrot', 'banana', 'apple']

arr = [
  { name: "홍길동", score: 90 },
  { name: "고영희", score: 85 },
  { name: "강아진", score: 97 },
];

/// 점수 내림차순
function compareDescending_score(a, b) {
  return b.store - a.score;
}

arr.sort(compareDescending_score);
console.log(arr);
