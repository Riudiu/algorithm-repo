// 전개 연산자(Spread Operator)
let a = [1, 2, 3];
console.log(...a);  // 1, 2, 3

let b = [4, 5, 6];
let c = a.concat(b);
console.log(c);

let d = [...a, ...b];
console.log(d);


a = {x: 1, y: 2}
b = {x: 3, y: 4}
// b = {g: 3, h: 4}

c = Object.assign({}, a, b);  // 빈 객체 안에 a와 b를 합친다.
console.log(c);

d = {...a, ...b};
console.log(d);


function fn(x, y, z) {
    console.log(x, y, z);
}
fn(1, 2, 3);

a = [4, 5, 6];
fn(...a);