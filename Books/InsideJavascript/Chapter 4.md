# 4. 함수와 프로토타입 체이닝

함수 정의
-----

* 함수 선언문
* 함수 표현식
* Function() 생성자 함수

함수 선언문은 function 키워드로 바로 조지는거, 이건 변수에 할당 안해줌
```javascript
function add(a, b) {
  return a + b; 
}

console.log(add(1, 3)) // 4
```

함수 표현식은 function으로 선언하고 변수에 할당, 호이스팅 막으려고 이 방식 쓴다
```javascript
const add = function(a, b) {
  return a + b;
}
console.log(add(1, 3)) // 4
```

#### 주의
함수 표현식에서는 함수 선언문과 같이 쓰면 에러가 발생할 수 있습니다.
```javascript
const add = function sum(a,b) {
  return a + b;
}

console.log(add(1,3)) // 4
console.log(sum(1,3)) // uncaught referenceError: sum is not defined
```
=> 함수 표현식에서 사용된 함수의 이름이 외부 코드에서는 접근이 안되요.


Function() 생성자 함수
```javascript
const add = new Function('x', 'y', 'return x + y');
console.log(add(1,3))
```

일반적으로 잘 쓰지 않는다.

함수 호이스팅 
------

함수 선언문 형태로 이용하면 호이스팅이 되버려서 위에서 접근이 가능해요.
이렇게 되면 나중에 같은 이름의 함수를 재선언하면 값이 이상해지겠죠
```javascript
add(1,3) // 4

function add(a,b) {
  return a + b;
}

add(1, 2) //3 
```

```javascript
add(2,3) // 6

function add (a, b) {
  return a + b;
}

function add (a,b) {
  return a * b; 
}

add(4,5) // 20
```

그래서 함수 표현식을 사용합니다
```javascript
add(1,3) // Uncaught ReferenceError: add is not defined

const add = function (a,b) {
  return a + b;
}
```

함수 객체: 함수도 객체다 
=======

자바스크립트에서 객체라는 것은 키와 밸류, 즉 프로퍼티를 가질수 있다.
```javascript
function add(a,b) {
  return a + b;
}

add.result = 5;
add.status = 'ok';

console.log(add.result) // 5
console.log(add.status) // ok
```

함수는 값으로 취급된다
-----

함수는 
* 리터럴에 의해 생성
* 변수나 배열의 요소, 객체의 프로퍼티 등에 할당 가능
* 함수의 인자로 전달 가능 (ex. 콜백함수)
* 함수의 리턴값으로 전달 가능 (ex. 함수 리턴 가능)
* 동적으로 프로퍼티를 생성 및 할당 가능 (ex. 느닷없이 add.subway 해버리기)

위의 특징들을 종합하여 자바스크립트 에서의 함수는 -> **일급객체**

=> 일급객체 라는 것은 변수에 할당이 가능해야 하고, 인자로 전달이 가능해야 하며, 리턴값으로 전달이 되어야 합니다. 이 세개가 충족하면 일급 객체라고 우리는 부릅니다.


```javascript
// 변수에 할당
const add = function (a, b) {
  return a + b;
}

// 함수의 인자로 전달
const mul = function (a) {
  return  a * a;
}

const foo = function(a, callback) {
  return callback(a);
}

console.log(foo(2, mul))

// 결과값으로 리턴

const bar = function() {
  return function () {
    console.log("return function")
  }
}

console.log(bar())

```

함수 객체의 프로토타입 확인하기
```javascript
function myFunction () { 
  return true;
}

console.log(myFuncton.prototype) // Object
console.log(myFuncton.prototype.constructor)
```

함수의 다양한 형태
-----

* 콜백 함수
```javascript
window.onload = function() {
  console.log("window loaded")
}
```
* 즉시 실행 함수
```javascript
(function() {
  console.log("test")
})()

(function(name) {
  console.log(`myname is ${name}`)
})('foo')
```
* 내부 함수
  
```javascript
function parent() {
  var a = 100;
  var b = 300;

  function child () {
    var b = 400;

    console.log(a)
    console.log(b)
  }
  child()
}

parent() // 100, 400
child() // child is not defined
```

* 함수를 리턴하는 함수
```javascript
function parent() {
  var a = 100;
  var b = 200;

  return function() {
    return a + b;
  }
}

const add = parent()
add()
```

함수 호출과 this
-----

* arguments 객체