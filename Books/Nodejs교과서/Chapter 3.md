# 3. 노드 기능 알아보기

### 3.1 REPL 사용하기

* 자바스크립트는 스크립트 언어이므로 미리 컴파일을 하지 않아도 즉석에서 코드를 실행할 수 있따!!
* REPL(Read, Eval, Print, Loop)

### 3.2 JS 파일 실행하기
`node helloworld`

### 3.3 모듈로 만들기

* 노드는 코드를 모듈로 만들 수 있다.
* 모듈 => 특정한 기능을 하는 함수나 변수들의 집합

```js
const odd = '홀수 입니다';
const even = '짝수 입니다';

// commonJs 방식이네
module.exports = {
  odd,
  even,
}
```

```js
const { odd, even } = require('./var');

function checkOddOrEven(num) {
  if (num % 2) {
    return odd;
  }
  return even;
}

module.exports = checkOddOrEven;
```

```js
const { odd, even } = require('./var');
const checkNumber = require('./func');

function checkStringOddOrEven(str) {
  if (str.length % 2) {
    return odd;
  } 
  return even;
}

console.log(checkNumber(10));
console.log(checkStringOddOrEven("hello"));
```

> 노드에서도 esm 방식으로 사용을 할 수 있다.  
> 하지만 파일의 확장자를 mjs로 지정해야 한다.  
> js로 쓰면서 esm 방식 사용하려면 package.json 에서 type: "module" 속성을 넣으면 된다!!   

### 3.4 노드 내장 객체 알아보기

1. global

> node에는 DOM이나 BOM이 없으므로 window, document 객체를 사용할 수 가 없다!!   
> 사용하면 에러 발생한다

2. console
3. 타이머
* `setTimeout(콜백 함수, 밀리초)` : 밀리초 뒤에 실행
* `setInterval(콜백 함수, 밀리초)` : 밀리초 마다 실행
* `setImmediate(콜백 함수)` : 즉시 실행(호출 스택이 비어야 실행된다!!)
* `clearTimeout(아이디)`: setTimeout 취소
* `clearInterval(아이디)`: setInterval 취소
* `clearImmediat(아이디)`: setImmediate 취소

4. __filename, __dirname
```js
console.log(__filename) // C:/Users/zerocho/filename.js
console.log(__dirname) // C:/Users/zerocho
```

5. module, exports, require

`module.exports === exports // true`

노드에서 this는??? 
=> module.exports를 가리킴!! 함수 선언문 내부의 this는 글로벌 객체!
```js
console.log(this); // {}
console.log(this === module.exports); // true
console.log(this === exports); // true
function whatIsThis() {
  console.log('function', this === exports, this === global)
}
whatIsThis(); // function false true
```

* 한 번 require된 것은 require.cache에 저장된다. 이후 요청오면 cache에 있는걸 재사용함

6. process

```js
process.version
process.arch
process.platrofm
process.pid
process.uptime()
process.execPath
process.cwd()
process.cpuUsage()
```

* process.env
=> 시스템의 환경변수 임!!, dotenv를 사용해서 조지자

* process.nextTick
이벤트 루프가 다른 콜백함수 보다 nextTick의 콜백함수를 우선으로 처리하도록 한다!!
```js
setImmediate(() => {
  console.log('immediate');
})
process.nextTick(() => {
  console.log('nextTick')
})
setTimeout(() => {
  console.log('setTimeout')
},0 )
Promise.resolve().then(() => console.log('promise'))
```
```js
nextTick
promise
timeout
immediate
```
* process.exit()

### 3.5 노드 내장 모듈 사용하기
1. os   
  `const os = require('os')`
2. path  
  (경로에 대한 내용들)
3. url    
  (인터넷 주소 커스텀 모듈), searchParams 객체가 특히 유용하다
  `a = new URL(''); a.searchParams.getAll()`
4. querystring
5. crypto   
  암호화를 도와주는 모듈!!
6. util   
  `util.deprecate`   
  `util.promisify`   
7. worker_threads
  노드에서 멀티 스레드 방식으로 작업하는 방법
```js
const {
  Worker, isMainThread, parentPort 
} = require('worker_threads');

if (isMainThread) {
  const worker = new Worker(__filename);
  worker.on('meesage', message => console.log('from worker', message));
  worker.on('exit', () => console.log('worker exit'));
  worker.postMessage('ping')
} else {
  parentPort.on('message', (value) => {
    console.log('from parent', value);
    parentPort.postMessage('pong');
    parentPort.close(); // 직접 워커를 종료해야한다!!
  })
}
```

