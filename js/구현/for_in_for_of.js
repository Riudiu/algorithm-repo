/// for in, for of 반복문

const user = {
    name: 'jiwoo',
    age: 34,
    isValid: true,
    email: "danny0170@naver.com"
}

for (let key in user) {
    console.log(key);  // name, age, isValid, email
}

console.log('----------------');

for (let key in user) {
    console.log(user[key]);   // jiwoo, 34, true, danny0170@naver.com
}

console.log('----------------');
console.log('----------------');

const nums = [1, 3, 5, 6];

for (let value of nums) {
    console.log(value);   // 1, 3, 5, 6
}

console.log('----------------');

for (let key in nums) {
    console.log(key);   // 0, 1, 2, 3
}

console.log('----------------');

for (let key in nums) {
    console.log(nums[key]);  // 1, 3, 5, 6
}