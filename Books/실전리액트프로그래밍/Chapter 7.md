# 7. 바벨과 웹팩 자세히 들여다보기

책 읽기 전 내가 가진 개념   
바벨 => js 코드를 버전에 맞게 수정해주는 도구   
웹팩 => js 코드를 배포하기 알맞게 만들어주는 도구   

### 7.1 바벨 실행 및 설정하기

##### 7.1.1 바벨을 실행하는 여러가지 방법
* @babel/cli로 실행하기
* 웹팩에서 babel-loader로 실행하기
* @babel/core를 직접 실행하기
* @babel/register로 실행하기

> 바벨이란  
> 입력과 출력이 모두 자바스크립트 코드인 컴파일러다. 이는 보통의 컴파일러가 고수준의 언어를 저수준의 언어로 변환하는 것과 비교된다.   
> 초기의 바벨은 es6 코드는 es5 코드로 변환해 주는 컴파일러였다. 현재는 바벨을 이용해서 리액트의 JSX 문법, 타입스크립트와 같은 정적 타입 언어, 코드 압축, 제안(proposal) 단계에 있는 문법 등을 사용할 수 있다.

* @babel/cli로 실행하기

```js
const element = <div>babel test</div>;
const text = `element type is ${element.type}`;
const add = (a,b) => a + b;
```

```shell
npx babel src/code.js --presets=@babel/preset-react --plugins=@babel/plugin-transform-template-literals,@babel/plugin-transform-arrow-functions

const element = /*#__PURE__*/React.createElement("div", null, "babel test");
const text = "element type is ".concat(element.type);

const add = function (a, b) {
  return a + b;
};
```

babel.config.js
```js
const presets = ['@babel/preset-react'];
const plugins = [
  '@babel/plugin-transform-template-literals',
  '@babel/plugin-transform-arrow-functions',
];

module.exports = { presets, plugins };
```

```shell
npx babel src/code.js --out-file dist.js 
npx babel src/code.js --out-dir dist
```

* 웹팩의 babel-loader로 실행하기

```shell
npm install webpack webpack-cli babel-loader
```

webpack.config.js
```js
const path = require('path');

module.exports = {
  entry: './src/code.js',
  output: {
    path: path.resolve(__dirname, 'dist'), 
    filename: 'code.bundle.js',
  },
  module: {
    rules: [{ test: /\.js$/, use: 'babel-loader' }],
  },
  optimization: { minimizer: [] },
}
```

```shell
npx webpack
```

* @babel/core를 직접 이용하기 

runBabel.js
```js
const babel = require('@babel/core');
const fs = require('fs');

const filename = './src/code.js';
const source = fs.readFileSync(filename, 'utf-8');
const presets = ['@babel/preset-react'];
const plugins = [
  '@babel/plugin-transform-template-literals',
  '@babel/plugin-transform-arrow-functions',
];
const { code } = babel.transformSync(source, {
  filename, 
  presets,
  plugins,
  configFile: false,
});
console.log(code);
```

```shell
node runBabel.js
```

바벨은 컴파일시 세 단계를 거친다
* 파싱 => 입력받은 코드로부터 AST(Abstract Syntax Tree)를 생성한다
* 변환 => AST를 원하는 형태로 변환한다.
* 생성 => AST를 코드로 출력한다.

자유도를 높여 컴파일 하는 법
```js
const babel = require("@babel/core");
const fs = require("fs");

const filename = "./src/code.js";
const source = fs.readFileSync(filename, "utf-8");
const presets = ["@babel/preset-react"];

const { ast } = babel.transformSync(source, {
  filename,
  ast: true,
  code: false,
  presets,
  configFile: false,
});

const { code: code1 } = babel.transformFromAstSync(ast, source, {
  filename,
  plugins: ['@babel/plugin-transform-template-literals'],
  configFile: false,
})

const { code: code2 } = babel.transformFromAstSync(ast, source, {
  filename,
  plugins: ["@babel/plugin-transform-arrow-functions"],
  configFile: false,
});

console.log(code1)
console.log(code2)
```

바벨 내부에서 extends 속성으로 다른 설정 파일을 가져올 수도 있다.

```
{
  "presets": ["@babel/preset-react"],
  "plugins": [
    [
      "@babel/plugin-transform-template-literals",
      {
        "loose": true
      }
    ]
  ]
}
```

