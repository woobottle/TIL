# 1. 리액트란 무엇인가

### 1.1 리액트란 무엇인가
* UI 라이브러리다.
* UI 기능만 제공한다.
* 전역 상태관리, 라우팅, 빌드 시스템은 직접 구축해야 한다.
* 가상돔을 통해서 UI를 빠르게 업데이트
  * 이전 UI 상태를 메모리에 저장하고 변화되는 부분만 탐지해서 업데이트 침(전체를 업데이트 치지 않아도 되서 효율성이 좋음)

> 리액트 네이티브는 모바일에서 자바스크립트를 실행하기 위해 JavascriptCore를 사용한다
> JavascriptCore는 웹킷에 저장된 C++로 작성된 자바스크립트 엔진 
> (모바일 운영체에서는 앱에서 C++코드를 실행할 방법을 제공함)


### 1.2.2 바벨 사용해보기
* 바벨은 자바스크립트 코드를 변환해주는 컴파일러다
* 바벨은 최신 자바스크립트 문법을 지정한 버전에 맞게 변환해준다.(동작 까보고 싶네)
* 리액트에서는 JSX 문법을 사용하기 위해 바벨을 사용한다. 바벨이 JSX 문법으로 작성된 코드를 createElement 함수를 호출하는 코드로 변환해준다.

### 1.2.3 웹팩의 기본 개념 이해하기
* 웹팩은 자바스크립트로 만든 프로그램을 배포하기 좋은 형태로 묶어주는 도구이다.(이름 그대로 이해하면 좋을 듯)
* 웹팩이 생성하는게 dist폴더 밑에 파일들

> 자바스크립트에는 ES6!! 부터 모듈 시스템이 언어 차원에서 지원된다. CommonJS는 자바스크립트의 대표적 모듈 시스템.
> node.js가 commonJs 표준을 따르면서 commonJs가 널리 퍼짐

* 폴리필
>  보충솜이라는 뜻, 실행시점에 기능이 존재하는지 검사해서 없으면 그 기능을 주입하는 것(이불에 솜이 없는 부분만 채워넣자!!)

* autoprefixer
> css에 접두사 붙여주는 친구, position: sticky, position: webkit-sticky, position: ms-sticky 처럼 각 브라우저 전용으로 필요한 친구들이 있음

### 1.4.4 css-in-js로 작성하기
* 보통 styled-components를 많이 이용하는데 특장점은 동적으로 style 먹일 수 있다는거.

```jsx
import React from 'react';
import styled from 'styled-components';

const BoxCommon = styled.div`
  width: ${props => (props.isBig ? 200 : 100)}px;
  height: 50px;
  background-color: #aaa;
`;

function Box({ size }) {
  const isBig = size === 'big';
  const label = isBig ? '큰 박스' : '작은 박스';
  return <BoxCommon isBig={isBig}>{label}</BoxCommon>;
}

export default Box
```

`window.history.pushState('v1', '','/page1');` 제일 마지막 파라미터로 url이 바뀌어 버림

### 1.5.2 react-router-dom 사용하기
* 브라우저 히스토리 api(window.history의 methods) 를 이용해서 관리하면 복잡하다.
* 이때 사용하는 것이 react-router-dom