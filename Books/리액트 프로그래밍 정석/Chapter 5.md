# 5. 하이어오더 컴포넌트

### 5-1 커링과 조합 개념 공부하기
커링 => 반환값이 함수인 디자인 패턴!! (중복된 코드를 반복적으로 입력하지 않고 원하는 기능을 조합하여 적재적소에 사용할 수 있다.)
```js
function multiply(a,b) {
  return a * b;
}
```

```js
function multiplyTwo(a) {
  return multiply(a, 2);
}
```

```js
function multiplyX(x) {
  return function(a) {
    return multiply(a, x);
  }
}
```

```js
const multiplyX => x => a => multiply(a, x);
```

커링 사용예시
```js
const multiplyThree = multiplyX(3);
const multiplyFour = multiplyX(4);

const result1 = multiplyThree(3); // 3 * 3;
const result2 = multiplyThree(4); // 4 * 3;
```

```js
const result1 = multiplyX(3)(3)
const result2 = multiplyX(4)(3)
```

* 커링 한 번 더 사용해보기
```js
const equation = (a,b,c) => x => ((x * a) * b) + c;
const formula = equation(2, 3, 4);
const x = 10;
const result = formula(x);
```

* 커링 응용
```js
const multiply = (a, b) => a * b;
const add = (a, b) => a + b;

const multiplyX = x => a => multiply(x, a);
const addX = x => a => add(x, a);

const addFour = addX(4);
const multiplyTwo = multiplyX(2);
const multiplyThree = multiplyX(3);
const formula = x => addFour(multiplyThree(multiplyTwo(x)));
```

커링 => 함수의 인자를 다시 구성하여 필요한 함수를 만드는 패턴

* compose 함수 생성
```js
function compose() {
  const funcArr = Array.prototype.slice.call(arguments);
  return funcArr.reduce(
    function (prevFunc, nextFunc) {
      return function(value) {
        return nextFunc(prevFunc(value));
      }
    },
    function(k) { return k; }
  )
}

const formulaWithCompose = compose(multiplyTwo, multiplyThree, addFour);
```

arguments => 함수의 인자 목록을 배열로 받을 수 있다.
Array.prototype.slice.call 메서드를 통해 인자목록을 배열로 변환

더 간결하게
```js
function compose(...funcArr) {
  return funcArr.reduce(
    function (prevFunc, nextFunc) {
      return function (...args) {
        return nextFunc(prevFunc(...args));
      }
    },
    function(k) { return k; }
  );
}
```

### 5-2 하이어오더 컴포넌트 기초 개념 공부하기
* 상속 패턴의 단점
기존의 상속 패턴의 경우 원치 않는 상속이 일어날 수 있다. (필요한 기능들을 가진 클래스들을 상속받으려다 보면 이 기능은 저쪽에 이기능은 이쪽에 있을 수 있다. 이렇게 되면 기존의 상속구조를 변경해야 한다. (Button -> LoadingButton, ToolTipButton -> SubmitButton))
상속구조가 깊어지면 상속 항목을 한눈에 파악하기 어렵다.

* 데코레이터 패턴
=> 클래스간의 종속성 없이 기능만을 공유한다.  
<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3b68cd1a-0d0c-41a0-a591-969842beac07%2FUntitled.png?table=block&id=828ba384-7d5f-4c25-a1b2-46a33f9ce5ea&spaceId=359809db-cb83-47c2-9cce-0c45f96418ab&width=2000&userId=56059f96-1ce0-4d35-87f6-3200db26ea2a&cache=v2">

=> 데코레이터 패턴에서는 필요한 기능만 탑재하여 각각 독립된 객체를 생성한 것을 볼 수 있다. (자바에서는 인터페이스 사용, 자바스크립트에서는 커링 사용)

하이어오더 컴포넌트 => 자바스크립트의 고차 함수(Higher-order function) 에서 유래, 자바스크립트에서는 커링 함수를 고차 함수라고 함

하이어오더 컴포넌트 예시
```js
function higherOrderComponent(Component) {
  return function Enhanced(props) {
    return <Component {...props}>;
  }
}

function higherOrderComponent(Component) {
  return class Enhanced extends React.Component {
    render() {
      return <Component {...this.props} />;
    }
  }
}
```

### 5-3 하이어오더 컴포넌트 라이브러리 사용하기

### 5-4 다중 하이어오더 컴포넌트 사용하기

### 5-5 필수 입력 항목 표시 기능 추가하며 하이어오더 컴포넌트 복습하기