```
{
  "extends": "../../common/.babelrc",
  "plugins": [
    "@babel/plugin-transform-arrow-functions",
    "@babel/plugin-transform-template-literals"
  ]
}
```

env 속성으로 환경별로 설정하기
```
{
  "presets": ["@babel/preset-react"],
  "plugins": [
    "@babel/plugin-transform-arrow-functions",
    "@babel/plugin-transform-template-literals"
  ],
  "env":{
    "production": {
      "presets": ["minify"]
    }
  }
}
```
=> 프로덕션 환경에서는 minify를 사용하게 한다.

overrides 속성으로 파일별로 설정하기
```
{
  "presets": ["@babel/preset-react"],
  "plugins": ["@babel/plugin-transform-template-literals"],
  "overrides": [
    {
      "include": "./service1",
      "exclude": "./service1.code2.js",
      "plugins": ["@babel/plugin-transform-arrow-functions"],
    }
  ]
}
```

### 7.1.3 전체 설정 파일과 지역 설정 파일
babel.config.js는 전체 설정 파일

폴더 내부에 있는 .babelrc, .babelrc.js 파일과 바벨 설정이 있는 package.json 파일이 지역설정 파일

### 7.1.4 바벨과 폴리필
자바스크립트의 최신 기능을 모두 사용하면서 오래된 브라우저를 지원하려면 바벨로 코드 문법을 변환하는 동시에 폴리필도 사용해야 한다.    
폴리필 => 런타임에 기능을 주입해 주는것!!!(런타임에 기능이 없는 경우에만 주입)   
**바벨을 사용하더라도 폴리필에 대한 설정은 별도로 해야한다.**   

폴리필 코드의 예
```js
if (!String.prototype.padStart) { // 있는지 없는지 검사해서 주입
  String.prototype.padStart = func
}
```

* core-js 모듈의 사용 예
core-js 모듈은 바벨에서 폴리필을 위해 공식적으로 지원하는 패키지다!!

웹팩에서 core-js 모듈을 사용한 예
```js
module.exports = {
  entry: ['core-js', './src/index.js'],
}
```

* core-js 모듈에서 필요한 폴리필만 가져오기
  
```js
import 'core-js/features/promise';
import 'core-js/features/object/values';
import 'core-js/features/array/includes';

const p = Promise.resolve(10);
const obj = {
  a: 10,
  b: 20,
  c: 30,
};
const arr = Object.values(obj);
const exist = arr.includes(20);
```
* @babel/preset-env 프리셋 이용하기
  
=> 런타임에 대한 정보를 설정해 주면 자동으로 필요한 기능을 주입해 준다.

babel.config.js
```js
const presets = [
  [
    '@babel/preset-env',
    {
      targets: '> 0.25%, not dead', // 시장점유율이 0.25% 이상이고 업데이트가 종료되지 않은 브라우저
    },
  ],
];

module.exports = { presets };
```

babel.config.js
```js
const presets = [
  [
    '@babel/preset-env',
    {
      targets: {
        chrome: '40', // 크롬 버전 최소 40
      },
      useBuiltIns: 'entry', // 'entry' => 지원하는 브라우저에서 필요한 폴리필만 추가 시킨다., 'usage' => 실제로 사용하는 폴리필만 추가
      corejs: { version: 3, proposal: true },
    },
  ],
];

module.exports = { presets }
```

```js
import 'core-js'';

const p = Promise.resolve(10);
const obj = {
  a: 10,
  b: 20,
  c: 30,
}
const arr = Object.values(obj);
const exist = arr.includes(20);
```

위의 babel.config.js의 설정으로 크롬 버전 40에 없는 기능들이 추가된다.

### 7.2 바벨 플러그인 제작하기

##### 7.2.1 AST 구조 들여다보기

```js
const v1 = a + b;
```

AST
```json
{
  "type": "Program",
  "start": 0,
  "end": 17,
  "body": [
    {
      "type": "VariableDeclaration",
      "start": 0,
      "end": 17,
      "declarations": [
        {
          "type": "VariableDeclarator",
          "start": 6,
          "end": 16,
          "id": {
            "type": "Identifier",
            "start": 6,
            "end": 8,
            "name": "v1"
          },
          "init": {
            "type": "BinaryExpression",
            "start": 11,
            "end": 16,
            "left": {
              "type": "Identifier",
              "start": 11,
              "end": 12,
              "name": "a"
            },
            "operator": "+",
            "right": {
              "type": "Identifier",
              "start": 15,
              "end": 16,
              "name": "b"
            }
          }
        }
      ],
      "kind": "const"
    }
  ],
  "sourceType": "module"
}
```


