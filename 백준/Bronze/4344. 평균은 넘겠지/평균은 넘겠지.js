let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

// 전체 점수 더하기 -> 그중에 평균점수 구하기 -> 평균점수 넘는 비율 구하기
function rateOfOverAverrage(arr, n) {
    let sum = arr.reduce((a, b) => a + b) - n;
    let averrage_score = parseInt(sum / n);
    let over_averrage = 0;
    for (let i = 1; i <= arr.length; i++) {
        if (arr[i] > averrage_score) over_averrage += 1;
    }
    let rate = (over_averrage / n) * 100;
    return rate.toFixed(3);
}

C = Number(input[0]);
for (let i = 1; i <= C; i++) {
    let arr = input[i].split(' ').map(Number);
    let N = arr[0];
    console.log(rateOfOverAverrage(arr, N) + '%');
}