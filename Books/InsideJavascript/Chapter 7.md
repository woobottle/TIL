# 함수형 프로그래밍

**순수함수**: 외부에 영향을 미치지 않는 함수
**고계함수**: 함수를 또 하나의 값으로 간주하여 함수의 인자 혹은 반환값으로 사용할 수 있는 함수 (1급객체의 조건이랑 비슷한것 같군)

=> 내부 데이터 및 상태는 그대로 둔 채 제어할 함수를 변경 및 조합함으로써 원하는 결과를 얻어내는 것이 함수형 프로그래밍의 중요한 특성!!!!!  


우리는 자바스크립트의 특성인 1급객체인 함수와 클로저를 이용해서 함수형 프로그래밍 구현이 가능하다.

```javascript
var f1 = function(input) {
  var result; 
  // 암호화 작업 수행
  result = 1;
  return result;
}

var f2 = function(input) {
  var result; 
  // 암호화 작업 수행
  result = 2;
  return result;
}

var f3 = function(input) {
  var result; 
  // 암호화 작업 수행
  result = 3;
  return result;
}

var get_encrypted = function(func) {
  var str = 'zzoon'; // str에 영향이 가지 않게 클로저로 사용

  return function() {
    return func.call(null, str);
  }
}

var encrypted_value = get_encrypted(f1)();
console.log(encrypted_value);
var encrypted_value = get_encrypted(f2)();
console.log(encrypted_value);
var encrypted_value = get_encrypted(f3)();
console.log(encrypted_value);
```


```javascript
function multiply(arr) {
  var len = arr.length;
  var i = 0, result = 1;

  for(; i < len; i++) {
    result *= arr[i]
  }
  
  return result;
}

var arr = [1,2,3,4];
console.log(multiply(arr)) //  24
```

```javascript
function reduce(func, arr, memo) {
  var len = arr.length,
    i = 0,
    accum = memo;

    for (; i < len; i++) {
      accum = func(accum, arr[i]);
    }

    return accum;
}

var arr = [1,2,3,4];

var sum = function(x, y) {
  return x + y;
}

var multiply = function(x, y) {
  return x * y;
}

console.log(reduce(sum, arr, 0))
console.log(reduce(multiply, arr, 0))
```


자바스크립트에서의 함수형 프로그래밍을 활용한 주요 함수
-----

### 커링

=> 특정 함수에서 정의된 인자의 일부를 넣어 고정시키고, 나머지를 인자로 받는 새로운 함수를 만드는 것
(인자 세개 받는 함수인데 2개나 혹은 1개만 들어와도 문제 없는것으로 이해함)    
```javascript
function calculate(a,b,c) {
  return a * b + c;
}

function curry(func) {
  console.log(arguments) // Arguments(2) [ƒ, 1, callee: ƒ, Symbol(Symbol.iterator): ƒ],  Arguments(3) [ƒ, 1, 3, callee: ƒ, Symbol(Symbol.iterator): ƒ]
  var args = Array.prototype.slice.call(arguments, 1);
  console.log(args) // 1,    1,3
  return function(){
    return func.apply(null, args.concat(Array.prototype.slice.call(arguments)));
  }
}

var new_func1 = curry(calculate, 1);
console.log(new_func1(2, 3))
var new_func2 = curry(calculate, 1, 3);
console.log(new_func2(3))
```


### bind
```javascript
Function.prototype.bind = function(thisArg) {
  var fn = this,
  slice = Array.prototype.slice,
  args = slice.call(arguments, 1);
  return function () {
    return fn.apply(this, args.concat(slice.call(arguments))) // 커링과 차이는 apply에서 this로 바인딩을 해준다.
  }
}
```


### each
```javascript
function each(obj, fn, args) {
  if (obj.length == undefined) 
    for (var i in obj)
      fn.apply(obj[i], args || [i, obj[i]])
  else
    for (var i = 0; i < obj.length; i++) 
      fn.apply(obj[i]), args || [i, obj[i]];
  return obj
}

each([1,2,3], function(idx, num)) {
  console.log(idx + ":" + num)
}
```

### map
```javascript
Array.prototype.map = function(callback) {
  var obj = this;
  var value, mapped_value;
  var A = new Array(obj.length);

  for(var i = 0; i < obj.length; i++) {
    value = obj[i];
    mapped_value = callback.call(null, value);
    A[i] = mapped_value
  }

  return A;
}

var arr = [1,2,3];
var new_arr = arr.map(function(value) {
  return value * value;
})
```


### reduce 
```javascript
Array.prototype.reduce = fucnction(callback, memo) {
  var obj = this;
  var value, accumulated_value = 0;

  for(var i = 0; i< obj.length; i++) {
    value = obj[i];
    accumulated_value = callback.call(null, accumulated_value, value)
  }

  return accumulated_value;
}

var arr = [1,2,3]
var accumulated_val = arr.reduce(function(a,b) {
  return a + b * b;
});
```