##### 7.2.2 바벨 플러그인의 기본 구조
```js
module.exports = function({ types: t }) {
  const node = t.BinaryExpression('+', t.Identifier('a'), t.Identifier('b'));
  console.log('isBinaryExpression:', t.isBinaryExpression(node));
  return {};
}
```

##### 7.2.3 바벨 플러그인 제작하기: 모든 콘솔 로그 제거

plugins/remove-log.js
```js
module.exports = function({ types: t }) {
  return {
    visitor: {
      ExpressionStatement(path) {
        if (t.isCallExpression(path.node.expression)) {
          if (t.isMemberExpression(path.node.expression.callee)) {
            const memberExp = path.node.expression.callee;
            if (
              memberExp.object.name === 'console' && memberExp.property.name === 'log'
            ) {
              path.remove();
            }
          }
        }
      }
    }
  }
}
```

### 7.3 웹팩 초급편 

웹팩은 모듈 번들러다   
모듈은 각 리소스 파일, 번들은 웹팩 실행후에 나오는 결과 파일이다.   
하나의 번들 파일은 여러 모듈로 구성됨   
웹팩을 이용하면 여러가지 리소스를 사용자에게 전달하기 좋은 형태로 만들 수 있다.   

* 필요한 이유
=> 웹팩을 사용하지 않으면 모든 파일을 body 끝에서 script tag로 가져온다. 이때 주소가 틀리거나 필요없어져서 삭제할때 문제가 생길수 있다.    

##### 7.3.1 웹팩 실행하기

```js
export function sayHello(name) {
  console.log('hello', name);
}
```

```js
import { sayHello } from "./util";

function myFunc() {
  sayHello('mike');
  console.log('myFunc');
}
myFunc();
```

```js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },
  mode: 'production',
  optimization: { minimizer: [] },
}
```

결과물 
```js
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
var __webpack_exports__ = {};

;// CONCATENATED MODULE: ./src/util.js
function sayHello(name) {
  console.log('hello', name);
}
;// CONCATENATED MODULE: ./src/index.js


function myFunc() {
  sayHello('mike');
  console.log('myFunc');
}
myFunc();
/******/ })()
;
```


##### 7.3.2 로더 사용하기
로더는 모듈을 입력으로 받아서 원하는 형태로 변환한 후 새로운 모듈을 출력해 주는 함수다.   
자바스크립트 뿐만 아니라 모든 파일은 모듈이 될수 있다.



```js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      }
    ]
  },
  mode: 'production',
};
```

```shell
npm install babel-loader css-loader style-loader
```

js파일 확장자를 가지고 있는 친구들은 babel-loader를 이용하도록 해버림
 
js에는 babel-loader   
css에는 css-loader, style-loader를 이용해주어야지 번들화 되고 실제로 적용도 된다.

* 기타 파일 처리하기

```shell
npm install file-loader raw-loader
```


```js
module: {
  rules: [
    {
      test: /\.js$/,
      exclude: /node_modules/,
      use: "babel-loader",
    },
    {
      test: /\.css$/,
      use: ["style-loader", "css-loader"],
    },
    {
      test: /\.(png|jpg|gif)$/,
      use: 'file-loader',
    },
    {
      test: /\.txt$/,
      use: 'raw-loader',
    }
  ],
},
```

* 이미지 파일의 요청 횟수 줄이기

이미지 파일을 번들 파일에 포함시키면 브라우저의 파일 요청 횟수를 줄일 수 있다.   
번들 파일 크기가 너무 커지면 자바스크립트가 늦게 실행되므로 작은 이미지 파일만 포함시키는 게 좋다.

```shell
npm install url-loader
```

```js
rules: [
  {
    test: /\.(png|jpg|gif)$/,
    use: [
      {
        loader: 'url-loader',
        options: {
          limit: 8192,
        }
      }
    ]
  }
]
```

##### 플러그인 사용하기
플러그인은 로더보다 강력한 기능을 갖는다.    
로더는 특정 모듈에 대한 처리만 담당하지만 플러그인은 웹팩이 실행되는 전체 과정에 개입할 수 있다.   

```shell
npm install clean-webpack-plugin html-webpack-plugin
```

```js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: '[name].[chunkhash].js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-react'],
          }
        }
      }
    ]
  },
  mode: 'production',
}
```

