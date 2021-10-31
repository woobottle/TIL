# 12. 웹 소켓으로 실시간 데이터 전송하기

### 12.1 웹 소켓 이해하기

Socket.IO는 웹 소켓을 이용한 라이브러리이다.    
웹 소켓 => HTML5에 새로 추가된 스펙, 실시간 양방향 데이터 전송을 위한 기술, Http와 다르게 ws 프로토콜을 사용함   
인터넷 익스플로러 등에서 웹소켓 프로토콜을 지원해주지 않아서 socket.io 와 같은 라이브러리르 사용하곤 한다.   
Http 프로토콜과 포트를 공유할수 있어서 따로 포트 열어줄 필요 없음


웹 소켓 등장전 방식 => 폴링 방식이용(클라이언트에서 서버로 계속 새로운 업데이트 있나 정보 요청)

서버센트(Server Sent Event) 이벤트 => 처음에 한번만 연결하면 서버에서 클라이언트로 지속적으로 데이터를 보냄(클라이언트에서 서버로 데이터를 보낼순 없음), 기존의 서버는 요청이 있어야 응답을 내주는 형식이다!!!


```js
const webSocket = require('./socket');

const server = app.listen(app.get('port'), () => {
  console.log("12321");
})

webSocket(server);
```

```js
const WebSocket = require('ws');

module.exports = (server) => {
  const wss = new WebSocket.Server({ server });

  wss.on('connection', (ws, req) => {
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress; // 클라이언트의 ip를 알아내는 유용한 방법
    console.log('새로운 클라이언트 접속', ip);
    ws.on('message', (message) => {
      console.log(message)
    });
    ws.on('error', () => {
      console.log('error')
    });
    ws.on('close', () => {
      console.log(ip);
      clearInterval(ws.interval);
    });

    ws.interval = setInterval(() => {
      if (ws.readyState === ws.OPEN) {
        ws.send('서버에서 클라이언트로 메시지를 보냅니다')
      } 
    }, 3000);
  })
}
```

클라이언트 쪽
```js
const webSocket = new WebSocket('ws://localhost:8005');
webSocket.onopen = function() {
  console.log('서버와 웹소켓 연결 성공');
}
webSocket.onmessage = function(event) {
  console.log(event.data);
  webSocket.send('클라이언트에서 서버로 답장을 보냅니다');
}
```

### 12.3 Socket.IO 사용하기

```shell
npm i socket.io@2
```

```js
const SocketIO = require('socket.io');

module.exports = (server) => {
  const io = SocketIO(server, { path: '/socket.io' });


  io.on('connection', (socket) => { // 웹 소켓 연결 시
    const req = socket.request;
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    socket.on('disconnect', () => {
      cleearInterval(socket.interval);
    });
    socket.on('error', (err) => {
      console.log(err)
    });
    socket.on('reply', (data) => { // 클라이언트로부터 메시지 수신 시
      console.log(data)
    });
    socket.interval = setInterval(() => {
      socket.emit('news', 'Hello Socket.IO')
    }, 3000);
  })
}
```

클라이언트
```html
<script>
  const socket = io.connect('http://localhost:8005', {
    path: '/socket.io',
  });
  socket.on('news', function (data) {
    socket.emit('news', 'Hello Node Js');
  })
</script>
```

Socket.io 는 먼저 폴링 방식으로 서버와 연결, 이후에 웹 소켓이 가능하다면 웹 소켓으로 업그레이드, 웹 소켓을 지원하지 않는 브라우저는 폴링 방식으로 변경됨

socket.io 에는 방(room)이라는 개념이 있다.
같은 네임스페이스 안에서도 같은 방에 들어있는 소켓끼리만 데이터를 주고받을 수 있다. (join, method 이용)
```js
const SocketIO = require('socket.io');

module.exports = (server, app) => {
  const io = new SocketIO(server, { path: '/socket.io' });
  app.set('io', io);
  const room = io.of('/room');
  const chat = io.of('/chat');

  room.on('connection', (socket) => {
    console.log('room 네임스페이스에 접속')
    socket.on('disconnect', () => {
      console.log('room 네임스페이스 접속 해제');
    })
  });

  chat.on('connection', (socket) => {
    const req = socket.request;
    const { headers: {referer} } = req;
    const roomId = referer
      .split('/')[referer.split('/').length - 1]
      .replace(/\?.+/, '');
    socket.join(roomId);

    socket.on('disconnect', () => {
      socket.leave(roomId);
    })
  })
}
```


### 12.7 핵심정리
* 웹 소켓과 http는 같은 포트를 사용할 수 있으므로 따로 포트를 설정할 필요가 없습니다.
* 웹 소켓은 양방향 통신이므로 서버뿐만 아니라 프런트엔드 쪽 스크립트도 사용해야 합니다.
* Socket.IO 를 사용하면 웹 소켓을 지원하지 않는 브라우저에서까지 실시간 통신을 구현할 수 있습니다.
* Socket.IO 네임스페이스와 방 구분을 통해 실시간 데이터를 필요한 사용자에게만 보낼 수 있습니다.
* app.set('io', io)로 소켓 객체를 익스프레스와 연결하고, req.app.get('io')로 라우터에서 소켓 객체를 가져오는 방식을 기억해 둡시다.
* 소켓 통신과 함께 데이터베이스 조작이 필요한 경우, 소켓만으로 해결하기보다는 HTTP 라우터를 거치는 것이 좋습니다.