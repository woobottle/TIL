# 4. http 모듈로 서버 만들기

### 4.1 요청과 응답 이해하기

```js
const http = require('http');

http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<h1>Hello Node!</h1>');
  res.end('<p>Hello Server!</p>')
})
.listen(8080, () => {
  console.log('8080')
})
```

```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<h1>Hello Node!</h1>');
  res.end('<p>Hello Server!</p>')
})
.listen(8080, () => {
  console.log('8080')
})


server.on('listening', () => {
  console.log('server listening')
})
server.on('error', (err) => {
  console.error(err);
})
```

요청에는 무조건 응답을 보내야 한다!! 보내지 않으면 timeout 일어남

### 4.2 REST와 라우팅 사용하기

REST(REpresentational State Transfer) => 서버의 자원을 정의하고 자원에 대한 주소를 지정하는 방법

GET, POST, PUT, PATCH, DELETE, OPTIONS

```js
const http = require('http');
const fs = require('fs').promises;

http.createServer(async (req, res) => {
  try {
    console.log(req.method, req.url);
    if (req.method === 'GET') {
      if (req.url === '/') {
        const data = await fs.readFile('./restFront.html');
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
        return res.end(data);
      } else if (req.url === '/about') {
        const data = await fs.readFile('./about.html');
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
        return res.end(data);
      }
      try {
        const data = await fs.readFile(`.${req.url}`);
        return res.end(data);
      } catch (err) {

      }
    }
    res.writeHead(404);
    return res.end('Not FOUNd');
  } catch (err) {
    console.error(err);
    res.writeHead(500, { 'Content-Type': 'text/html; charset=utf-8'});
    res.end(err.message);
  }
})
.listen(8082, () => {
  console.log(8082)
})
```

### 4.3 쿠키와 세션 이해하기

쿠키: 키-값의 쌍, 유효기간이 존재   
브라우저에서 서버로 요청을 보낼때 자동으로 동봉이 됨   
서버는 요청에 들어 있는 쿠키를 읽어서 사용자가 누구인지 파악.   

브라우저는 쿠키가 있다면 자동으로 동봉해서 보내주므로 따로 처리할 필요 x   
서버에서 브라우저로 쿠키를 보낼때만 코드를 작성하여 처리하면 된다   

```js
const http = require('http');

http.createServer((req, res) => {
  console.log(req.url, req.headers.cookie);
  res.writeHead(200, { 'Set-Cookie': 'mycookie=test' });
  res.end('Hello Cookie')
})
.listen(8083, () => {
  console.log(8083)
})
```

```js
const http = require('http');
const fs = require('fs').promises;
const url = require('url');
const qs = require('querystring');

const parseCookies = (cookie = '') => 
  cookie
    .split(';')
    .map(v => v.split('='))
    .reduce((acc, [k,v]) => {
      acc[k.trim()] = decodeURIComponent(v);
      return acc;
    }, {}); 

http.createServer(async (req, res) => {
  const cookies = parseCookies(req.headers.cookie);

  if (req.url.startsWith('/login')) {
    const { query } = url.parse(req.url);
    const { name } = qs.parse(query);
    const expires = new Date();

    expires.setMinutes(expires.getMinutes() + 5);
    res.writeHead(302, {
      Location: '/',
      'Set-Cookie': `name=${encodeURIComponent(name)}; Expires=${expires.toGMTString()}; HttpOnly; Path=/`,
    });
    res.end();
  } else if (cookies.name) {
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
    res.end(`${cookies.name}`)
  } else {
    try {
      const data = await fs.readFile('./cookie2.html');
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
      res.end(data);
    } catch (err) {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
      res.end(err.message);
    }
  }
})
.listen(8084, () => {
  consoel.log(8084);
})
```

* 쿠키명=쿠키값: 기본적인 쿠키의 값
* Expires=날짜: 만료기한
* Max-age=초: expire과 비슷, 날짜 대신 초 입력
* Domain=도메인명: 쿠키가 전송될 도메인을 특정
* Path=URL: 쿠키가 전송될 URL특정 가능(기본값은 '/', 이 경우 모든 url에서 쿠키 전송 가능)
* Secure: HTTPS일 경우에만 쿠키가 전송
* HttpOnly: 설정 시 자바스클비트에서 쿠키에 접근할 수 없음(쿠키 조작 방지하기 위해 설정하는 것이 좋음)

```js
const http = require('http'); // commonjs식 모듈 방식
const js = require('fs').promises;
const url = require('url');
const qs = require('querystring');

const parseCookies = (cookie = '') => 
  cookie
    .split(';')
    .map(v => v.split('='))
    .reduce((acc, [k ,v]) => {
      acc[k.trim() = decodeURIComponent(v)]
      return acc
    }, {});

const session = {};

http.createServer(async (req, res) => {
  const cookies = parseCookies(req.headers.cookie);
  if (req.url.startsWith('/login')) {
    const { query } = url.parse(req.url);
    const { name } = qs.parse(query);
    const expires = new Date();
    expires.setMinutes(expires.getMinutes() + 5);
    const uniqueInt = Date.now();
    session[uniqueInt] = {
      name,
      expires,
    };
    res.writeHead(302, {
      Location: '/',
      'Set-Cookie': `session=${uniqueInt}; Expires=${expires.toGMTString()}; HttpOnly; Path=/,`
    });
    res.end();
  } else if (cookies.session && session[cookies.session].expires > new Date()) {
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
    res.end(`${session[cookies.session],name}`)
  }
})
```

세션 => 쿠키의 보안성을 보완하고자 임시값으로 세팅하고 세션 아이디로만 소통할수 있도록 하는 부분    
쿠키에 민감한 정보를 가지고 있으면 브라우저에 그대로 노출됨   
쿠키를 사용하지 않아도 되지만 보통 쿠키를 사용     
실제 배포용 서버에서는 세션을 레디스나 멤캐시드와 같은 데이터베이스에 저장


### 4.4 https와 http2

https 띄우기
```js
const https = require('https');
const fs = require('fs');

https.createServer({
  cert: fs.readFileSync('도메인 인증성 경로'),
  key: fs.readFileSynce('도메인 비밀키 경로'),
  ca: [
    fs.readFileSync('상위 인증서 경로'),
    fs.readFileSync('상위 인증서 경로'),
  ],
}, (req, res) => {

})
.listen(443, () => {
  console.log(443)
})
```


### 4.5 cluster
=> 싱글 프로세스로 동작하는 노드를 cpu 코어를 모두 사용할 수 있게 해주는 모듈     
* 포트를 공유하는 노드 프로세스를 여러 개 둘 수도 있음
* 요청이 많이 들어왔을 때 병렬로 실행된 서버의 개수만큼 요청이 분산되게 할 수 있다.