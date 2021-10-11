# 5. 클로저

> 이미 생명주기가 끝난 외부 함수의 변수를 참조하는 함수!!

```javascript
var outer = function (){
  var foo = 'bar'
  var inner = function () {
    console.log(foo);
  }
  return inner // 함수를 반환해야함, 함수의 실행을 반환하면 클로저 동작 x
}

var func = outer();
func()
```

**자바스크립트의 가비지 컬렉터는 어떤 값을 참조하는 변수가 하나라도 있다면 그 값은 수집 대상에 포함시키지 않는다!!!**

// return 없이도 클로저가 발생하는 다양한 경우
```javascript
(function() {
  var a = 0;
  var intervalId = null;
  var inner = function(){
    if (++a >= 10) {
      clearInterval(intervalId);
    }
    console.log(a)
  };
  intervalId = setInterval(inner, 1000);
})();
```

```javascript
(function () {
  var count = 0;
  var button = document.createElement("button");
  button.innerText = 'click'
  button.addEventListener('click', function() {
    console.log(++count, 'times clicked')
  });
  document.body.appendChild(button);
})();
```

둘다 지역변수를 참조하는 내부함수를 외부에 전달했기 때문에 클로저다!!!

### 클로저와 메모리 관리

메모리 관리를 위해 참조 카운트를 0으로 만든다.
0으로 만드는 방법은 식별자에 참조형이 아닌 기본형 데이터(null or undefined)를 할당해 버림
```javascript
var outer = (function() {
  var a = 1;
  var inner = function () {
    return ++a;
  }
  return inner;
})();
console.log(outer());
console.log(outer());
outer = null
```


### 클로저 활용 사례
* 콜백 함수 내부에서 외부 데이터를 사용하고자 할 때
```javascript
var fruits = ['apple', 'banana', 'peach'];
var $ul = document.createElement('ul');

fruits.forEach(function(fruit) {
  var $li = document.createElement('li);
  $li.innerText = fruit;
  $li.addEventListenrer('click', function () {
    alert('your choice is' + fruit) // fruit은 클로저로 사라지지 않는다.
  })
  $ul.appendChild($li);
});
```
* 정보 은닉
```javascript
var createCar = function () {
  var fuel = Math.ceil(Math.random() * 10 + 10);
  var power = Math.ceil(Math.random() * 3 + 2);
  var moved = 0;
  return {
    moved: function() {
      return moved;
    },
    run: function () {
      var km = Math.ceil(Math.random() * 6);
      var wasteFuel = km / power;
      if (fuel < wasteFuel) {
        console.log('이동불가');
        return;
      }
      fuel -= wasteFuel;
      moved += km;
    },
  };
}
var car = createCar();
car.run()
console.log(car.moved())
```