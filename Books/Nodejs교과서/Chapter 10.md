# 10. 웹 API 서버 만들기

### JWT 토큰으로 인증하기

JWT  
* 헤더: 토큰 종류와 해시 알고리즘에 대해 들어있음
* 페이로드: 토큰의 내용물이 인코딩된 부분
* 시그니처: 서명을 통해 토큰이 변조되었는지 여부를 확인할 수 있다.

jwt 페이로드의 내용이 노출되고 있는 이유는 ?? => 내용이 들어있기 때문이다! 매번 내용을 가지고 위조 되었는지를 판단해야 하므로!
랜덤한 토큰을 받으면 토큰의 주인이 누구인지, 그 사람의 권한은 무엇인지를 매 요청마다 확인해야 한다. (중요한 내용을 jwt에 담으면 안된다.)
Jwt의 핵심은 내용은 깔 수 있지만 서명을 통해 변조 되었는지를 판단하는 것!!

```shell
npm i jsonwebtoken
```

책에서 설명하는 jwt token을 사용하는 이유는 페이로드의 정보를 가지고 디비에 다녀오지 않아서 이다. token이 위조되지 않았는지만 판단하고 바로 다음 router로 가버린다.   
세션을 이용한 이전의 경우에는 session의 정보로 디비를 한번 조회하고 있는지 판단을 했었다.   
나는 이전에 jwt를 사용하고 동시에 디비 조회도 했었었다.    
나쁜 방식은 아닌데 뭔가 혼합해서 쓰고 있었던 것 같다.


### 사용량 제한 구현하기
```shell
npm i express-rate-limit
```

```js
exports.apiLimiter = new RateLimit({
  windowMs: 60 * 1000,
  max: 1,
  handler(req, res) {
    res.status(this.statusCode).json({
      code: this.statusCode,
      message: '1분에 한 번만 요청할 수 있습니다',
    });
  };
});

exports.deprecated = (req, res) => {
  res.status(410).json({
    code: 410,
    message: '새로운 버전이 나왔습니다',
  })
}
```

```js
router.get('/test', verifyToken, apiLimiter, (req, res) => {
  res.json(req.decoded)
})
```

### cors 에러

브라우저에서 다른 도메인의 서버로 요청을 보냈을때 발생하는 에러 (Accept-Control-Allow-Origin)이라는 헤더가 없다고 에러 발생   
서버 to 서버는 발생하지 않음   

Options 메서드는 실제 요청을 보내기 전에 서버가 이 도메인을 허용하는지 체크하는 역할  


```shell
npm i cors
```

```js
router.use(cors({
  credentials: true, // 이 옵션을 활성화해야 다른 도메인 간에 쿠키가 공유됨!!!!!
})
```

axios에서도 withCredentials: true 옵션을 줘서 요청을 보내야 한다.

```js
const router = express.Router();

router.use(async (req, res, next) => {
  const domain = await Domain.findOne({
    where: { host: url.parse(req.get('origin')).host },
  });
  if (domain) {
    cors({
      origin: req.get('origin'),
      credentials: true,
    })(req, res, next)
  } else {
    next()
  }
})
```
req.get('origin') 이 친구만 요청을 허용해 준다. 여러개의 도메인을 허용하고 싶다면 배열로 작성


```js
cors() === cors()(req, res, next)
```