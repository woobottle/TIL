# 2. 실행 컨텍스트

자바 스크립트는 실행 컨텍스트(실행할 코드에 제공할 환경 정보들을 모아놓은 객체) 들을 콜스택에 쌓아 올렸다가 가장 위에 있는 것부터 실행
```javascript
function outer(){
  var foo = 'bar';
  function inner() {
    console.log(foo);
  }
  outer();
}

outer()
```

inner()
outer()
전역 컨텍스트

실행컨텍스트의 수집정보
-----
* VariableEnvironment: 현재 컨텍스트 내의 식별자들에 대한 정보 + 외부 환경 정보, 선언 시점의 LexicalEnvironment의 스냅샷(변경 사항은 저장되지 않음) => 이것 때문에 리액트에서 useRef 사용해서 조졌었음
* LexicalEnvironment: 처음에는 VariableEnvironment와 같지만 변경 사항이 실시간으로 반영됨.
* ThisBinding: this 식별자가 바라봐야 할 대상 객체

![image](https://user-images.githubusercontent.com/72545732/136683901-42f777c7-0d89-4d7f-8d06-a19b73d7a96e.png)

### VariableEnvironment
맨 처음에는 LexicalEnvironment와 값이 같음
이후에는 LexicalEnvironment의 내용을 사용하게 됨

### LexicalEnvironment
약간 백과사전 느낌
현재 컨텍스트의 내부에는 a,b,c 변수가 있고 그 외부 정보는 D를 참조하도록 구성되어 있다고 안내하는 느낌 
컨텍스트의 내용이 변할때마다 업데이트 됨

```javascript
function a(x) {
  console.log(x); // 1
  var x;
  console.log(x); // 1 (undefined가 출력될 것 같지만 1이 출력됨. => 호이스팅 되기 때문에!!!)
  var x =  2;
  console.log(x); // 2
}
a(1)
```

위의 코드를 단계적으로 변경해보자
```javascript
function a() {
  var x = 1;
  console.log(x);
  var x;
  console.log(x);
  var x = 2;
  console.log(x);
}
a(1)
```

호이스팅 되기 때문에!!!!
```javascript
function a() {
  var x;
  var x;
  var x;

  x = 1;
  console.log(x);
  console.log(x);
  x = 2;
  console.log(x);
}
a(1)
```

함수 선언의 호이스팅
함수 선언은 전체가 호이스팅 된다 그러므로 함수 표현식을 써야 한다.
```javascript
function a() {} => 함수 선언문
var a = function() {} => 함수 표현식
```

```javascript
function a() {
  console.log(b);
  var b = 'bbb';
  console.log(b);
  function b() {
    console.log(b);
  }
}
a()
```

```javascript
function a() {
  var b;
  function b(){

  };

  console.log(b);
  b = 'bbb';
  console.log(b);
  console.log(b);
}
a()
```
아래는 함수 선언문과 함수 표현식의 사용 예
```javascript
console.log(sum(1,2)); // 호이스팅 되므로 에러 발생하지 않음
console.log(multiply(3,4)); // 함수 표현식으로 선언 되었으므로 호이스팅이 되지 않고 에러 발생

function sum(a,b){
    return a + b;
}

var mulitply = function(a,b) {
    return a * b;
}
```

```javascript
function sum(a,b) { // 호이스팅 되어버림
    return a + b;
}
var multiply;

console.log(sum(1,2));
console.log(multiply(3,4));

mulitply = function(a,b) {
    return a * b;
}
```

함수 선언문의 위험성


```javascript
console.log(sum(3,4)) // 3 + 4 = 7
function sum(x,y) {
  return x + y;
}
console.log(sum(1,2)) // 1 + 2 = 3
function sum(x,y) {
  return x + '+' + y + '=' = (x+y)
}
consle.log(sum(3,4)) // 3 + 4 = 7
```

### 스코프, 스코프 체인, outerEnvironmentReference
* 스코프: 식별자에 대한 유효범위
* 스코프 체인: '식별자의 유효범위'를 안쪽에서 부터 바깥으로 차례로 검색해 나가는 것!!
* lexicalEnvironment의 outerEnvironmentReference를 이용하여 스코프 체인이 가능하다!!

```javascript
var a = 1;
var outer = function() {
  var inner = function() {
    console.log(a);
    var a = 3;
  }
  inner();
  console.log(a);
}
outer(); // undefined, 1
console.log(a); // 1
```

inner 내부의 함수에서 undefined가 출력되는 이유는 inner내부의 EnvironmentRecord에 a가 호이스팅 되어서 발견되긴 하지만 아직 값이 할당이 안되어 있으므로
outer 내부의 함수에서 1이 출력되는 이유는 outer가 선언될 당시 a가 1이 였다.