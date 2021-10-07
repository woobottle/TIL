# 1. 데이터 타입

### 1. 데이터 타입의 종류 

##### 자바스크립 데이터 타입
* 기본형 타입
  1. String
  2. Number
  3. Boolean
  4. Null
  5. Undefined
  6. Symbol (es6 에서 추가)

* 참조형 타입
  1. Array
  2. Regex
  3. Function
  4. Object (es6 에서 추가)
  5. Date (es6 에서 추가)

* 기본형과 참조형의 차이를 알아야 한다
  * 기본형은 값이 담긴 주솟값을 바로 복제
  * 참조형은 값이 담긴 주솟값들을 가리키는 주솟값을 복제

##### 데이터 타입에 관한 배경지식

자바스크립트에서는 메모리 압박에서 좀 더 자유롭다. 숫자의 경우 정수형인지 부동 소수점인지 확인 안하고 8바이트를 바로 할당.   

##### 변수 선언과 데이터 할당

메모리 영역에 변수 영역과 데이터 영역으로 나뉘어져 있다.   
`var a = 'abc'` 를 선언하면 
1. 변수영역에 a를 저장
2. 데이터 영역에 abc를 저장
3. 변수영역이 가리키는 주솟값을 데이터 영역의 abc를 가리키게 한다.
4. 이후에 변수 a를 불러오면 데이터 영역의 참조된 주솟값을 통해 그 값을 가져온다.

변수 영역/데이터 영역으로 나눈 이유는 데이터 변환을 자유롭게 할 수 있게 함과 동시에 메모리를 더욱 효율적으로 관리하기 위해서 이다.   
미리 정해둔 공간내에서만 값을 변경하거나 하면 값에 크기에 따라 공간의 크기가 달라지므로 정해둔 공간의 크기를 변경하는 작업이 전체적으로 필요해지게 된다. 따라서 따로 분리해서 관리

```javascript
var obj1 = {
  a: 1,
  b: 'bbb',
}
```
1. 변수 영역에 obj1에 대한 주솟값을 할당
2. 데이터 영역에 obj1의 객체들을 가리키는 주솟값을 할당, 
3. 1, bbb에 관한 주솟값을 할당
4. obj1의 변수들을 관리하는 변수 영역을 또 할당
5. 변수들을 관리하는 변수 영역에 키값 넣고 주솟값은 데이터 영역의 1, bbb를 가리키게 함

**객체의 변수 영역이 별도로 존재한다**


### 불변 객체
객체의 가변성에 따른 문제점
```javascript
var user = {
  name: 'Jaenam",
  gender: 'male',
}

var changeName = function(user, newName) {
  var newUser = user;
  newUser.name = newName;
  return newUser;
}

var user2 = changeName(user, 'Jung')

if (user !== user2) {
  console.log("유저 정보가 변경되었습니다")
}
console.log(user.name, user2.name) //Jung Jung
console.log(user === user2) // true
```

해결책 -> 새로운 객체를 리턴시켜버리자
```javascript
var user = {
  name: 'Jaenam",
  gender: 'male',
}

var changeName = function(user, newName) {
  return {
    name: newName,
    gender: user.gender,
  }
}

var user2 = changeName(user, 'Jung')

if (user !== user2) {
  console.log("유저 정보가 변경되었습니다")
}
console.log(user.name, user2.name) //Jaenam Jung
console.log(user === user2) // false
```

`console.log(typeof null) // object`