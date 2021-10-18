# 6. 익스프레스 웹 서버 만들기

### 6.1 익스프레스 프로젝트 시작하기
`npm -i D nodemon` 서버코드에 수정사항이 생길때마다 서버를 자동으로 재시작 해줌

app.js
```js
const express = require('express');

const app = express()
app.set('port', process.env.PORT || 3000);

app.get('/', (req, res) => {
  res.send('Hello, Express');
});

app.listen(app.get('port'), () => {
  console.log(app.get('port'), '번 포트에서 대기중')
})
```

### 6.2 자주 사용하는 미들웨어
미들웨어 => 익스프레스의 핵심, 요청과 응답의 중간에 위치하여 미들웨어라고 부름

```js
const express = require('express');

const app = express()
app.set('port', process.env.PORT || 3000);

app.use((req, res, next) => {
  console.log('모든 요청에 다 실행됩니다');
  next();
})

app.get('/', (req, res, next) => {
  console.log('GET / 요청에서만 실행됩니다.')
  next();
}, (req, res) => {
  throw new Error('에러는 에러 처리 미들웨어로 갑니다.')
});

app.use((err, req, res, next) => { // 에러처리 미들웨어
  console.error(err);
  res.status(500).send(err.message);
})

app.listen(app.get('port'), () => {
  console.log(app.get('port'), '번 포트에서 대기중')
})
```

|app.use(미들웨어)|모든 요청에서 미들웨어 실행|
|----|----|
|app.use('/abc', 미들웨어)|abc로 시작하는 요청에서 미들웨어 실행|
|app.post('/abc', 미들웨어)|abc로 시작하는 Post 요청에서 미들웨어 실행|


```shell
npm i morgan cookie-parser express-session dotenv
```
dotenv를 제외한 모든 패키지는 미들웨어

```js
const express = require('express');
const morgan = require('morgan');
const cookieParser = require('cookie-parser');
const session = require('express-session');
const dotenv = require('dotenv');
const path = require('path')

dotenv.config()
const app = express()
app.set('port', process.env.PORT || 3000);

app.use(morgan('dev'))
app.use('/', express.static(path.join(__dirname, 'public')));
app.use(express.json());
app.use(express.urlencoded({ extended: false }))
app.use(cookieParser(process.env.COOKIE_SECRET));
app.use(session({
  resave: false,
  saveUninitialized: false,
  secret: process.env.COOKIE_SECRET,
  cookie: {
    httpOnly: true,
    secure: false,
  },
  name: 'session-cookie',
}))
```

##### 6.2.1 morgan
로그에 대한 정보들 콘솔에 찍힘,  
인수로 dev, combined, common, short, tiny 등이 있다.    
개발 환경에서는 dev, 배포 환경에서는 combined를 선호함

##### 6.2.2 static
정적인 파일들을 제공하는 라우터   
express에서 기본 제공
```js
app.use('/', express.static(path.join(__dirname, 'public')));
```

##### 6.2.3 body-parser
요청의 본문에 있는 데이터를 해석해서 req.body 객체로 만들어주는 미들웨어   
보통 폼 이터나 Ajax 요청의 데이터를 처리, 멀티파트(이미지, 동영상, 파일) 데이터는 multer 모듈을 사용함

```js
app.use(express.json())
app.use(express.urlencoded({ extended: false })) 
```
express 높은 버전부터 body-parser 기본 제공


```js
const bodyParser = require('body-parser');
app.use(bodyParser.raw());
app.use(bodyParser.text());
```

##### 6.2.4 cookie-parser
쿠키를 해석해서 req.cookies 객체로 만들어 버림   

쿠키 세팅하기
```js
res.cookie('name', 'woobottle', {
  expires: new Date(Date.now() + 900000),
  httpOnly: true,
  secure: true,
});
res.clearCookie('name', 'woobottle', { httpOnly: true, secure: true })
```

##### 6.2.5 express-session
세션 관리용 미들웨어, 세션은 사용자별로 req.session 객체 안에 유지됩니다.
```js
app.use(session({
  resave: false,
  saveUninitialized: false,
  secret: process.env.COOKIE_SECRET,
  cookie: {
    httpOnly: true,
    secure: false,
  },
  name: 'session-cookie',
}));
```

