// 병합 정렬 (Merge Sort)
// 병합 정렬은 전형적인 분할 정복 알고리즘이다.
// 시간 복잡도 O(N log N)을 보장하는 빠른 정렬 알고리즘 중 하나이다.

// 분할 정복(Divide and Conquer)
// 1. 분할(divide) : 큰 문제를 작은 부분 문제(쉬운 문제)로 분할한다.
// 2. 정복(conquer) : 작은 부분 문제를 각각 해결한다.
// 3. 조합(combine) : 해결한 부분 문제들의 답을 이용하여 다시 큰 문제를 해결한다.
// 분할 정복은 일반적으로 재귀 함수를 이용해 구현하지만, 오버헤드의 위험이 있다.

// 병합 정렬에서 각 부분 배열은 이미 정렬된 상태로 본다.
// 병합시 각 부분 배열에 대하여 첫째 원소부터 시작하여 하나씩 확인한다.

function merge(left, right) {
  let result = [];
  while (left.length && right.length) {
    if (left[0] <= right[0]) {
      // 두 배열의 첫 원소를 비교하여
      result.push(left.shift()); // 더 작은 수를 결과에 넣음
    } else {
      result.push(right.shift()); // 오른쪽도 마찬가지
    }
  }
  while (left.length) result.push(left.shift()); // 어느 한 배열이 더 많이 남았다면 나머지를 다 넣음
  while (right.length) result.push(right.shift()); // 오른쪽도 마찬가지
  return result;
}

function mergeSort(array) {
  if (array.length < 2) return array; // 원소가 하나일 때는 그대로 내보냅니다.
  let pivot = Math.floor(array.length / 2); // 대략 반으로 쪼개는 코드
  let left = array.slice(0, pivot); // 쪼갠 왼쪽
  let right = array.slice(pivot, array.length); // 쪼갠 오른쪽
  return merge(mergeSort(left), mergeSort(right)); // 재귀적으로 쪼개고 합칩니다.
}

const arr = [1, 100, 50, 250, 35, 80, 99];
const sorted = mergeSort(arr);
console.log(sorted);
