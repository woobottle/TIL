# 7. 클래스

* 자바스크립트는 프로토타입 기반 언어 => 상속 개념 없음
* es6에서 클래스 문법 추가 (일부는 프로토타입을 활용하고 있음)

### 7.1 클래스와 인스턴스의 개념 이해

인스턴스 => 어떤 클래스의 실존하는 개체!!   
`const Seulgi = new Person('seulgi')`


### 7.2 자바스크립트의 클래스

```js
var Rectangle = function (width, height) {
  this.width = width;
  this.height = height;
}

Rectangle.prototype.getArea = function () {
  return this.width * this.height;
}

Rectangle.isRectangle = function (instance) {
  return instance instanceof Rectange && 
    instance.width > 0 && instance.height > 0;
}

var rect1 = new Rectangle(3,4)
console.log(rect1.getArea()); // 12
console.log(rect1.isRectangle(rect1)) // error
console.log(Rectangle.isRectangle(rect1)) // true
```

isRectangle은 Rectangle의 스태틱 메소드임!

### 7.3 클래스 상속

```js
var Grade = function () {
  var args = Array.prototype.slice.call(arguments);
  for (var i = 0; i < args.length; i++) {
    this[i] = args[i]
  }
  this.length = args.length;
}

Grade.prototype = [];
var g = new Grade(100, 80)
```

위의 예제는 두가지 문제점을 가지고 있다.
1. length 프로퍼티가 삭제가 가능하다 `delete g.length`
2. Grade의 프로토타입에 빈 배열이 할당 되었다.

```js
g.push(90)
console.log(g) // { 0: 100, 1: 80, 2: 90, length: 3}

delete g.length
g.push(70)
conolse.log(g) // { 0: 70, 1: 80, 2: 90, length: 1}
```

=> 내장 객체인 Array 에서는 length가 삭제가 불가능함(configurable 속성이 false이다)

```js
Grade.prototype = ['a', 'b', 'c', 'd']
var g = new Grade(100, 80)

g.push(90) 
console.log(g) // { 0: 100, 1: 80, 2: 90, length: 3}

delete g.length
g.push(70)
console.log(g)  // { 0: 100, 1: 80, 2: 90, _ , 4: 70 length: 5}
```

=> 클래스에 있는 값이 인스턴스에 영향을 미치면 안된다!!

* 7.3.2 클래스가 구체적인 데이터를 지니지 않게 하는 방법

1. 프로퍼티들을 일일이 지우고 더는 새로운 프로퍼티를 추가할 수 없게 하는 것
```js
delete Square.protype.width;
delete Square.protype.height;
Object.freeze(Square.prototype);
```
2. 중간에 빈 생성자 함수를 끼어버리는것
더글라스 크락포드(js 창시자)가 고안해낸 방법
```js
var Rectangle = function(width, height) {
  this.width = width;
  this.height = height;
}

Rectangle.prototype.getArea = function () {
  return this.width * this.height;
}

var Square = function (width) {
  Rectangle.call(this, width, width);
}

var Bridge = function () {};
Bridge.prototype = Rectangle.prototype;
Square.prototype = new Bridge();
Object.freeze(Square.prototype)
```


### 4. es6의 클래스 및 클래스 상속

es5와 es6의 클래스 문법 비교
```js
var es5 = function(name) {
  this.name = name;
}
es5.staticMethod = function() { 
  return this.name + " staticMethod";
}
es5.prototype.method = function() {
  return this.name + 'method';
}
var es5Instance = new es5('es5');
console.log(es5Instance.staticeMethod())
console.log(es5Instance.method())

var es6 = class {
  constructor(name) {
    this.name = name;
  }
  static staticMethod () {
    return this.name + " staticMethod";
  }
  method(){ // 자동으로 prototype 객체 내부에 할당되는 메서드
    return this.name + ' method';
  }
};
var es6Instance = new es6('es6');
console.log(es6Instance.staticMethod());
console.log(es6Instance.method());
```

es6의 클래스 상속
```js
var Rectangle = class {
  constructor (width, height) {
    this.width = width;
    this.height = height;
  }
  getArea() {
    return this.width * this.height;
  }
};

var Square = class extends Rectangle {
  constructor(width) {
    super(width, width);
  }
  getArea() {
    console.log('size is' + super.getArea())
  }
}
```


### 5. 정리

클래스 : 어떤 사물의 공통 속성을 모아 정의한 추상적인 개념(붕어빵 틀)   
인스턴스 : 클래스의 속성을 지니는 구체적인 사례(붕어빵(피자붕어빵, 크림붕어빵 등등))   

클래스에 직접 생성한 메서드를 스태틱 메서드라 하며 인스턴스에서 직접 호출 불가능   

es5에서 클래스를 구현하기 위한 세가지 방법
1. superclass의 프로퍼티들을 일일이 삭제하는 방법 `delete Square.prototype.width; Object.freeze(Square.prototype)`
2. 중간에 빈 함수(Bridge)를 이용하는 방법
3. Object.create를 이용하는 방법 (이건 잘 이해 x)

=> es6 클래스 사용하면 간단하게 해결