html-webpack-plugin은 chunkhash 옵션을 설정했기 때문에 파일의 내용이 수정될때마다 html파일의 내용도 수정해주어야 하는데 이를 자동으로 해준다.
clean-webpack-plugin은 웹팩을 실행할 때마다 dist 폴더를 정리한다.

```js
 plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: './template/index.html',
    })
  ],
```

* DefinePlugin
=> 문자열 대체하는 플러그인

```js
new webpack.DefinePlugin({
  APP_VERSION: '"1.2.3."',
  TEN: '10',
})
```

* ProvidePlugin
=> 미리 설정한 모듈을 자동으로 등록해 준다.

자주 사용하는 모듈을 import 키워드를 사용해서 가져오는 게 귀찮을 수 있다.

```js
new webpack.ProvidePlugin({
  React: 'react',
  $: 'jquery',
})
```

### 7.4 웹팩 고급편

##### 7.4.1 나무 흔들기(Tree Shaking)
tree shaking은 불필요한 코드를 제거해 주는 기능이다.    
웹팩은 기본적으로 트리쉐이킹을 제공한다.     
그러나 제대로 동작하지 않는 경우가 있다.    
따라서 트리쉐이킹을 잘 이해하고 있어야 번들 파일 크기를 최소로 유지할 수 있다.    

util_esm.js
```js
export function func1() {
  console.log('func1');
}

export function func2() {
  console.log('func2');
}
```

util_common.js
```js
function func1() {
  console.log('func1')
}
function func2() {
  console.log("func2");
}
module.exports = { func1, func2 };
```

index.js
```js
// 트리 쉐이킹 성공
import { func1 } from './util_esm';

// 트리 쉐이킹 실패
import { func1 } from './util_commonjs';
func1()

// 트리 쉐이킹 실패 (내부는 esm으로 되어있지만 동적임포트를 이용하였기 때문에 실패)
import('./util_esm').then(util => util.func1())
```



* commonjs 로 작성된 파일의 경우 트리쉐이킹이 실패한다.



다음과 같은 경우에 트리쉐이킹은 실패한다.

* 사용되는 모듈이 ESM(ECMAScript Modules)이 아닌경우
* 사용하는 쪽에서 ESM이 아닌 다른 모듈 시스템을 사용하는 경우
* 동적 임포트를 사용하는 경우
* 모듈 내부에서 함수를 호출하는 경우 해당 함수는 사용되는 파일이 없지만 삭제되지 않는다.


-----

* 외부 패키지의 트리쉐이킹

lodash 패키지는 esm으로 되어 있지 않기 때문에 트리쉐이킹이 동작 하지 않는다.  
아래와 같이 사용하여야 한다.
```js
import fill from 'lodash/fill';

import {fill} from 'lodash-es';
```

lodash-es는 esm 모듈시스템을 사용한다.   

* 바벨 사용 시 주의할 점
=> 우리가 작성한 코드를 바벨로 컴파일한 이후에도 ESM 문법으로 남아 있어야 한다.  
@babel/preset-env 플러그인을 사용한다면 아래와 같이 사용해야 한다.   
babel.config.js
```js
const preset = [
  [
    '@babel/preset-env',
    {
      modules: false, // 모듈시스템을 변경하지 않도록 한다.
    }
  ]
]
```


##### 7.4.2 코드 분할
많은 수의 사용자를 대상으로 하는 서비스라면 응답 시간을 최소화하기 위해 코드를 분할하는 게 좋다.

```js
const path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
  entry: {
    page1: './src/index1.js',
    page2: './src/index2.js',
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'dist'),
  },
  plugins: [new CleanWebpackPlugin()],
  mode: 'production',
}
```

* SplitChunksPlugin
웹팩에서는 코드 분할을 위해 기본적으로 SplitChunksPlugin을 내장하고 있다.   
```js
optimization: {
  splitChunks: {
    chunks: 'all',
    name: 'vendor',
  }
},
```

chunks 속성의 기본값은 동적 임포트만 분할하는 async다. 우리는 동정 임포트가 아니더라도 코드가 분할되도록 all로 설정한다.   
이 상태로 웹팩을 빌드하면 lodash와 REACT 모듈은 vendor.js 파일로 만들어진다.

