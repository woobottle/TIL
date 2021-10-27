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
  const url = originalUrl.replace(/\/original\//, '/thumb/')
  res.json({ url, originalUrl })
})