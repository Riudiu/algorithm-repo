// 형 변환(Type Conversion)
// 가급적 === 일치 연산자를 사용해야 하는 이유

const a = 1;
const b = '1';

console.log(a === b);  // false
console.log(a == b);   // true

let c = 0;
let d = false;

console.log(c === d);  // false
console.log(c == d);   // true

c = true;
d = 1;

console.log(c === d);  // false
console.log(c == d);   // true

// === 일치
// ==  동등
