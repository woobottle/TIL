# 5. 실행 컨텍스트와 클로저

[1. 실행 컨텍스트의 개념](#1-실행-컨텍스트의-개념)   
[2. 활성객체와 변수객체](#2-활성객체와-변수객체)    
[3. 스코프 체인](#3-스코프-체인)   
[4. 클로저](#4-클로저)   


### 1. 실행 컨텍스트의 개념
ECMA 스크립트에서 실행 컨텍스트에 대한 설명
> 현재 실행되는 컨텍스트에서 이 컨텍스트와 관련 없는 실행 코드가 실행 되면, 새로운 컨텍스트가 생성되어 스택에 들어가고 제어권이 그 컨텍스트로 이동한다

```javascript
console.log("This is global context");

function ExContext1() {
  console.log("This is ExContext1()")
}

function ExContext2() {
  ExContext1() // 제어권이 exContext1의 실행 컨텍스트로 넘어가고 종료되면 제어권이 다시 돌아온다.
  console.log("this is Excontext2()')
}

ExContext2()

// this is global context
// this is excontext1()
// this is excontext2()
```


### 2. 활성객체와 변수객체

```javascript
function execute(param1, param2) {
  var a = 1, b = 2;
  function func() {
    return a + b;
  }
  return param1 + param2 + func()
}

execute(3,4)
```

1. 실행 컨텍스트가 생성되면 자바스크립트 엔진은 실행에 필요한 정보를 담을 객체를 생성한다 -> 이게 활성객체
2. arguments 객체 생성
3. 스코프 정보 생성
4. 변수 생성 
5. this 바인딩
6. 코드 실행

<img src="https://user-images.githubusercontent.com/72545732/135300469-c13feacf-62d8-4d23-a3a4-ce583d705a31.png" width='60%'/>


### 3. 스코프 체인

자바스크립트에서는 오직 함수만이 유효 범위의 한 단위가 된다.   
이 유효 범위를 나타내는 스코프가 [[scope]]프로퍼티로 각 함수 객체 내에서 연결 리스트 형식으로 관리


```javascript
var var1 = 1;
var var2 = 2;
function func() {
  var var1 = 10;
  var var2 = 20;
  console.log(var1);
  console.log(var2);
}
func()
console.log(var1);
console.log(var2);
```


![image](https://user-images.githubusercontent.com/72545732/135302791-a8d87fba-ad88-4c50-a003-c39eceb52e10.png)

내 정리 => 스코프 체인에 자기 자신과 상위 스코프의 친구가 스택처럼 쌓이고 변수를 참조할때 우선 맨 처음 스코프내에서 찾고 그 다음에 없으면 그 다음 스코프로 가서 찾고

책 정리
* 각 함수 객체는 [[scope]] 프로퍼티로 현재 컨텍스트의 스코프 체인을 참조한다.
* 한 함수가 실행되면 새로운 실행 컨텍스트가 만들어지는데, 이 새로운 실행 컨텍스트는 자신이 사용할 스코프 체인을 다음과 같은 바업ㅂ으로 만든다. 현재 실행되는 함수 객체의 [[scope]] 프로퍼티를 복사하고 새롭게 생성된 변수 객체를 해당 체인의 제일 앞에 추가한다.
* 요약하면 스코프 체인은 다음과 같이 표현할 수 있다   
스코프체인 = 현재 실행 컨텍스트의 변수 객체 + 상위 컨텍스트의 스코프 체인


```javascript
var value = "value1";

function printValue() {
  return value;
}

function printFunc(func) {
  var value = "value2";
  console.log(func());
}

printFunc(printValue) // value1
// 위의 함수는 결국 printValue가 실행되는건데 
// printValue function의 스코프체인에는 printFunc가 포함되어 있지 않으므로 
// 전역객체로 선언된 value가 호출된다.
```

### 4. 클로저

이미 생명주기가 끝난 외부 함수의 변수를 참조하는 함수를 클로저라 한다. => 함수를 클로저라 한다!!!   
스코프체인에 변수 객체만 남아있어서 계속 참조되고 있는 경우로   
가비지 컬렉션에 의해 제거되지 않는다.

내가 생각한 예시
```javascript
function printFunc() {
  var value = "value";

  function printValue() {  // 얘가 클로저
    console.log(value)
  }

  return printValue
}

var inner = printFunc()
inner()
```

책의 예시
```javascript
function outerFunc() {
  var x = 10;
  var innerFunc = function() { console.log(x) } // innerFunc가 클로저
  return innerFunc;
}

var inner = outerFunc()  // 이거 실행후 outerFunc 실행 컨텍스트는 종료
inner();
```


```javascript
function outerFunc(arg1, arg2) {
  var local = 8;
  function innerFunc(innerArg) {
    console.log((arg1 + arg2)/(innerArg + local));
  }
  return innerFunc
}
var exam1 = outerFunc(2, 4) 
exam1(2) // 0.6
```

클로저의 활용 
-----
private 메서드 처럼 사용할수 있고 전역변수로 사용하지 않고 함수 내부에서 사용 가능
ex) html에서 박스 색깔 토글한다고 가정

```html
<body>
  <div id="box" style="width: 80px; height: 80px"></div>


  <script type="text/javascript">
    const box = document.getElementById("box")

    const outerFunc = function () {
      let isToggle = true;

      const innerFunc = function () {
        const backgroundColor = '';
        box.style.backgroundColor = backgroundColor === 'green' ? 'red' : 'green';
        isToggle = !isToggle;
      }

      return innerFunc
    }

    box.addEventListener("click", outerFunc())
  </script>
</body>


```

