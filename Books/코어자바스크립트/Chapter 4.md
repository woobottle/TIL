# 4. 콜백함수

```javascript
var newArr = [10, 20, 30].map(function (currentValue, index) {
  console.log(currentValue, index);
  return currentValue + 5;
})
console.log(newArr);

// 10 0
// 20 1
// 30 2
// [15, 25, 35]
```

map의 구조
```javascript
Array.prototype.map(callback[, thisArg])
callback: function(currentvalue, index, array) 
```
this를 안주면 전역객체로 잡혀버림 

Array.prototpye.map 구현
```javascript
Array.prototyp.map = function (callback, thisArg) {
  var mappedArr = [];
  for (var i = 0; i< this.length; i++) {
    var mappedValue = callback.call(thisArg || window, this[i], i, this);
    mappedArr[i] = mappedValue;
  }
  return mappedArr
}
```
-> 제어권을 넘겨받을 코드에서 call/apply 메서드의 첫번째 인자에 콜백 함수 내부에서의 this가 될 대상을 명시적으로 binding해버림
3장에서 보면 Array 내부함수쪽에서 this 인자로 해서 보내주는거 볼수 있음

```javascript
var obj = {
  vals: [1,2,7],
  logValues: function(v, i) {
    console.log(this, v, i);
  }
}
obj.logValues(1,2);
[4,5,6].forEach(obj.logValues); // window 4 0
```

### 콜백 함수 내부의 this에 다른 값 바인딩 하기
```javascript
var obj1 = {
  name: 'obj1',
  func: function () {
    console.log(this.name)
  }
}
var obj2 = {
  name: 'obj2',
  func: obj1.func,
}
var callback2 = obj2.func();
setTimeout(callback2, 1500);

var obj3 = { name: 'obj3' };
var callback3 = obj1.func.call(obj3);
setTimeout(callback3, 2000);

var obj4 = { name: 'obj4' };
setTimeout(obj1.func.bind(obj4), 3000)
```

