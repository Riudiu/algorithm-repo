let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = Number(input[0]);
let cnt = 0;
for (let i = 1; i <= N; i++) {
    let str = input[i];
    let tmp = "";
    for (let s of str) {
        //이전에 문자가 등장했으면서, 연속적이지 않으면 그룹 단어가 아니기에 중단
        if (tmp.includes(s) && tmp[tmp.length - 1] !== s) 
            break;
        else 
            tmp += s;
    }
    if (str === tmp) cnt += 1;
}
console.log(cnt);