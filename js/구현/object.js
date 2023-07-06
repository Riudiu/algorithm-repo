// 0bject(객체) - key(속성):value(값) 형태
// constructor(생성자) 방식
const user = new Object();
user.name = 'Riudiu';
user.age = 22;

console.log(user);  // {name: 'Riudiu', age: 22}

// function User() {
//     this.name = 'Jiwoo'
//     this.age = 47
// }
// const user = new User();

// 리터럴 방식
const user2 = {
    name: 'Jiwoo',
    age: 37,
    brother: user
}
console.log(user2);         // {name: 'Jiwoo', age: 37}
console.log(user2.name);    // Jiwoo  / '.' - 점 표기법
console.log(user2['age']);  // 37     / '['']' - 대괄호 표기법
console.log(user2.brother.name);  // Riudiu
