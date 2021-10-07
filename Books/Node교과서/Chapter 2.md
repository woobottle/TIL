# 2. 알아두어야 할 자바스크립트

### const,let
둘이 공통적으로 가지는 특징 -> 블록 스코프

```javascript
if (true) {
  var x = 3;
}
console.log(x) // 3

if (true) {
  const y = 3;
}
console.log(y) // y is undefined
```

### 템플릿 문자열
```javascript
const num3 = 1;
const num4 = 2;
const result2 = 3;
const string2 = `${num3} 더하기 ${num4} 는 ${result2}`
```

### 객체 리터럴
```javascript
// 이전 코드
var sayNode = function() {
  console.log("node");
}
var es = 'ES';
var oldObject = {
  sayJS: function() {
    console.log('JS');
  },
  sayNode: sayNode,
}
oldObject[es+6] = 'Fantastic';

// 변경된 코드
const newObject = {
  sayJS(){
    console.log('JS')
  },
  sayNode,
  [es+6]: 'Fantastic',
}
```

### 화살표 함수
```javascript
const sayName = function () {
  console.log("me")
}

const sayMyName = () => "me"
```

### 구조분해 할당
```javascript
const test = [1,2,3];
const [a, b, c] = test;
console.log(a, b, c)
```

### 클래스
es6에서 클래스가 추가되었지만 여전히 프로토타입 기반으로 동작한다.   
프로토타입 기반 문법을 보기 좋게 변경한 것이라고 생각하면 됨
```javascript
class Human {
  constructor(type = 'human') {
    this.type = type;
  }
}

staic isHuman(human) {
  return human instanceof Human;
}

breathe() {
  alert('h-a-m;)
}

class Zero extends Human {
  constructor(type, firstName, lastName) {
    supter(type);
    this.firstName = firstName;
    this.lastName = lastName;
  }

  sayName() { 
    super.breathe();
    alert(`${this.firstName} ${this.secondName}`)
  }
}

const newZero = new Zero('human', 'Zero', 'Cho')
Human.isHuman(newZero)
```


### 프로미스
```javascript
const condition = true;
const promise = new Promise((resolve, reject) => {
  if (condition) {
    resolve('성공')
  } else {
    reject('실패')
  }
})

promise.then((message) => {
  console.log(message) // 성공(Resolve)한 경우 실행
})
.catch((error) => {
  console.log(error) // 실패(reject)한 경우 실행
})
.finally(() => {
  console.log('무조건')
})
```

```javascript
const promise1 = Promise.resolve('성공1');
const promise2 = Promise.resolve('성공2');
// Promise all은 하나라도 실패하면 error promise 중인것들이 모두 끝나야 return
Promise.all([promise1, promise2])
  .then((result) => {
    console.log(result) // ['성공1', '성공2']
  })
  .catch((error) => {
    console.error(error);
  })
```

### async/await
es2017부터 추가

```javascript
const findAndSaveUser = async (Users) => {
  try {
    let user = await Users.findOne({});
    user.name = 'zero';
    user = await user.save();
    user = await Users.findOne({ gender: 'm' });
  } catch (error) {
    console.error(erorr);
  }
}
```

```javascript
const promise1 = Promise.resolve('성공');
const promise2 = Promise.resolve('성공2);
(async () => {
  for await (promise of [promise1, promise2]) {
    console.log(promise);
  }
})()
```


프론트엔드 자바스크립트
------

### Ajax
주로 axios 사용

### FormData

```javascript
const formData = new FormData();
formData.append('name', 'zeroCho');
formData.append('item'. 'orange');
formData.has('item');
formData.has('money');
formData.get('item')
formData.getAll('item')
```

### encodeURIComponent, decodeURIComponent
ajax요청에 한글 있는경우 서버마다 다른데 인식이 되지 않는경우가 있다.
```javascript
encodeURIComponent('노드'); // '%EB%85%B8%EB%939%9C'

decodeURIComponent('%EB%85%B8%EB%939%9C') // 노드
```

### 데이터 속성과 dataset
```html
<ul>
  <li data-id="1" data-user-job="programmer">Zero</li>
</ul>
<script>
  console.log(document.querySelector('li').dataset) // {id: '1', userJob: 'programmer'}
</script>
```