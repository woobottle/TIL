# 2. 리액트 es6 문법 액기스

### 2-1 템플릿 문자열
### 2-2 전개 연산자
```js
var array1 = ['one', 'two']
 // 전개 연산자를 배열 표현식 없이 사용한 잘못된 예제
var wrongArr = ...array1
```

### 2-3 가변 변수와 불변 변수
가변변수 : let
불변변수는 값을 다시 할당할 수 없는 것이지 값을 변경할 수는 있다.
```js
const arr2 = []
const obj2 = {}
obj2['name'] = '내이름';
Object.assign(obj2, { name: '새이름' })
```

불변성을 지키기 위해 배열에서 값을 추가할때는 concat, 삭제할때는 slice 등을 이용하자.
push, pop, shift등을 이용하면 원본 데이터가 변경되므로 불변성이 깨진다.
```js
const arr = [1,2,3]
const arr2 = arr.concat(4)
const arr3 = arr2.shift(0, 1)
```

### 2-4 클래스

es5 prototype 이용한 클래스
```js
function Shape(x, y) {
  this.name = 'Shape';
  this.move(x, y);
}
Shape.create = function (x, y) {
  return new Shape(x, y);
};
Shape.prototype.move = function (x, y) {
  this.x = x;
  this.y = y;
};
Shape.prototype.area = function () {
  return 0;
};
Shape.prototype = {
  move: function (x, y) {
    this.x = x;
    this.y = y;
  },
  area: function () {
    return 0;
  },
};

var s = new Shape(0, 0);
s.area();

function Circle(x, y, radius) {
  Shape.call(this, x, y);
  this.name = 'Circle';
  this.radius = radius;
}
Object.assign(Circle.prototype, Shape.prototype, {
  ares: function () {
    return this.radius * this.radius;
  },
});
var c = new Circle(0, 0, 10);
c.area();
```

```js
class Shape {
  static create(x, y) {
    return new Shape(x, y);
  }
  name = 'Shape'; // es7 문법 this.name = 'Shape' 이랑 같다
  constructor(x, y) {
    this.move(x, y);
  }
  move(x, y) {
    this.x = x;
    this.y = y;
  }
  area() {
    return 0;
  }
}
var s = new Shape(0, 0);
s.area();
```

**클래스 내부에서는 변수선언을 위한 키워드(var, let, const) 를 사용하지 않는다** => 변수들의 scope때매 그런것이 아닐까?

```js
class Circle extends Shape {
  constructor(x, y, radius) {
    super(x, y);
    this.radius = radius;
  }
  area() {
    if (this.radius === 0) return super.area();
    return this.radius * this.radius;
  }
}
var c = new Circle(0, 0, 10);
c.area();
```

### 2-5 화살표 함수
커링 함수시에 계단형 구조 만들어지지 않게 해준다
```js
function addNumber(num) {
  return function (value) {
    return num + value;
  }
}

const addNumber = num => value => num + value;
```

화살표 함수는 콜백 함수의 this 오류를 피하기 위해 bind()함수를 사용하여 this객체를 전달하는 과정을 포함하고 있다!

```js
class MyClass {
  value = 10;
  constructor() {
    var addThis2 = function(first, second) {
      return this.value + first + second;
    }.bind(this)
    var addThis3 = (first, second) => this.value + first + second
  }
}
```

### 2-6 객체 확장 표현식과 구조 분해 할당

```js
[item2, item1] = [item1, item2]
```
### 2-7 라이브러리 의존성 관리
기존에 script로 불러올때는 시간도 소요되고 로딩 순서에 따라 오류가 있을수 있었다.
import 구문을 사용하여 script 엘리먼트 없이 연결된 파일 및 의존 파일을 먼저 모두 내려받고 코드를 구동하도록 변경함
### 2-8 배열 함수
forEach, map, reduce
```js
function sum(numbers) {
  return numbers.reduce((cur, next) => cur + next, 0)
}


function parse(qs) {
  const queryString = qs.subStr(1);
  const chunks = qs.split("&");
  return chunks
    .map((chunk) => {
      const [key, value] = chunk.split("=");
      return { key, value }
    })
    .reduce((result, item) => 
      result[item.key] = item.value;
      return result;
    , {})
}
```

### 2-9 비동기 함수
비동기 처리란 => 작업시간이 많이 필요한 작업을 처리할때 대기하고 있는 상태라면 다른 작업들 먼저 처리하고 A의 응답이 오면 처리하는 방식