splitChunks 속성의 기본값
```js
module.exports = {
  //...
  optimization: {
    splitChunks: {
      chunks: 'async', // 동적임포트만 분할 하도록
      minSize: 30000, // 파일 크기가 30kb이상인 모듈만
      minChunks: 1, // 한 개 이상의 chunk에 포함되어 있어야 한다 (chunk는 번들파일이라고 이해하면 됨)
      //...
      cacheGroups: { // 파일 분할은 그룹별로, 기본적으로 외부(vendor), 내부(default)로 나뉨, 외부모듈은 비교적 덜 바뀌므로 브라우저에 오래 캐싱될 수 있다
        default: {
          minChunks: 2, // 내부 모듈은 두 개 이상의 번들 파일에 포함되어야 분할된다.
          priority: -20,
          reuseExistingChunk: true,
        }
      },
      defaultVendors: {
        test: /[\\/]node_modules[\\/]/,
        priority: -10
      }
    }
  }
}
```

utils.js 모듈도 분할되도록 설정하기
```js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all', // 모든 코드 분할하도록 설정
      minSize: 10, // 파일크기 낮춤
      cacheGroups: {
        vendors: {
          test: /[\\/]node_modules[\\/]/,
          priority: 2,
          name: 'vendors',
        },
        defaultVendors: {
          minChunks: 1, // 최소 한개에 쓰이는 모듈 분할되도록 설정
          priority: 1,
          name: 'default',
        }
      }
    }
  }
}
```

react 패키지는 별도로 분할하도록 설정
```js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        defaultVendors: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 1,
        },
        reactBundle: {
          test: /[\\/]node_moudles[\\/](react|react-dom)[\\/]/,
          name: 'react.bundle',
          priority: 2, // 우선순위가 높아야 리액트 모듈이 vendors 그룹에 들어가지 않음
          minSize: 100,
        }
      }
    }
  }
}
```

##### 7.4.3 로더 제작하기
로더는 모듈을 입력으로 받아서 원하는 형태로 변경 후 자바스크립트 코드를 반환한다.
로더가 자바스크립트 코드를 반환하기 때문에 웹팩은 css, png, csv 확장자를 갖는 모듈도 처리할 수 있다.

중간과정에서 처리되는 css-loader 처럼 다른 형태의 데이터로 반환할 수도 있다. 하지만 style-loader 처럼 가장 마지막에 처리되는 로더는 항상 자바스크립트 코드를 반환한다.   

webpack.config.js
```js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.csv$/,
        use: './my-csv-loader',
      }
    ]
  },
  mode: 'production',
}
```

my-csv-loader
```js
module.exports = function(source) {
  const result = { header: undefined, rows: [] };
  const rows = source.split('\n');
  for (const row of rows) {
    const cols = row.split(',');
    if (!result.header) {
      result.header = cols;
    } else {
      result.rows.push(cols);
    }
  }
  return `export deafult ${JSON.stringify(result)}`;
};
```



##### 7.4.4 플러그인 제작하기
DefinePlugin처럼 플러그인은 모듈의 내용도 수정할 수 있기 때문에 로더가 할 수 있는 거의 모든 일을 할 수 있다.
웹팩이 생성하는 번들 파일의 목록과 각 파일의 크기 정보를 파일로 저장해 주는 플러그인을 제작해보자


my-plugin.js
```js
class MyPlugin {
  constructor(options) {
    this.options = options;
  }
  apply(compiler) { // 웹팩의 각 처리 단계에서 호출될 콜백 함수를 등록할 수 있다.
    compiler.hooks.done.tap('MyPlugin', () => { // 웹팩의 실행이 완료되었을때 호출되는 콜백 함수
      console.log('bundling completed');
    });
    compiler.hooks.emit.tap('MyPlugin', compilation => {
      let result = '';
      for (const filename in compilation.assets) { // 웹팩이 생성할 파일의 목록이 들어있다.
        if (this.options.showSize) {
          const size = compilation.assets[filename].size();
          result += `${filename}(${size})\n`;
        } else {
          result += `${filename}\m`;
        }
      }
      compilation.assets['fileList.txt'] = {
        source: function() {
          return result;
        },
        size: function() {
          return result.length;
        }
      }
    })
  }
}

module.exports = MyPlugin;
```

webpack.config.js
```js
const path = require('path');
const MyPlugin = require('./my-plugins');

module.exports = {
  entry: {
    app1: './src/index1.js',
    app2: './src/index2.js',
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'dist'),
  },
  plugins: [new MyPlugin({ showSize: true })],
  mode: 'production'
}
```