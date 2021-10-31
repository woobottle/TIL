# 15. AWS와 GCP로 배포하기

### 15.1 서비스 운영을 위한 패키지

* morgan   
=> 로깅을 위한 패키지, 서버에 로그를 남긴다    
배포 환경일 때는 morgan을 combined 모드로, 개발 환경일때는 dev 모드로    

* express-session
```js
app.use(cookieParser(process.env.COOKIE_SECRET));

const sessionOption = {
  resave: false,
  saveUninitialized: false,
  secret: process.env.COOKIE_SECRET,
  cookie: {
    httpOnly: true,
    secure: false,
  }
};

if (process.env.NODE_ENV === 'production') {
  sessionOption.proxy = true;
}
```

* sequelize(orm)

const/config.js  
```js
require('dotenv').config();

module.exports = {
  development: {
    username 'root',
    password: 'dfsdf',
    database: 'test',
    host: '',
    dialect: '',
  },
  test: {
    username 'root',
    password: 'dfsdf',
    database: 'test',
    host: '',
    dialect: '',
  },
  production: {
    username 'root',
    password: 'dfsdf',
    database: 'test',
    host: '',
    dialect: '',
  }
}
```

* cross-env    
=> 윈도우에서 NODE_ENV=production 과 같은 노드 환경변수 세팅 동작할수 있도록 도와주는 패키지

* sanitize-html   
=> 이거 설치하면 xss(cross site scription)을 막을 수 있다.   
내용이 들어왓을때 script의 내용들은 전부 필터링 해준다

xss -> 게시글을 등록시 스크립트 내용을 포함시켜서 다른사람이 게시글을 봤을때 해당 스크립트가 실행되게 한다.

* csurf   
csrf => 사용자가 의도치 않게 공격자가 의도한 행동을 하게 만드는 공격, 특정 페이지에 방문할 때 저절로 로그아웃 되거나, 게시글이 써지는 현상을 유도할 수 있다.    
csurf 패키지는 csrf 토큰을 쉽게 발급하거나 검증할 수 있게 해준다. (csrf 토큰은 csrf를 막기위해 내가 한 행동이다 라는 것을 인증하기 위해 이용함)   


```js
const csrf = require('csurf');
const csrfProtection = csrf({ cookie: true });

app.get('/form', csrfProtection, (req, res) => {
  res.render('csrf', { csrfToken: req.csrfToken() });
});

app.post('/form', csrfProtection, (req, res) => {
  res.send('ok')
})
```

* pm2    
가장 큰 기능은 서버가 에러로 인해 꺼졌을 때 서버를 다시 켜주는 기능,   
멀티 프로세싱, 클라이언트로부터 요청이 올 때 알아서 요청을 여러 노드 프로세스에 고르게 분배해줌 `pm2 start app.js -i 0`    
멀티 스레딩이 아니므로 서버의 메모리 같은 자원을 공유하지는 못한다. => 프로세스 간에 세션이 공유되지 않게 되므로 로그인 후 새로고침 했을때 다른 프로세스에서 요청을 받으면 로그인이 끊어져 버림

서버를 재시작하고 싶으면 `npx pm2 reload all` => 서버가 다운타임(서버가 중지되어 클라이언트가 접속할 수 없는 시간) 거의 없이 재시작 됨

* winston    
console.log, console.error를 사용하면 서버가 꺼지면 날라가버림, 이 로그들을 파일이나 다른 데이터베이스에 저장해야 한다 -> 윈스턴으로 가자

```js
const { createLogger, format, transports } = require('winston');

const logger = createLogger({
  level: 'info',
  format: format.json()
  transports: [
    new transports.File({ filename: 'combined.log' }),
    new transports.File({ filename: 'error.log', level: 'error' }),
  ],
});

if (process.env.NODE_ENV !== 'production') {
  logger.add(new transports.Console({ format: format.simple()) }))
}

module.exports = logger;
```

* helmet
서버의 보안 취약점을 보완해주기 위해 사용, 웹 서버에서 헤더 설정을 바꿔줌 (보안의 취약점에 도움이 될 수 있다)
<https://dlwlrma0203.tistory.com/65>

* connect-redis
멀티 프로세스 간 세션 공유를 위해 레디스와 익스프레스를 연결해주는 패키지

* nvm, n
윈도우에서는 nvm, 리눅스나 맥에서는 n `sudo npm i -g n`