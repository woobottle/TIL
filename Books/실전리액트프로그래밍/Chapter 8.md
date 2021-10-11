# 8. 서버사이드 렌더링 그리고 Next.js

두 가지 이유로 서버사이드 렌더링이 필요하다
* 검색 엔진 최적화를 해야한다
* 빠른 첫 페이지 렌더링이 중요하다

구글을 제외한 다른 검색 엔진에서는 자바스크립트를 실행하지 않기 때문에 클라이언트 렌더링만 하는 사이트는 내용이 없는 사이트와 동일하게 처리된다.

```jsx
import React, { useState, useEffect } from 'react';
import Home from './Home';
import About from './About';

export default function App({ page }) {
  const [page, setPage] = useState(page);
  useEffect(() => {
    window.onpopstate = event => {
      setPage(event.state);
    };
  }, []);

  function onChangePage(e){ 
    const newPage = e.target.dataset.page;
    window.history.pushState(newPage, '', `/${newPage}`);
    setPage(newPage);
  }

  const PageComponent = page === 'home' ? Home : About;
  return (
    <div className="container">
      <button data-page="home" onClick={onChangePage}>
        Home
      </button>
      <button data-page="about" onClick={onChangePage}>
        About
      </button>
      <PageComponent />
    </div>
  );
}
```

1. SPA를 위해 onpoopstate 이벤트 처리 함수를 등록한다. 
2. 브라우저에서 뒤로가기 버튼을 클릭하면 onpopstate 함수가 호출된다.


### 서버사이드 렌더링 함수 사용해 보기: renderToString

리액트에서는 서버사이드 렌더링을 위해 다음 네개의 함수를 제공한다.

* renderToString
* renderToNodeStream
* renderToStaticMarkup
* renderToStaticNodeStream

맨 아래 두개는 정적 페이지를 렌더링할 때 사용된다.

`npm install express @babel/cli @babel/plugin-transform-modules-commonjs`

@babel/cli 패키지는 서버에서 사용될 자바스크립트 파일을 컴파일할 때 사용된다. 서버에서도 리액트의 jsx 문법으로 작성된 자바스크립트를 실행해야 하므로 바벨이 필요하다.

`@babel/plugin-transform-modules-commonjs` 는 esm으로 작성된 모듈 시스템을 commonjs로 변경하기 위해 설치
서버에서는 노드 환경에서 자바스크립트를 실행하기 때문에 commonjs 모듈 시스템이 필요하다


```javascript
import express from 'express';
import fs from 'fs';
import path from 'path';
import { renderToString } from 'react-dom/server'; // 1
import React from 'react';
import App from './App';

const app = express();
const html = fs.readFileSync(
  path.resolve(__dirname, '../dist/index.html'),
  'utf-8',
);
app.use('/dist', express.static('dist'));
app.get('/favicon.ico', (req, res) => res.sendStatus(204));
app.get('*', (req, res) => {
  const renderString = renderToString(<App pageName="home" />);
  const result = html.replace(
    '<div id="root"></div>',
    `<div id="root">${renderString}</div>`
  );
  res.send(result);
});
app.listen(3000);
```

1. react-dom/server 폴더 밑에 서버에서 사용되는 기능이 모여 있다.



## 넥스트 초급편

넥스트에서 모든 페이지 컴포넌트는 pages 폴더 밑에 만들어야 한다.
```javascript
function Page1() {
  return (
    <div>
      <p>This is home page</p>
    </div>
  );
}

export default Page1;
```

=> 파일 상단에 리액트 모듈을 가져오는 import 키워드가 보이지 않는다. 넥스트는 리액트 모듈을 자동으로 포함시켜 준다.


브라우저 캐싱을 최대로 활용하기 위해서는 파일의 내용이 변경되면 팡리의 경로도 변경되는 게 좋다. 웹팩의 file-loader를 사용해서 이 기능을 구현해 보자

```js
module.exports = {
  webpack: config => {
    config.module.rules.push({
      test: /.(png|jpg)$/,
      use: [
        {
          loader: 'file-loader',
          options: {
            name: '[path][name].[ext]?[hash]', // 쿼리 파라미터에 hash를 추가해서 파일의 내용이 변경될 때마다 파일의 경로도 수정되도록 한다.
            emitFile: false, // next는 static 폴더의 정적 파일을 그대로 서비스하기 때문에 파일을 복사할 필요가 없다.
            publicPath: '/',
          },
        },
      ],
    });
    return config;
  },
}
```

* 서버에서 생성된 데이터를 전달하기

넥스트에서는 getInitialProps라는 함수를 이용해서 페이지 컴포넌트로 속성값을 전달한다.
```js
import { callApi } from '../src/api';

Page2.getInitialProps = async ({ query }) => {
  const text = query.text || 'none'; // 쿼리에서 text를 뽑아냄
  const data = await callApi();
  return { text, data };
};

export default function Page2({ text, data }) {
  return (
    <div>
      <p>{text}</p>
      <p>{data}</p>
    </div>
  );
}
```

user-agent 정보 추출하기
```js
MyComponent.getInitialProps = async ({ req }) => {
  const userAgent = req ? req.headers['user-agent'] : navigator.userAgent;
}
```

