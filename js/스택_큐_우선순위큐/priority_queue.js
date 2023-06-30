/*
  Javascript는 기본적으로 우선순위 큐를 라이브러리로 제공하지 않는다.
  https://github.com/ndb796/priorityqueuejs
  위 저장소에서 index.js 소스 코드를 가져온 뒤에 다음과 같이 사용할 수 있다.
*/

let pq = new PriorityQueue(function(a, b) {
    return
});

pq.enq({cash: 250, name: 'Jiwoo Yun'});
pq.enq({cash: 300, name: 'Danny Yun'});
pq.enq({cash: 150, name: 'Kwangmin Choi'});
console.lof(pq.size());
console.lof(pq.deq());
console.lof(pq.peek());
console.lof(pq.size());