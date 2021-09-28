# 3. 자바스크립트 데이터 타입과 연산자

자바스크립트의 데이터 타입  
<img src="https://user-images.githubusercontent.com/50283326/134811500-9999f34b-ecfb-46a6-87ea-89cec6a4e8e4.png" style="width: 70%"/>

자바스크립트 기본 타입
---------------

* null은 object 타입이다

```javascript

var intNum = 10
var floatNum = 0.1

var singleQuoteStr = 'single quote string'
var doubleQuoteStr = "double quote string"
var singleChar = 'a'

var boolVar = true

// undefined
var emptyVar

var nullVar = null

console.log(
  typeof intNum // number
  typeof floatNum // number
  typeof singleQuoteStr // string
  typeof doubleQuoteStr // string
  typeof singleChar // string
  typeof boolVar // boolean
  typeof emptyVar // undefined
  typeof nullVar // object
)

```

숫자
----
자바스크립트는 하나의 숫자형만 존재  
전부 다 number

null과 undefined
---
*undefined*는 타입이자, 값을 나타낸다.
*null*의 타입은 object (null이 아니다.) 


객체
---

객체 리터럴 방식으로 객체 생성
```javascript
var foo = {
  name: 'foo',
  age: 30,
  gender: 'male',
}
```

for in 문을 통한 객체 프로퍼티 출력
```javascript
var foo = {
  name: 'foo',
  age: 30,
  gender: 'male',
}

var prop;
for (prop in foo) {
  console.log(prop, foo[prop])
}
```

참조 타입의 특성 
======
자바 스크립트에서는 기본타입을 제외한 모든 값은 객체다.  
배열, 함수, 정규표현식은 모두 객체다.  
이들을 참조 타입이라고 부르는 이유는 실제 값이 아닌 참조값으로 처리되기 때문이다.

```javascript
var objA = {
  val: 40
}

var objB = objA;
console.log(objB.val) // 40
objB.val = 50;
console.log(objA.val) // 50
```

objA는 val가 포함된 객체의 주소를 가리킨다.  
objB = objA는 objB가 objA가 바라보던 주소를 바라보게 하는 것이다  
같은 주소의 값을 변경해 버리면 이후에 해당 주솟값을 호출하면 값은 당연히 바뀌어 있다.  
이걸 방지하기 위해서 깊은복사를 해야하는데  
`JSON.parse(JSON.stringify(objA))`를 나는 좋아한다.

<img src="https://user-images.githubusercontent.com/50283326/134812112-3f0ce113-55e4-4203-89c1-414eae0f1c23.png" style="width: 70%"/>

객체 비교
----

(==)를 쓰게되면 참조값을 비교하게 된다.
(===)를 써야 제대로된 일치 비교가 가능하다.


프로토타입 
===

자바스크립트의 모든 객체는 자신의 부모 역할을 하는 객체와 연결되어 있다.  
이러한 부모 객체를 **프로토타입 객체** 라고 부른다

생성된 객체에서 메소드를 호출했는데 해당 메소드가 존재하지 않으면 프로토타입의 메서드를 호출하게 된다.  
이는 책의 나중에 나온다

배열 
===

```javascript

var arr = [0, 1, 2]

arr.push(3);
console.log(arr) // [0, 1, 2, 3]

arr.length = 5;
console.log(arr) // [0, 1, 2, 3, undefined]

arr.push(4)
console.log(arr) // [0, 1, 2, 3, undefined, 4]
```

배열 요소 삭제
---
```javascript
  var arr = [0, 1, 2, 3]

  arr.splice(2, 1) // 배열의 두번째 요소부터 1개를 삭제한다.
  console.log(arr) // 0, 1, 3
```


유사 배열 객체
----

length 프로퍼티를 가지고 있는 객체를 유사 배열 객체라 한다.
```javascript
var arr = ['bar'];
var obj = {
  name: 'foo',
  length: 1
};

arr.push('baz');
console.log(arr) // 'bar', 'baz'
obj.push('baz') // error  push는 Array객체의 메서드 이다


var arr = ['bar'];
var obj = {
  name: 'foo',
  length: 1,
}

arr.push('baz');
console.log(arr)

Array.prototype.push.apply(obj, ['baz']);
console.log(obj) // { '1': 'baz', name: 'foo', length: 2}
```

apply()메서드를 사용하면 객체지만 표준 배열 메서드를 사용하는 것이 가능하다.  
이건 4장에서 나옴

==(동등) 연산자와 ===(일치) 연산자
=======

```javascript
console.log('1' == 1) // true
console.log('1' === 1) // false
```

동등 연산자는 참조 주소의 값이 동등한지만 비교
일치 연산자는 타입까지 체크해준다!!!


!!연산자
=====

!!의 역할은 피연산자를 boolean 값으로 변환하는 것이다

```javascript
console.log(!!0) // false
console.log(!!1) // true
console.log(!!'string') // true
console.log(!!'') // false  틀림
console.log(!!true) // true
console.log(!!false) // false
console.log(!!null) // false 틀림
console.log(!!undefined) // false
console.log(!!{}) // true
console.log(!![1,2,3]) // true
```