# 3. This

### 상황에 따라 달라지는 this
* this는 함수를 호출할 때 결정된다.


* 전역공간에서의 this는 전역객체를 참조(브라우저에서는 window, node.js에서는 global)
(전역변수를 선언하면 자바스크립트 엔진은 이를 전역객체의 프로퍼티로 할당한다.)
          
```javascript
console.log(this);
console.log(window);
console.log(this === window); // true
```

* 어떤 함수를 메서드로서 호출한 경우 this는 메소드 호출 주체를 가리킴
```javascript
var func = function(){
  console.log(this, x)
}

func(1) // window {....} 1

var obj: {
  method: func
}

obj.method(2) // {method: func} 2
```

* 어떤 함수를 함수로서 호출한 경우 this는 전역 객체
```javascript
var func = function() {
  console.log(this);
}
func() // window
```

내부 함수에서 this를 우회하는 법
```javascript
var obj = {
  outer: function() {
    console.log(this);
    var innerFunc1 = function() {
      console.log(this) // window
    }
    innerFunc1();

    var self = this;
    var innerFunc2 = function() {
      console.log(self); // outer: f
    }
    innerFunc2()
  }
};

obj.outer();
```

화살표 함수를 사용
화살표 함수는 실행 컨텍스를 생성할때 this 바인딩 과정 자체가 빠져버림!! 상위 스코프의 this를 그대로 활용!!
```javascript
var obj = {
  outer: function() {
    console.log(this); // { outer : f }
    var innerFunc = () => {
      console.log(this); // { outer: f }
    }
    innerFunc();
  }
};
obj.outer();
```

콜백 함수 호출 시 그 함수 내부에서의 this
```javascript
setTimeout(function () { console.log(this); }, 300); // window

[1,2,3,4,5].forEach(function (x) {
  console.log(this, x) // window, x
})

document.body.innerHTML += "<button id='a'>클릭</button>"
document.body.querySelector("#a").addEventListener('click', function(e) {
  console.log(this, e); // 이벤트 걸린 객체 정보, click에 대한 정보
})
```


* 생성자 함수에서의 this는 생성될 인스턴스를 참조
```javascript
var Person = function(name, age) {
  this.name = name;
  this.age = age;
}

var a = new Person('1', 1);
var b = new Person('2', 2);
```

### 명시적으로 this를 바인딩하는 방법

* call 메서드
`Fucnction.prototype.call(thisArg[, arg1[, arg2[, ...]]])`

```javascript
var func = function (a,b,c) {
  console.log(this, a, b, c);
}

func(1,2,3) // window, 1,2,3
func.call({x:1}, 1,2,3) // {x:1}, 1,2,3
```

* apply 메서드
call 메서드와 기능적으로 완전 동일
call 메서드는 첫번째 인자를 제외한 나머지 모든 인자들을 호출할 함수의 매개변수로 지정
apply 메서드는 두번째 인자를 배열로 받아 그 배열의 요소들을 호출할 함수의 매개변수로 지정해버림

apply vs call 뒤에 매개 변수를 배열로 받냐 아니냐 차이

`Fucnction.prototype.apply(thisArg[, argsArray])`
```javascript
var func = function (a, b, c) {
  console.log(this, a, b, c);
}

func.apply({x: 1}, [1,2,3]) // {x:1}, 1, 2, 3

var obj = {
  a: 1,
  method: function (x,y) {
    console.log(this.a, x, y)
  }
}

obj.method.apply({a: 4}, [5, 6]) // 4, 5, 6
```

### call / apply 메서드의 활용
* 주로 유사배열 객체에 활용해버림
* 유사배열 객체 -> 배열처럼 length 가지고 있는 친구들, 아래는 그 예시
```javascript
var obj = {
  0: 'a',
  1: 'b',
  2: 'c',
  length: 3
}

Array.prototype.push.call(obj, 'd');
console.log(obj) // {0: 'a', 1: 'b', 2: 'c', 3: 'd', length: 4}

Array.prototype.slice.call(obj) // 배열을 slice하면 인자 없을때는 자기 자신 뱉어버림, 얕은 복사임
console.log(obj) // ['a', 'b', 'c', 'd'] 
```

* es6에서는 유사배열 객체를 배열객체로 바꿔버리기 위해 `Array.from`을 추가
```javascript
var obj = {
  0: 'a',
  1: 'b',
  2: 'c',
  length: 3,
}

var arr = Array.from(obj);
console.log(arr) // ['a', 'b', 'c']
```

### 생성자 내부에서 다른 생성자를 호출
```javascript
function Person(name, gender) {
  this.name = name;
  this.gender = gender;
}

function Student(name, gender, school) {
  Person.call(this, name, gender);
  this.school = school;
}

function Employee(name, gender, company) {
  Person.call(this, name, gender);
  this.company = company;
}

var by = new Student('minki', 'male', '단국대');
var jn = new Employee('woo', 'male', 'google');
```

```javascript
var numbers = [1,2,3,4,5]
var max = Math.max.apply(null, numbers)
var min = Math.max.apply(null, numbers)
console.log(max, min)

var max = Math.max(...numbers)
var min = Math.min(...numbers)
console.log(max, min)
```

### bind 메서드
`Function.prototype.bind(thisArg[, arg1[, arg2[, ...]]])`
```javascript
var func = function (a,b,c,d) {
  console.log(this, a, b, c, d);
}
func(1,2,3,4);

var bindFunc1 = func.bind({x: 1})
bindFunc1(1,2,3,4) // {x:1}, 1,2,3,4
```

* 내부함수에 this를 전달하자!!!
```javascript
var obj = {
  outer: function(){
    console.log(this);
    var innerFunc = function() {
      console.log(this)
    }
    innerFunc.call(this);
  }
}
obj.outer()

var obj = {
  outer: function(){
    console.log(this);
    var innerFunc = function() {
      console.log(this)
    }.bind(this);
    innerFunc();
  }
}
obj.outer()
```

### 별도의 인자로 this를 받는경우(콜백 함수 내에서의 this)

```javascript
var report = {
  sum: 0,
  count: 0,
  add: function() {
    var args = Array.prototype.slice.call(arguments);
    args.forEach(function(entry) {
      this.sum += entry;
      ++this.count;
    }, this); // forEach 내부에 this를 같이 인자로 보내줘야 상위의 this(report)를 그대로 참조할수 있음
  },
  average: function() {
    return this.sum / this.count;
  }
}
report.add(60, 70, 80, 60)
console.log(report.sum, report.count, report.average())
```


* 콜백 함수와 함께 thisArgs를 인자로 받는 ㅁ서드
```javascript
Array.prototype.forEach(callback[, thisArg])
Array.prototype.map(callback[, thisArg])
Array.prototype.filter(callback[, thisArg])
Array.prototype.some(callback[, thisArg])
Array.prototype.every(callback[, thisArg])
Array.prototype.find(callback[, thisArg])
```