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