8. child_process
=> 노드에서 다른 프로그램을 실행하고 싶거나 명령어를 수행하고 싶을 때 사용 (다른 언어의 코드를 수행하고 결과를 받아올 수 있다.)

```js
const spawn = require('child_process').spawn;

const process = spawn('python', ['test.py'])

process.stdout.on('data', function(data) {
  console.log(data.toString())
}) // 실행 결과

process.stderr.on('data', function(data) {
  console.log(data.doString())
}) // 실행 에러
```

### 3.6 파일 시스템 접근하기
fs 모듈!!!

```js
const fs = require('fs');

fs.readFile('./readme.txt', (err, data) => {
  if (err) {
    throw err;
  }
  console.log(data); // Buffer로 찍힘
  console.log(data.toString());
})
```

* readFile의 결과물은 버퍼라는 형식으로 제공된다.
* fs는 기본적으로 콜백 형식의 모듈이다
  
```js
const fs = require('fs').promises;

fs.readFile('./readme.txt')
  .then((data) => {
    console.log(data);
    console.log(data.toString())
  })
  .catch((err) => {
    console.error(error);
  })
```

* 동기 - 블로킹 => 백그라운드 작업이 완료되었는지 계속 체크해야하고 그동안 다른 작업을 하지 못한다.
* 비동기 - 논블로킹 => 백그라운드 작업 완료 상관없이 자기 자신 작업 계속 진행함

fs 모듈 동기적으로 처리하기 (fs.readFileSync)
```js
const fs = require('fs');

console.log('start')
let data = fs.readFileSync('./readme2.txt');
console.log('number1', data.toString());
let data = fs.readFileSync('./readme2.txt');
console.log('number2', data.toString());
let data = fs.readFileSync('./readme2.txt');
console.log('number3', data.toString());
```
=> 요청이 수백개 들어왔을때 밑에 작업이 계속 기다리고 있어야 하므로 문제가 생긴다.

비동기 메서드를 사용하되 순서를 유지해보자!!
```js
const fs = require('fs');

console.log('start')
fs.readFile('./readme2.txt', (err, data) => {
  if (err) {
    throw err;
  }
  console.log('number1', data.toString());
  fs.readFile('./readme2.txt', (err, data) => {
    if (err) {
      throw err;
    }
    console.log('number2', data.toString());
    fs.readFile('./readme2.txt', (err, data) => {
    if (err) {
      throw err;
    }
    console.log('number3', data.toString());
  })
})
```

2. 버퍼와 스트림 이해하기
영상을 로딩할 때는 버퍼링 한다고 하고 영상을 실시간으로 송출할 때는 스트리밍 한다고 한다.
버퍼링은 영상을 재생할 수 있을때 까지 데이터를 모으는 동작
스트리밍은 방송인의 컴퓨터에서 시청자의 컴퓨터로 영상 데이터를 조금씩 전송하는 동작

`Buffer.toString()` : 버퍼를 문자열로 바꿔줌

100mb 파일을 읽을때 100mb의 버퍼를 만들어 이용하지 말고 1mb의 버퍼를 100번 전송하자!!! 
기존의 방식대로면 버퍼의 크기가 커서 파일 크기가 크면 메모리를 너무 많이 차지함

```js
const fs = require('fs');
const readStream = fs.createReadStream('./readme.txt', { highWaterMark: 16 });
const data = []

readStream.on('data', (chunk) => {
  data.push(chunk);
  console.log('data: ', chunk, chunk.length)
})

readStream.on('end', () => {
  console.log('end', Buffer.concat(data).toString())
})

readStream.on('error', (err) => {
  console.log('error', err);
})
```

한 파일을 읽어서 바로 다른 파일에 저장 때려버리자(pipe 개념)
```js
const fs = require('fs');

const readStream = fs.createReadStream('readme4.txt');
const writeStream = fs.createWriteStream('writeme3.txt');
readStream.pipe(writeStream);
```

4. 스레드풀 알아보기

노드에서는 멀티 스레드를 쓸수 있다. 경우는 두가지 인데 노드 자체적으로 사용하거나(스레드 풀) 워커스레드 사용하는 방식이다. 여기서는 스레드풀 관련 알아보자

crypto, zlib, dns.lookup 등이 스레드풀 사용한다.

스레드풀을 직접 컨트롤할 수는 없지만 개수를 조절할 수는 있다.
이때 자신의 코어 개수와 같아야 효과가 좋다.
`process.env.UV_THREADPOOL_SIZE`


> 맥/리눅스에서 프로세스 종료하기   
> `lsof -i tcp:포트`   
> `kill -9 포트`   

