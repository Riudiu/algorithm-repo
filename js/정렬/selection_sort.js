// 선택 정렬 (Selection Sort)
// 가장 작은 것을 선택해서 앞으로 보내는 정렬 기법, 앞으로 보내진 원소는 더 이상 위치가 변경되지 않는다.
function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let minIndex = i; // 가장 작은 원소의 인덱스
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[minIndex] > arr[j]) {
        minIndex = j;
      }
    }
    // swap
    let temp = arr[i];
    arr[i] = arr[minIndex];
    arr[minIndex] = temp;
  }
}

let arr = [68, 883, 1, 5, 10, 499, 52, 909, 6, 8];
selectionSort(arr);
console.log(arr);
