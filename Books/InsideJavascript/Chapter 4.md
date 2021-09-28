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

```javascript
function func(arg1, arg2) {
  console.log(arg1, arg2);
}

func() // undefinded undefined
func(1) // 1 undefined
```

위 예시의 특성때문에 자바스크립트에서는 런타임시에 호출된 인자의 개수를 확인해야합니다.  
이를 가능케 하는게 **arguments 객체**다

arguments 객체는 **유사 배열 객체**이다

```javascript
  const add = function(a,b) {
    console.dir(arguments);
    return a + b;
  }
```

arguments는 객체지만 배열은 아니다. => length 프로퍼티가 있어서 배열과 유사하게 동작하지만, 배열은 아니므로 배열 메서드를 에러가 발생합니다. 그래서 이러한 유사배열객체들을 사용할때는 call과 apply 메서드를 이용한 this 바인딩을 이용하는데 나중에 알아보자   

* this는 자신을 호출한 객체에 바인딩 된다.   
`a.sayName()` this는 a    
`b.sayName()` this는 b   

내부 함수에서 this를 이용하여 호출할때 this를 바인딩 해주지 않으면 this는 전역객체를 가리키므로 주의해야 한다.
```javascript
var value = 100;

var myObject = {
  value: 1,
  func1: function() {
    this.value += 1;
    console.log('func1() called. this.value : ' + this.value);

    func2 = function() {
      this.value += 1;
      console.log('func2() called. this.value : ' + this.value);

      func3 = function () {
        this.value += 1;
        console.log('func3() called. this.value : ' + this.value)
      }

      func3();
    }
    func2();
  }
};

myObject.func1(); // 2, 101, 102
```
위 코드의 해결책 => 명시적 this 바인딩

```javascript
var value = 100;

var myObject = {
  value: 1,
  func1: function() {
    var that = this;
    that.value += 1;
    console.log('func1() called. this.value : ' + this.value);

    func2 = function() {
      that.value += 1;
      console.log('func2() called. this.value : ' + that.value);

      func3 = function () {
        that.value += 1;
        console.log('func3() called. this.value : ' + that.value)
      }

      func3();
    }
    func2();
  }
};

myObject.func1(); // 2, 3, 4
```

생성자 함수 에서의 this 바인딩 => 빈 객체를 가리킴
```javascript
function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

const foo = new Person('foo', 2, 'man')
```

call과 apply 메서드를 이용한 명시적인 this 바인딩 
---

```javascript
function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

var foo = {}
Person.apply(foo, [1, 2, 3])
console.dir(foo)
```

apply에서 처음으로 넘긴 인자가 this로 바인딩되고 두번째 인자가 파라미터로 전달된다.  
`Person.call(foo, 'foo', 30, 'man')`   
apply나 call이나 this 바인딩 하는건 비슷하고 유사배열객체에 this 바인딩 할때 주로 사용한다.   

```javascript
function myFunction() {
  console.dir(arguments)

  // arguments.shift() => 에러 발생  -> arguments는 유사배열객체 이지 배열이 아니다. 배열의 메서드를 쓰면 에러 발생
  var args = Array.prototype.slice.apply(arguments);
  console.dif(args);
}

myFunction(1,2,3)
```

자바스크립트 함수는 항상 리턴값을 반환한다
------

* 리턴값 따로 지정안하면 undefined 값 리턴
* 생성자 함수에서 리턴값 지정 안하면 생성된 객체 리턴
```javascript
function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;

  return 100;
}

var foo = new Person('foo', 30, 'man');
console.log(foo)
```

=> 생성자 함수에서 return을 기본타입으로 주면 this로 바인딩된 객체가 리턴된다(신기)   

프로토타입 체이닝
------

아래 그림만 이해하면 된다

![image](https://user-images.githubusercontent.com/72545732/135125211-b154c81c-6db8-4300-9b40-2904328e78fc.png)


```javascript
function Person(name) {
  this.name = name;
}

var foo = new Person('foo');
console.dir(Person)
console.dir(foo);
```

메서드가 호출되었을때 자신내부의 프로퍼티면 그냥 호출되고  
만약에 없으면 프로토타입의 메서드가 있으면 출력 없으면 다시 프로토타입 타고 간다  
최종적으로 없을때 undefined method 출력   