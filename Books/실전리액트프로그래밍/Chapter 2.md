# 2. ES6+를 품은 자바스크립트, 매력적인 언어가 되다.

### 2.1 변수를 정의하는 새로운 방법: Const, let

##### 2.1.1 var가 가진 문제
* 함수 스코프
```javascript
function example() {
  var i = 0;
}
console.log(i) // i is undefined error
```

```javascript
for(var i = 0; i < 10; i++) {
  console.log(i);
}
console.log(i) // 10
```

* 호이스팅
  * var로 정의된 변수는 함수 최상단으로 끌어올려 진다.
  * 변수에 값의 할당을 나중에 해도 그전에 사용이 가능하고 undefined가 떠버린다

##### 2.1.2 const, let
```javascript
  let foo = 'bar1';
  console.log(foo); // bar1
  if (true) {
    let foo = 'bar2';
    console.log(foo); // bar2
  }
  console.log(foo) // bar1
```

* const, let 으로 선언한 변수들도 호이스팅이 된다. 하지만 TDZ(Temporal Dead Zone)에 존재하기 때문에 사용하면 참조 에러 발생
  
const,let 이 호이스팅 되는 이유
```javascript
const foo = 'foo';
{
  console.log(foo); // 참조 에러
  const foo = 2;
}
```

위의 예시에서 블록 내의 foo가 호이스팅 되지 않았더라면 console은 블록 밖의 foo를 출력해야 맞지만 
블록 내의 foo 변수가 호이스팅 되고 TDZ에 존재하기 때문에 console.log 는 에러가 발생

아래는 var에서의 호이스팅 효과
```javascript
var foo = 1;
(function() {
  console.log(foo); // undefined
  var foo = 2;
})();
```

* const로 정의해도 객체 내부의 속성값은 수정 가능함
```javascript
const bar = { prop1: 'a' };
bar.prop1 = 'b';
bar.prop2 = 123;
console.log(bar); // {prop1: 'b', prop2: 123}
const arr = [10, 20]
arr[0] = 100
arr.push(300);
console.log(arr) // [100, 20, 300]
```

* 전개 연산자를 활용하여 할당하면 원래의 값에 영향을 주지 않는다
```javascript
const arr1 = [1,2,3];
const obj1 = {age: 23, name: 'mike'};
const arr2 = [...arr1];
const obj2 = {...obj1}
arr2.push(4);
obj2.age = 80;
```

* 배열 비구조화에서의 기본값
```javascript
const arr = [1];
const [ a = 10, b = 20] = arr
constol.log(a) // 1
constol.log(b) // 20
```

* 배열 비구조화를 통한 값의 교환
```javascript
let a = 1;
let b = 2;
[a,b] = [b,a];
console.log(a) // 2
console.log(b) // 1
```

* 객체 비구조화에서 별칭 사용하기
```javascript
const obj1 = {age: 20, name: 'mike'};
const {age: theAge, name} = obj1
console.log(theAge) // 20
console.log(name) // 'mike'
```

* 매개변수 기본값
```javascript
function printLog(a = 1) {
  console.log({ a })
}
printLog(); { a: 1} 
```

* 나머지 매개변수를 사용한 코드
```javascript
function printLog(a, ...rest) {
  console.log({a, rest})
}
printLog(1,2,3) // {a: 1, reset: [2,3]}
```

##### 2.3.2 함수를 정의하는 새로운 방법: 화살표 함수
```javascript
const add = (a,b) => a + b;
console.log(add(1,2)) // 3
const add5 = a => a + 5;
console.log(add5(5)) // 10
const addAndReturnObject = (a,b) => ({ result: a + b})
console.log(addAndReturnObject(1,2)) // {result: 3}
```

```javascript
const printLog = (...rest) => console.log(rest);
printLog(1, 2) // [1,2]
```

* this와 arguments가 바인딩되지 않는 화살표 함수

원래 버그 발생하는 상황
```javascript
const obj = {
  value: 1,
  increase: function() {
    this.value++;
  },
};
obj.increase();
console.log(obj.value) // 2
const increase = obj.increase;
increase();
console.log(obj.value) // 2
```

생성자 함수 내부에서 정의된 화살표 함수의 this
```javascript
function Something(){
  this.value = 1;
  this.increase = () => this.value++;
}
const obj = new Something();
obj.increase();
console.log(obj.value) // 2
const increase = obj.increase;
increase();
console.log(obj.value) // 3
```

* setInterval 함수를 사용할 때의 화살표 함수 사용
```javascript
function Something() {
  this.value = 1;
  setInterval(function increase() {
    this.value++;
  }, 1000)
}

const obj = new Something(); // value는 그대로 1, setInterval내의 this가 window를 참조
```

```javascript
function Something() {
  this.value = 1;
  setInterval(() => {
    this.value++;
  }, 1000)
}
const obj = new Somenthing() // value는 2
```

### 프로미스
* 프로미스의 세가지 상태 (pending, fulfilled, rejected)

프로미스를 생성하는 세가지 방법
```javascript
const p1 = new Promise((resolve, reject) => {
  //...
})
const p2 = new Promise.reject('error message');
const p3 = new Promise.resolve(param)
```

* Promise.resolve의 반환값
=> Promise객체(상태: fulfilled) 반환함
```javascript
const p1 = Promise.resolve(123);
console.log(p1) // Promise { <fulfilled>: 123}
console.log(p1 !== 123) // true
const p2 = new Promise(resolve => setTimeout(() => resolve(10) ,1));
console.log(Promise.resolve(p2) === p2) // true
```

```javascript
requestData()
  .then(data => {

  })
  .catch(error => {

  })
  .finally(() => {

  })
```

### 2.4.2 프로미스 활용하기

##### 병렬로 처리하기 : Promise.all
비동기 함수 간에 서로 의존성이 없다면 병렬로 처리하는 게 더 빠르다

Promise.all에 파라미터로 promise객체를 담은 배열이 들어감
Promise들 전부 결과 받아와야 then 호출
```javascript
requestData1().then(data => console.log(data))
requestData2().then(data => console.log(data))

Promise.all([requestData1(), requestData2()]).then(([data1, data2]) => {
  console.log(data1, data2)
})
```

##### 가장 빨리 처리된 프로미스 가져오기 : Promise.race
여러개중 가장 빨리 결과값 가져온 친구의 결과값 반환

```javascript
Promise.race([
  requestData(),
  new Promise((_, reject) => setTimeout(reject, 3000))
])
.then(data => console.log(data))
.catch(error => console.log(error))
```


### async, await

async await 함수는 프로미스를 반환한다
```javascript
async function getData() {
  return 123;
}
getData().then(data => console.log(data)); //123
```


* async, await 함수를 병렬로 사용해보자~~
  
await을 나중에 할당하면 병렬로 실행!! (이건 외우자, 나중에 쓸모 있을듯)
```javascript
async function getData() {
  const p1 = asyncFunc1();
  const p2 = asyncFunc2();
  const data1 = await p1;
  const data2 = await p2;
}
```
Promise.all 활용
```javascript
async function getData() {
  const [data1, data2] = await Promise.all([asyncFunc1(), asyncFunc2()]);
}
```

##### 실행을 멈출 수 있는 제너레이터