##### 6.2.6 미들웨어의 특성 활용하기

next를 호출해줘야 다음으로 넘어간다. 위에서 설치한 모듈들은 내부적으로 next를 호출하고 있어 아래와 같이 사용할 수 있다.
```js
app.use(
  morgan('dev'),
  express.static('/', path.join(__dirname, 'public')),
  express.json(),
  express.urlencode({ extended: false }),
  cookieParser(process.env.COOKIE_SECRET),
)
```
next('route') => 다음 라우터로   
next(error) => 에러 핸들러로

```js
app.use((req, res, next) => {
  if (process.env.NODE_ENV === 'production') {
    morgan('combined')(req, res, next)
  } else {
    morgan('dev')(req, res, next)
  }
})
```


##### 6.2.7 multer
이미지, 동영상 등을 비롯한 여러 가지 파일들을 멀티파트 형식으로 업로드할 때 사용하는 미들웨어
```js
const multer = require('multer');

const upload = multer({
  storage: multer.diskStorage({
    destination(req, file, done) {
      done(null, 'uploads/');
    },
    filename(req, file, done) {
      const ext = path.extname(file.originalname);
      done(null, path.basename(file.originalname, ext) + Date.now() + ext);
    },
  }),
  limits: { fileSize: 5 * 1024 * 1024 },
})
```

업로드 폴더 있는지 없는지 체크
```js
const fs = require('fs');

try {
  fs.readdirSync('uploads');
} catch (err) {
  console.error('uploads 폴더가 없어 폴더를 생성합니다');
  fs.mkdirSync('uploads')
}
```

파일 하나 업로드
```js
app.post('/upload', upload.single('image'), (req, res) => {
  console.log(req.file, req.body);
  res.send('ok')
})
```

파일 복수개 업로드
```js
app.post('/upload', upload.fields([{name: 'image1'}, {name: 'image2'}]), (req, res) => {
  console.log(req.file, req.body);
  res.send('ok')
})
```

### 6.3 Router 객체로 라우팅 분리하기
익스프레스를 사용하는 이유 중 하나는 바로 라우팅을 깔끔하게 관리할 수 있다는 점입니다.

routes/index.js
```js
const express = require('express');

const router = express.Router();

router.get('/', (req, res) => {
  res.send('Hello, Express')
})

module.exports = router;
```

routes/user.js
```js
const express = require("express");

const router = express.Router();

router.get("/", (req, res) => {
  res.send("Hello, User");
});

module.exports = router;
```

app.js
```js

const indexRouter = require('./routes');
const userRouter = require('./routes/user');

const app = express()

app.use('/', indexRouter);
app.use('/user', userRouter);
```

### 6.4 req, res 객체 살펴보기

* req.app => req 객체를 통해 app 객체에 접근, req.app.get('port')
* req.body => body-parser가 요청의 본문을 해석한 객체
* req.cookies => cookie-parser 미들웨어가 만드는 쿠키를 해석한 객체(서명안된 쿠키들)
* req.ip => 요청 ip
* req.params
* req.query
* req.signedCookies => 서명된 쿠키들
* req.get(헤더이름)

<br>
<br>


* res.app
* res.cookie(키, 값, 옵션)
* res.clearCookie(키, 값, 옵션)
* res.end()
* res.json(JSON)
* res.redirect(주소)
* res.render(뷰, 데이터)
* res.send(데이터)
* res.sendFile(경로)
* res.set(헤더, 값)
* res.status(코드)

```js
res
  .status(201)
  .cookie('test', 'test')
  .redirect('/admin')
```

### 6.5 템플릿 엔진 사용하기

> ejs를 사용하지 않는 이유    
> 노드에는 ejs나 handlebars 같은 템플릿 엔진도 있지만    
> 레이아웃 기능이 없으므로 추천 x


##### 6.5.1 퍼그(제이드)

나중에 사용하게 되면 그때 보자


##### 6.5.2 넌적스

나중에 사용하게 되면 그때 보자