# 4. http 모듈로 서버 만들기

### 4.1 요청과 응답 이해하기

```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8'});
  res.write('<h1>Hello Node</h1>');
  res.end('<p>Hello Server</p>');
});
server.listen(8080);

server.on('listening', () => {
  console.log('8080')
})
server.on('error', (error) => {
  console.log(error)
;})
```