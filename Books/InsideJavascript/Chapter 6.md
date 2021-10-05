# 6. 객체지향 프로그래밍

* 클래스, 생성자, 메서드
* 상속
* 캡슐화

클래스 기반의 언어
-----
* JAVA, C++과 같은 언어
* 클래스로 객체의 형태 정의, 생성자로 인스턴스 생성 가능
* 모든 인스턴스가 클래스에 정의된 구조, 런타임에 바꿀수 없다.
* 정확성, 안전성, 예측성

프로토타입 기반의 언어
-----
* 객체의 자료구조, 메서드 등을 동적으로 바꿀수 있다.
* 자바스크립트


클래스, 생성자, 메서드
=====

리팩토링 필요한 코드
새로운 인스턴스들이 모두 각자의 메서드를 가지게 되므로 불필요하게 중복되는 영역을 메모리에 올려놓고 사용한다 -> 자원낭비
```javascript
function Person(arg) {
  this.name = arg;

  this.getName = function() {
    return this.name;
  }

  this.setName = function(value) {
    this.name = value
  }
}

var me = new Person('me')
var you = new Person('you')
var him = new Person('him')
```

프로토 타입을 이용한 리팩토링
```javascript
function Person(arg) {
  this.name = arg;
}

Person.prototype.getName = function() {
  return this.name
}

Person.prototype.setName = function(value) {
  this.name = value;
}

var me = new Person("me")
var you = new Person("you")
```

getName//setName을 프로토타입의 메서드로 접근

상속
===

### 프로타입을 이용한 상속

```javascript
  function create_object(o) {
    function F() {}
    F.prototype = o;
    return new F();
  }
```

prototype이 o인 F객체를 생성해서 리턴 하겠다!!   
**프로토타입의 특성을 활용하여 상속을 구현하는 것이 프로토타입 기반의 상속이다**   


### 클래스 기반의 상속

```javascript
function Person(arg) {
  this.name = arg;
}

Person.prototype.setName = function(value) {
  this.name = value;
};

Person.prototype.getName = function(value) {
  return this.name;
}

function Student(arg) {

}

var you = new Person("iamhjoo");
Student.prototype = you;

var me = new Student("zzoon");
me.setName("zzoon")
console.log(me.getName()) // zzoon
```

### 캡슐화
=> 기본적으로 여러 가지 정보를 하나의 틀 안에 담는 것을 의미, 여기서 중요한 것은 정보의 공개 여부(정보 은닉)

```javascript
var Person = function(arg) {
  var name = arg ? arg : 'zzoon';

  return {
    getName : function() {
      return name;
    },
    setName : function(arg) {
      name = arg;
    }
  };

  var me = Person();
  console.log(me.getName()) // zzoon
}
```

**주의할 점**
private 멤버를 반환할 때 참조값을 반환하는 형태 이므로 값의 변경이 가능해진다
```javascript
var ArrCreate = function(arg) {
  var arr = [1,2,3];

  return {
    getArr: function() {
      return arr;
    }
  };
}

var obj = ArrCreate();
var arr = obj.getArr();
arr.push(5);
console.log(obj.getArr()); // [1,2,3,5]
```

=> 깊은 복사로 값을 반환 하거나, 새로운 객체를 만들어서 값을 반환하거나 한다.

