let stack = [];

stack.push(3);
stack.push(7);
stack.push(5);
console.log(stack);         // [3, 7, 5]
console.log(stack.pop());   // 5
console.log(stack);         // [3, 7]

stack.push(9);
stack.push(1);
stack.push(4); 
stack.pop();

let reversed = stack.slice().reverse();
console.log(reversed);      // [1, 9, 7, 3]
console.log(stack);         // [3, 7, 9, 1]