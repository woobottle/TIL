# 14. CLI 프로그램 만들기

```js
#!/usr/bin/env node // usr/bin/env에 등록된 node 명령어로 이 파일을 실행하라!!!!
console.log('Hello CLI');
```

```json
"license": "ISC",
"bin": {
  "cli": "./index.js"
}
```

`npm i -g` 로 해당 패키지 전역 설치 하면 콘솔에서 cli 명령어 치면 index.js 실행됨!!!!!! 신기


```js
#!/usr/bin/env node

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('예제가 재미있습니까? (y/n) ', (answer) => {
  if (answer === 'y') {
    console.log('감사합니다')
  } else if (answer === 'n') {
    console.log('죄송합니다')
  } else {
    console.log('y 또는 n만 입력하세요');
  }
  rl.close();
})
```


```js
// template.js
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const readline = require('readline');

let rl;
let type = process.argv[2];
let name = process.argv[3];
let direcotry = process.argv[4] || '.';

const htmlTemplate = `
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Template</title>
  </head>
  <body>
    <h1>Hello</h1>
    <p>CLI</p>
  </body>
</html>
`;

const routerTemplate = `
const express = require('express');
const router = express.Router();
 
router.get('/', (req, res, next) => {
   try {
     res.send('ok');
   } catch (error) {
     console.error(error);
     next(error);
   }
});
 
module.exports = router;
`;

const exist = (dir) => {
  try {
    fs.accessSync(dir, fs.constants.F_OK | fs.constants.R_OK | fs.constants.W_OK);
    return true;
  } catch (e) {
    return false;
  }
}

const mkdirp = (dir) => {
  const dirname = path
    .relative('.', path.normalize(dir))
    .split(path.sep)
    .filter(p => !!p);
  dirname.forEach((d, idx) => {
    const pathBuilder = dirname.slice(0, idx + 1).join(path.sep);
    if (!exist(pathBuilder)) {
      fs.mkdirSync(pathBuilder);
    }
  });
}

const makeTemplate = () => { // 템플릿 생성 함수
  mkdirp(directory);
  if (type === 'html') {
    const pathToFile = path.join(directory, `${name}.html`);
    if (exist(pathToFile)) {
      console.error('이미 해당 파일이 존재합니다');
    } else {
      fs.writeFileSync(pathToFile, htmlTemplate);
      console.log(pathToFile, '생성 완료');
    }
  } else if (type === 'express-router') {
    const pathToFile = path.join(directory, `${name}.js`);
    if (exist(pathToFile)) {
      console.error('이미 해당 파일이 존재합니다');
    } else {
      fs.writeFileSync(pathToFile, routerTemplate);
      console.log(pathToFile, '생성 완료');
    }
  } else {
    console.error('html 또는 express-router 둘 중 하나를 입력하세요.');
  }
};

const dirAnswer = (answer) => { // 경로 설정
  directory = (answer && answer.trim()) || '.';
  rl.close();
  makeTemplate();
};

const nameAnswer = (answer) => { // 파일명 설정
  if (!answer || !answer.trim()) {
    console.clear();
    console.log('name을 반드시 입력하셔야 합니다.');
    return rl.question('파일명을 설정하세요. ', nameAnswer);
  }
  name = answer;
  return rl.question('저장할 경로를 설정하세요.(설정하지 않으면 현재경로) ', dirAnswer);
};

const typeAnswer = (answer) => { // 템플릿 종류 설정
  if (answer !== 'html' && answer !== 'express-router') {
    console.clear();
    console.log('html 또는 express-router만 지원합니다.');
    return rl.question('어떤 템플릿이 필요하십니까? ', typeAnswer);
  }
  type = answer;
  return rl.question('파일명을 설정하세요. ', nameAnswer);
};

const program = () => {
  if (!type || !name) {
    rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
    console.clear();
    rl.question('어떤 템플릿이 필요하십니까? ', typeAnswer);
  } else {
    makeTemplate();
  }
};

program(); // 프로그램 실행부
```

package.json이 바뀌면 새로 전역설치를 진행해 주어야 한다.


### 14.2 commander, inquirer 사용하기


```js

const { program } = require("commander");

program.version("0.0.1", "-v, --version").name("cli");

program
  .command("template <type>")
  .usage("<type> --filename [filename] --path [path]")
  .description("템플릿을 생성합니다")
  .alias("tmpl")
  .option("-f, --filename [filename]", "파일명을 입력하세요.", "index")
  .option("-d, --directory [path]", "생성 경로를 입력하세요", ".")
  .action((type, options) => {
    console.log(type, options.filename, options.directory);
  });

program.command("*", { noHelp: true }).action(() => {
  console.log("해당 명령어를 찾을 수 없습니다");
  program.help();
});

program.parse(process.argv); 
```


```js
const inquire = require('inquirer');

program
  .action((cmd, args) => {
    if (args) {
      console.log(chalk.bold.red("해당 명령어를 찾을 수 없습니다."));
      program.help();
    } else {
      inquirer
        .prompt([
          {
            type: "list",
            name: "type",
            message: "템플릿 종류를 선택하세요.",
            choices: ["html", "express-router"],
          },
          {
            type: "input",
            name: "name",
            message: "파일의 이름을 입력하세요.",
            default: "index",
          },
          {
            type: "input",
            name: "directory",
            message: "파일이 위치할 폴더의 경로를 입력하세요.",
            default: ".",
          },
          {
            type: "confirm",
            name: "confirm",
            message: "생성하시겠습니까?",
          },
        ])
        .then((answers) => {
          if (answers.confirm) {
            makeTemplate(answers.type, answers.name, answers.directory);
            console.log(chalk.rgb(128, 128, 128)("터미널을 종료합니다."));
          }
        });
    }
  })
  .parse(process.argv);
```



* 노드는 단순히 서버가 아니라 자바스크립트를 실행하는 런타임입니다!
* 프로그래머의 소양 중 하나는 DRY(Dont Repeat YourSelf)입니다. cli프로그램을 이용해 반복되는 작업을 최소화하는 프로그램을 제작해 봅시다.