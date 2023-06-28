let set = new Set();

set.add(3);
set.add(5);
set.add(7);
set.add(3);

console.log(`개수 : ${set.size}`);
console.log(`7 포함 여부 : ${set.has(7)}`);

set.delete(5);
console.log(`5 포함 여부 : ${set.has(5)}`);

// 원소 하나씩 출력
for (let item of set) console.log(item); 
