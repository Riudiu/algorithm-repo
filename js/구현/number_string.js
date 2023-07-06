// Int -> String
let a = "777";
let b = Number(a);
console.log(b);
console.log(typeof(b));

// String -> Int
let x = 777;
let y = String(a);
console.log(y);
console.log(typeof(y));

const number = 13;
const pi = .14;

console.log(number + undefined);          // NaN - not a number
console.log(typeof(number + undefined));  // number
console.log(pi);                          // 0.14

/* 부동 소수점 오류 -> 컴퓨터가 기본적으로 0과 1의 2진수를 사용해서 동작하기 때문.
   숫자를 표현할려면 10진수를 쓰는데 그랬을 때 컴퓨터는 10진수를 2진수로 바꾸는 작업을 한다.
   이때 간혹 무한 소수라는 개념이 발생하고, 이것을 무한한 것이 아닌 유한하게 표현하기 위해 
   세부적인 값에 초과나 혹은 손실로 계산 오류가 발생할 수 있다. */
const aaa = 0.1;
const bbb = 0.2;
console.log(aaa + bbb);                       // 0.30000000000000004
console.log(Number((aaa + bbb).toFixed(1)));  // 0.3     +) toFixed()는 기본적으로 string 타입을 반환