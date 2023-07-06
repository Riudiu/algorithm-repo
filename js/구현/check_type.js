/// 데이터 타입 확인

console.log(typeof 'Hello' === 'string');
console.log(typeof 123 === 'number');
console.log(typeof false === 'boolean');
console.log(typeof undefined === 'undefined');
console.log(typeof null === 'object');
console.log(typeof [] === 'object');
console.log(typeof {} === 'object');

console.log([].constructor === Array);
console.log({}.constructor === Object);

console.log(Object.prototype.toString.call(null).slice(8, -1) == "Null");


function checkType(data) {
    return Object.prototype.toString.call(data).slice(8, -1);
}
console.log(checkType(null));
console.log(checkType([]));
console.log(checkType({}));

console.log(checkType('string'));
console.log(checkType(123));
console.log(checkType(false));
console.log(checkType(undefined));
console.log(checkType(function () {}));
