# 6. 프로토타입

자바스크립트는 프로토타입 기반 언어입니다. 
클래스 기반 언어에서는 '상속'을 사용하지만 프로토타입 기반 언어에서는 어떤 객체를 원형으로 삼고 이를 복제 함으로써 
상속과 비슷한 효과를 얻습니다.


`var instance = new Constructor()`

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ffb65403-0e38-4ee5-a03c-e650a22472b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211011T055922Z&X-Amz-Expires=86400&X-Amz-Signature=3f3c35ea40d45a530931e3ac43e59a077880c3c34910d4fd1bc7e326f268e6b5&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" width="50%">

* 어떤 생성자 함수를 new 연산자와 함께 호출하면
* Constructor에서 정의된 내용을 바탕으로 새로운 instance가 생성됩니다.
* instance에는 __proto__라는 프로퍼티가 자동으로 부여됨
* 이 프로터피는 Counstructor의 prototype이라는 프로퍼티를 참조

```javascript
var Person = function (name) {
  this._name = name;
}

Person.prototype.getName = function() {
  return this._name;
}

var suzi = new Person('Suzi');
suzi.__proto__.getName(); // undefined
suzi.getName() // Suzi
```
`Person.prototype === suzi.__proto__`

1. instance의 __proto__가 Counstructor의 prototype 프로퍼티를 참조하므로 Person.prototype의 name이 반환되어야 함. 근데 이게 없으므로 undefined가 호출된거.

```javascript
var suzi = new Person('Suzi');
suzi.__proto__._name = "SUZI_proto";
suzi.__proto__.getName(); // SUZI_proto
```
=> 관건은 this이다!! method의 this가 suzi.__proto__가 되는게 문제다

```javascript
var suzi = new Person('Suzi', 28);
suzi.getName(); // suzi
var iu = new Person('iu', 28);
iu.getName(); // iu
```
=> __proto__가 생략이 가능한 프로퍼티 이기 때문에 위의 코드는 동작이 원할하게 나오는 것이다.
=> 그냥 그런가 하고 받아들이자!!!

```javascript
suzi.__proto__.getName
-> suzi(.__proto__).getName
-> suzi.getName
```

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/732a2d11-8a71-406e-8354-f383a157bdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211011T060402Z&X-Amz-Expires=86400&X-Amz-Signature=e3242e27b62da78f842e4c7b8d6a6a206cead0fa80d35af7b8b44217fc5c3b76&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" 
width="50%">

**생성자 함수의 prototyp에 어떤 메서드나 프로퍼티가 있다면 인스턴스에서도 마치 자신의 것처럼 해당 메서드나 프로퍼티에 접근할 수 있다!!**

```javascript
var arr = [1,2];
arr.forEach(function () {})
Array.isArray(arr); // true
arr.isArray(); // TypeError
```
isArray는 Array.prototype에 있는 메서드가 아니라 Array에 있는 메서드여서 4번째 줄에서 에러가 난다.
(Array.isArray, Array.from)

### constructor 프로퍼티
 
생성자 함수 (자기 자신)을 참조한다~~~

```javascript
var arr = [1,2];
Array.prototype.constructor === Array // true
arr.__proto_.constructor === Array // true
arr.constructor === Array // true

var arr2 = new arr.constructor(3,4);
console.log(arr2) // [3,4]
```

### 프로토타입 체인

```javascript
var Person = function (name) {
  this.name = name;
};

Person.prototype.getName = function () {
  return this.name;
}

var iu = new Person('지금');
iu.getName = function(){
  return '바로 ' + this.name;
}
console.log(iu.getName());
```

=> 자바스크립트 엔진이 getName이라는 메서드는 찾는 방식은 자신 내부에서 메서드 검색하고 없으면 __proto__를 검색하는 순서로 진행.

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d39d5071-f7d0-403b-b4a2-63905d925560/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211011T063916Z&X-Amz-Expires=86400&X-Amz-Signature=6255eaa0dd7ad79d86c57b0b89abcf6c20c30159be228c48b98f22ec7cf28510&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22" width="50%">

```javascript
var arr = [1,2];
arr(.__proto__).push(3)
arr(.__proto__)(.__proto__).hasOwnProperty(2);
```

메서드 오버라이드와 프로토타입 체이닝
```javascript
var arr = [1,2];
Array.prototype.toString.call(arr); // 1,2
Object.prototype.toString.call(arr); // [object Array]
arr.toString(); // 1,2

arr.toString = function () {
  return this.join('_');
}
arr.toString(); 1_2
```