req의 유무로 나뉜 이유는 서버에서 호출되는 경우와 클라이언트에서 호출되는 경우 두가지가 존재하기 때문이다.

* 페이지 이동하기

넥스트는 페이지 이동을 위해 Link 컴포넌트와 Router 객체를 제공한다.

```js
import { callApi } from '../src/api';
import Router from 'next/router';
import Link from 'next/link';

export default function Page2({ text, data }) {
  return (
    <div>
      <button onClick={() => Router.push('/page1')}>page1으로 이동</button>
      <Link href="/page3">
        <a>page3로 이동</a>
      </Link>
    </div>
  );
}
```

router 객체가 좀더 동적인 코드에 적합하다!!

* 에러 페이지 구현하기
pages폴더 밑에 _error.js 파일을 작성한다.

```js
ErrorPage.getInitialProps = ({ res, err }) => {
  const statusCode = res ? res.statusCode : err ? err.statusCode : null;
  return { statusCode };
};

export default function ErrorPage({ statusCode }) {
  return (
    <div>
      {statusCode === 404 && '페이지를 찾을 수 없습니다.'}
      {statusCode === 500 && '알 수 없는 에러가 발생했습니다.'}
      {!statusCode && '클라이언트에서 에러가 발생했습니다.'}
    </div>
  )
}
```

넥스트 고급편
-----

규모가 커지면
* 서버를 직접 띄워야 한다
* 여러 페이지 컴포넌트의 공통 기능을 분리하는 방법이 필요
* styled-components 등의 다른 패키지를 적용하는 방법도 고려해봐야 한다.
* 서버사이드 렌더링시 cpu 연산을 최소화 하는게 중요하다. 이때 렌더링 결과를 캐싱하거나 빌드 시 미리 렌더링하는 방법을 사용한다.

##### 페이지 공통 기능 구현하기

공통으로 띄우고 싶은 기능은 pages/_app.js 파일에 구현한다.
```jsx
import Link from 'next/link';

export default function MyApp({ Component, pageProps }) {
  return (
    <div>
      <Link href="/page1">
        <a>page1</a>
      </Link>
      <Link href="/page2">
        <a>page2</a>
      </Link>
      <Component {...pageProps}/>
    </div>
  );
}
```

1. Component는 현재 렌더링 하려는 페이지의 컴포넌트
2. pageProps 속성값은 해당 페이지의 getInitialProps 함수가 반환한 값

##### 넥스트에서의 코드 분할
넥스트는 기본적으로 페이지별로 번들 파일을 생성한다.

* 동적 임포트로 코드 분할하기
```js
import { callApi } from '../src/api';
import Router from 'next/router';

Page2.getInitialProps = async ({ query }) => {
  const text = query.text || 'none';
  const data = await callApi();
  return { text, data };
};

export default function Page2({ text, data }) {
  function onClick() {
    import('../src/sayHello').then(({ sayHello }) => console.log(sayHello()));
  }
  return (
    <div>
      <p>{text}</p>
      <p>{data}</p>
      <button onClick={() => Router.push('/page1')}>page1으로 이동</button>
      <button onClick={onClick}>sayHello</button>
    </div>
  );
}
```

동적 임포트를 사용하면 클라이언트 뿐만 아니라 서버를 위한 번들 파일도 생성이 된다.

* getInitialProps 함수에서 동적 임포트 사용하기
getInitialProps 함수는 두가지 경우가 존재한다. 서버에서 호출되는 경우 클라이언트에서 호출되는 경우 서버측에서 호출되는 경우는 자바스크립트 파일이 전송되지 않는다.

* 여러 페이지에 공통으로 사용되는 코드 분할하기
넥스트는 여러 페이지에서 공통으로 사용되는 모듈을 별도의 번들 파일로 분할한다.
한 곳에서만 쓰이는 파일은 따로 파일을 생성하지 않고 하지 않고 여러 곳에서 공통으로 쓰이면 별도의 파일로 생성한다.


##### 웹 서버 직접 띄우기
직접 서버를 띄우면 렌더링 결과를 캐싱할 수 있다.

```js
const express = require('express');
const next = require('next');

const port = 3000;
const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev }) 
const handle = app.getRequestHandler();

app.prepare().then(() => {
  const server = express();

  server.get('/page/:id', (req, res) => {
    res.redirect(`/page${req.params.id}`);
  });
  server.get('*', (req, res) => {
    return handle(req, res);
  });

  server.listen(port, err => {
    if (err) throw err;
  })
})
```

##### 서버사이드 렌더링 캐싱하기

1. lru-cache 패키지를 이용

##### 페이지 미리 렌더링 하기

페이지를 미리 렌더링 하면 서버의 cpu 리소스를 절약할 수 있다.

* 자동으로 미리 렌더링 하기
=> getInitialProps 함수가 없는 페이지는 자동으로 미리 렌더링 된다.
따라서 필요할 때만 써야한다.
(_app.js 에서 getInitialProps 함수를 사용하면 모든 페이지가 미리 렌더링 되지 않는다!)

* next export로 미리 렌더링하기
`next export` 명령어를 사용하면 미리 정적인 페이지를 만든다. 
express에서 `server.use(express.static('out'))` 를 통해 정적 파일을 서비스하도록 설정이 가능하다

