# 16. 서버리스 노드 개발

### 16.1 서버리스 이해하기

서버리스는 클라우드 서비스가 대신 관리해주므로 개발자나 운영자가 서버를 관리하는 데 드는 부담이 줄어든다는 의미

AWS => 람다, API Gateway, s3
GCP => 앱 엔진, 파이어베이스, 클라우드 펑션스, 클라우드 스토리지

### 16.2 s3 사용 하기

s3 버킷 정책
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AddPerm",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
      ],
      "Resource": "arn:aws:s3::nodebird/*",
    }
  ]
}
```

> s3를 사용하면 데이터를 저장할 때와 데이터를 로드할 때 과금이 든다

### 16.3 aws lambda 사용하기

이미지 리사이징은 cpu를 많이 잡아먹므로 람다로 분리했다.

사진이 s3에 올라가고 s3에 올라가게 되면 람다 트리거가 동작해서 이미지가 리사이징 된다.


aws-upload/index.js
handler 함수가 람다 호출시 실행되는 함수이다
```js
const AWS = require('aws-sdk');
const sharp = require('sharp');

const s3 = new AWS.S3();

exports.handler = async (event, context, callback) => {
  const Bucket = event.Records[0].s3.bucket.name;
  const Key = decodeURIComponent(event.Records[0].s3.object.key);
  const filename = Key.split("/")[Key.split('/').length - 1]
  const ext = Key.split('.')[Key.split('.').length - 1].toLowerCase()
  const requiredFormat = ext === 'jpg' ? 'jpeg' : ext;
  // sharp 에서는 jpg 대신에 jpeg 사용
  console.log('name', filename, 'ext', ext);

  try {
    const s3Object = await s3.getObject({ Bucket, Key }).promise();
    console.log('original', s3Object.Body.length);

    const resizedImage = await sharp(s3Object.Body)
      .resize(200, 200, { fit: 'inside' })
      .toFormat(requiredFormat)
      .toBuffer();
    
    await s3.putObject({
      Bucket,
      Key: `thumb/${filename}`,
      Body: resizedImage,
    }).promise();

    return callback(null, `thumb/${filename}`) // 완료 여부를 람다에게 알리는 것, 첫번째 인자는 에러, 두번째 인자는 반환값
  } catch (error) {
    console.error(error);
    return callback(error);
  }
}
```



nodebird/routes/post.js
```js
AWS.config.update({
  accessKeyId: process.env.S3_ACCESS_KEY_ID,
  secretAccessKey: process.env.S3_SECRET_ACCESS_KEY,
  region: 'ap-northeast-2',
});
const upload = multer({
  storage: multerS3({
    s3: new AWS.S3(),
    bucket: 'nodebird',
    key(req, file, cb) {
      cb(null, `original/${Date.now()}${path.basename(file.originalname)}`);
    },
  }),
  limits: { fileSize: 5 * 1024 * 1024 },
});
router.post('/img', isLoggedIn, upload.single('img'), (req, res) => {
  console.log(req.file);
  const originalUrl = req.file.location;
  const url = originalUrl.replace('/\/original\//', '/thumb/')
  res.json({ url, originalUrl })
})
```

img 태그에는 onerror가 있어서 error 발생시 트리거 된다.
<img src="{{twit.img}}" onerror="this.src = this.src.replace(/\/thumb\//, '/original/')"/>