```js
function work1(onDone) {
  setTimeout(() => onDone('작업1 완료'), 100);
}
function work2(onDone) {
  setTimeout(() => onDone('작업2 완료'), 200);
}
function work3(onDone) {
  setTimeout(() => onDone('작업3 완료'), 300);
}
function urgendWork() {
  console.log('긴급 작업');
}

work1(function (msg) {
  console.log('done after 100ms:' + msg);
  work2(function (msg2) {
    console.log('done after 300ms:' + msg2);
    work3(function (msg3) {
      console.log('done after 600ms:' + msg3);
    });
  });
});

urgendWork();
```

```js
const work1 = () =>
  new Promise((resolve) => {
    setTimeout(() => resolve('작업1 완료!'), 100);
  });

const work2 = () =>
  new Promise((resolve) => {
    setTimeout(() => resolve('작업2 완료!'), 200);
  });

const work3 = () =>
  new Promise((resolve) => {
    setTimeout(() => resolve('작업3 완료!'), 300);
  });

const urgentWork = () => console.log('긴급 작업');

const nextWorkDone = (msg1) => {
  console.log(msg1);
  return work2();
};

work1()
  .then(nextWorkDone)
  .then((msg2) => {
    console.log('done after 200ms:' + msg2);
    return work3();
  })
  .then((msg3) => {
    console.log('done after 300ms:' + msg3);
  });

urgentWork();
```
### 2-10 디바운스와 스로틀

디바운스와 스로틀은 es6 문법이 아니다. '지연처리'를 효율적으로 구현할 수 있으므로 내용에 추가

##### 디바운스
어떤 내용을 입력하다가 특정 시간동안 대기하고 있으면 마지막에 입력된 내용을 바탕으로 서버 요청을 하는 방법
(ex. 네이버 검색창에 내용 입력할때는 아무것도 안나오다가 입력을 멈추면 하단에 검색 목록 나오는 기능)

<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbb29f427-e14d-4908-8868-3a0bb4249f67%2FUntitled.png?table=block&id=57a1a01d-0412-4b07-ad3e-8e8f4428f5b5&spaceId=359809db-cb83-47c2-9cce-0c45f96418ab&width=1910&userId=56059f96-1ce0-4d35-87f6-3200db26ea2a&cache=v2">

```js
export function debounce(func, delay) {
  let inDebounce;
  return function (...args) { // 클로저네
    console.log(inDebounce)
    if (inDebounce) {
      clearTimeout(inDebounce);
    }
    inDebounce = setTimeout(() => func(...args), delay);
  };
}

const run = debounce((val) => console.log(val), 100);

run('a');
run('b');
run('2');
// 100ms 이후
// 2
```

##### 스로틀
스로틀이란 => 입력되는 동안에도 바로 이전에 요청한 작업을 주기적으로 실행한다
(ex. 페이스북 타임라인 => 무한스크롤 하면서 아래에 새로 추가된 요소들을 그린다.)

<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F8b001b12-c0ba-4590-8b81-3221f8c89c5f%2FUntitled.png?table=block&id=612e03bb-8e5b-44a9-8fe8-0eb704493e5f&spaceId=359809db-cb83-47c2-9cce-0c45f96418ab&width=1910&userId=56059f96-1ce0-4d35-87f6-3200db26ea2a&cache=v2">

요청이 실행되는 동안에는 서버 요청 무시하다가 재개되면 그 요청 실행하고 재개되면 그 다음에 처음 들어온 요청 실행, 실행되는 동안에는 중복된 요청을 무시한다.

```js
function throttle(func, delay) {
  let lastFunc;
  let lastRan;
  return function (...args) {
    const context = this;
    if (!lastRan) {
      func.call(context, ...args);
      lastRan = Date.now();
    } else {
      if (lastFunc) clearTimeout(lastFunc);
      lastFunc = setTimeout(function () {
        if (Date.now() - lastRan >= delay) {
          func.call(context, ...args);
          lastRan = Date.now();
        }
      }, delay - (Date.now() - lastRan));
    }
  };
}
var checkPosition = () => {
  const offset = 500;
  const currentScrollPosition = window.scrollY;
  const pageBottomPosition = document.body.offsetHeight - window.innerHeight - offset;
  if (currentScrollPosition >= pageBottomPosition) {
    console.log('다음 페이지 로딩');
  }
};

var infiniteScroll = throttle(checkPosition, 300);
window.addEventListener('scroll', infiniteScroll);
```