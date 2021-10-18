# 5. 패키지 매니저

### 5.1 npm 알아보기
npm => Node Package Manager   
npm에 업로드된 노드 모듈을 패키지라고 부른다.  
패키지는 다른 패키지를 사용할 수 있다.

### 5.2 package.json으로 패키지 관리하기
package.json => 패키지 버전 관리하는 파일 

> audited [숫자] packages   
> 패키지에 있을 수 잇는 취약점을 자동으로 검사했다는 의미   
> npm audit fix를 입력하면 npm이 스스로 수정할 수 있는 취약점을 알아서 수정합니다.   

```shell
npm install morgan cookie-parser express-session

npm install --save-dev nodemon
```

> 명령어 줄여쓰기   
> npm install -> npm i  
> npm --save-dev -> npm -D   
> npm --global -> npm -g   

### 5.3 패키지 버전 이해하기
노드 패키지들의 버전은 항상 세 자리로 이루어져 있다. => SemVer 방식의 버전 넘버링을 따르고 있기 때문
SemVer => Semantic Versioning(유의적 버전)의 약어, 버전을 구성하는 세 자리가 모두 의미가 있다.

첫번째 자리 -> major 버전
두번째 자리 -> minor 버전
세번째 자리 -> patch 버전(기존 기능에 문제가 있어 수정)

기호 별 의미
* npm i express@^1.1.1 => minor 버전까지만 설치하거나 업데이트, 1.1.1 이상부터 2.0.0 미만 버전까지 설치
* npm i express@~1.1.1 => patch 버전까지만 설치하거나 업데이트, 1.1.1 이상부터 1.2.0 미만 버전까지 설치
* <, >, >=, <=, =   => 보이는 의미 그대로
* npm i express@latest => 안정된 최신 버전의 패키지를 설치

### 5.4 기타 npm 명령어
`npm outdated` 명령어로 업데이트 할 수 패키지가 있는지 확인 가능

current !== wanted 면 업데이트가 필요한 상황   
`npm update [패키지명]` 으로 해당 패키지 업데이트 가능   

삭제 => `npm uninstall [패키지명]`, `npm rm [패키지명]`


### 5.5 패키지 배포하기
npm publish ~~~