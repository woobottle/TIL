# 11. 노드 서비스 테스트 하기

### 11.1 테스트 준비하기

```shell
npm i -D jest
```

```json
  "scripts": {
    "start": "nodemon app",
    "test": "jest"
  },
```

npm test로 실행하면 파일명에 test나 spec이 들어간 파일들을 모두 찾아 실행

```js
test('1 + 1은 2입니다.', () => {
  expect(1 + 1).toEqual(2);
});
```


### 11.2 유닛 테스트

```js
// route/middlewares.js
exports.isLoggedIn = (req, res, next) => {
  if (req.isAuthenticated()) {
    next();
  } else {
    res.status(403).send('로그인 필요')
  }
};

exports.isNotLoggedIn = (req, res, next) => {
  if (!req.isAuthenticated()) {
    next()
  } else {
    const message = encodeURIComponent('로그인한 상태입니다');
    res.redirect(`/?error=${message}`);
  }
}

// route/middlewares.test.js
const expectExport = require('expect');
const { isLoggedIn, isNotLoggedIn } = require('./middlewares');

describe('isLoggedIn', () => {
  const res = {
    status: jest.fn(() => res),
    send: jest.fn(),
  };
  const next = jest.fn();

  test('로그인되어 있으면 isLoggedIn이 next를 호출해야 함', () => {
    const req = {
      isAuthenticated: jest.fn(() => true),
    };
    isLoggedIn(req, res, next);
    expect(next).toBeCalledTimes(1);
  });

  test("로그인되어 있지 않으면 isLoggedIn이 에러를 응답해야 함", () => {
    const req = {
      isAuthenticated: jest.fn(() => false),
    };
    isLoggedIn(req, res, next);
    expect(res.status).toBeCalledWith(403);
    expect(res.send).toBeCalledWith('로그인 필요');
  });
})


describe("isNotLoggedIn", () => {
  const res = {
    redirect: jest.fn(),
  };
  const next = jest.fn();

  test("로그인되어 있으면 isNotLoggedIn이 에러를 응답해야 함", () => {
    const req = {
      isAuthenticated: jest.fn(() => true),
    };
    isNotLoggedIn(req, res, next);
    const message = encodeURIComponent('로그인한 상태입니다');
    expect(res.redirect).toBeCalledWith(`/?error=${message}`);
  });

  test("로그인되어 있지 않으면 isNotLoggedIn이 next를 호출해야 함", () => {
    const req = {
      isAuthenticated: jest.fn(() => false),
    };
    isNotLoggedIn(req, res, next);
    expect(next).toBeCalledTimes(1);
  });
});
```


실제 데이터베이스와 연결을 해줘야 하는 경우 mock을 이용하여 테스트환경에서 접근할 수 있게 해주어야 한다.
```js
jest.mock('../models/user');
const User = require('../models/user');
const { addFollowing } = require("./user")

describe('addFolowing', () => {
  const req = {
    user: { id: 1 },
    params: { id: 2 },
  };
  const res = {
    status: jest.fn(() => res),
    send: jest.fn(),
  };
  const next = jest.fn();

  test('사용자를 찾아 팔로잉을 추가하고 success를 응답해야 함', async () => {
    User.findOne.mockReturnValue(Promise.resolve({
      addFollowing(id) {
        return Promise.resolve(true); // Promise를 반환해야 다음 await이 호출될 수 있다.
      }
    }));
    await addFollowing(req, res, next);
    expect(res.send).toBeCalledWith('success');
  })

  test("사용자를 못 찾으면 res.status(404).send('no user')", async () => {
    User.findOne.mockReturnValue(null);
    await addFollowing(req, res, next);
    expect(res.status).toBeCalledWith(404);
    expect(res.send).toBeCalledWith('no user');
  });

  test('DB에서 에러가 발생하면 next(error) 호출함', async () => {
    const error = '테스트용 에러';
    User.findOne.mockReturnValue(Promise.reject(error))
    await addFollowing(req, res, next);
    expect(next).toBeCalledWith(error);
  })
})
```


### 11.3 테스트 커버리지

```json
"scripts": {
  "coverage": "jest --coverage"
}
```

```shell
npm run coverage
```

<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F0da84dd8-efc7-484d-9b63-3c40b06260fd%2FUntitled.png?table=block&id=cf1b89ff-fe34-4688-8fa3-dd75a76c7777&spaceId=359809db-cb83-47c2-9cce-0c45f96418ab&width=2000&userId=56059f96-1ce0-4d35-87f6-3200db26ea2a&cache=v2">

user.js
```js
const Sequelize = require('sequelize');

module.exports = class User extends Sequelize.Model {
  static init(sequelize) {
    return super.init(
      {
        email: {
          type: Sequelize.STRING(40),
          allowNull: true,
          unique: true,
        },
        nick: {
          type: Sequelize.STRING(15),
          allowNull: false,
        },
        password: {
          type: Sequelize.STRING(100),
          allowNull: true,
        },
        provider: {
          type: Sequelize.STRING(10),
          allowNull: false,
          defaultValue: "local",
        },
        snsId: {
          type: Sequelize.STRING(30),
          allowNull: true,
        },
      },
      {
        sequelize,
        timestamps: true,
        underscored: false,
        modelName: "User",
        tableName: "users",
        paranoid: true,
        charset: "utf8",
        collate: "utf8_general_ci",
      }
    );
  }
  static associate(db) {
    db.User.hasMany(db.Post);
    db.User.belongsToMany(db.User, {
      foreignKey: "followingId",
      as: "Followers",
      through: "Follow",
    });
    db.User.belongsToMany(db.User, {
      foreignKey: "followerId",
      as: "Followings",
      through: "Follow",
    });
  }
};
```

user.test.js
```js
const Sequelize = require('sequelize');
const User = require('./user');
const config = require('../config/config')['development'];
const sequelize = new Sequelize(
  config.database, config.username, config.password, config,
)

describe('User 모델', () => {
  test('static init 메서드 호출', () => {
    expect(User.init(sequelize)).toBe(User);
  })
  test('static associate 메서드 호출', () => {
    const db = {
      User: {
        hasMany: jest.fn(),
        belongsToMany: jest.fn(),
      },
      Post: {}
    };
    User.associate(db);
    expect(db.User.hasMany).toHaveBeenCalledWith(db.Post);
    expect(db.User.belongsToMany).toHaveBeenCalledTimes(2);
  })
})
```

테스트 커버리지를 높이는 것에 집착하기 보다는 필요한 부분 위주로 올바르게 테스트하는 것이 좋다.

### 11.4 통합 테스트
라우트를 통째로 테스트

```shell
npm i -D supertest
```

supertest를 사용하기 위해서는 app 객체를 사용하여야 한다.
supertest를 이용 app을 이용하여 post 요청

```js
const request = require('supertest');
const { sequelize } = require('../models');
const app = require('../app');

beforeAll(async () => {
  await sequelize.sync();
});

describe('Post /login', () => {
  test('로그인 수행', async (done) => {
    request(app)
      .post('/login')
      .send({
        email: 'zerocho@gmail.com',
        password: 'nodejsbook',
      })
      .expect('Location', '/')
      .expect(302, done);
  })
})
```

테스트 종료 시 데이터를 정리하는 코드를 추가해야 한다.
```js
afterAll(async () => {
  await sequelize.sync({ force: true });
});
```

### 11.5 부하 테스트

```shell
npm i -D artillery
```

서버 키고 나서
```shell
npx artilery quick --count 10 -n 50 http://localhost:8001
```

혹은 artillery 참고해서 파일 만들어서 해당 파일 실행하면 됨