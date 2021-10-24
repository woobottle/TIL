# 1. 리액트의 정체를 알아보자.

###### 리액트의 개념과 장점
* 화면 출력에 특화된 프레임워크
* 컴포넌트로 화면 구성을 효율적으로 할 수 있다.
  => 가상돔 활용 필요한 부분만 쓱쓱 업데이트 쳐줌
* 게임 엔진 원리를 도입하여 화면 출력 속도가 빠르다
  <img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F41f7be4c-dd36-4c4b-8d43-03f4f44f4e1e%2FUntitled.png?table=block&id=99b102c3-059e-4973-a89e-9f5cb39f0988&spaceId=359809db-cb83-47c2-9cce-0c45f96418ab&width=2000&userId=56059f96-1ce0-4d35-87f6-3200db26ea2a&cache=v2">
  
  **대부분의 게임 엔진은 다음 장면에 필요한 화면을 미리 그려 두는 방법으로 화면을 빠르게 전환합니다.**
  
  이 방법을 리액트에 도입하여 '다음에 나타날 화면의 일부(노드)를 미리 그려 놓고 변경된 화면의 일부(노드)만 수정하는' virtual DOM 기술을 만들었다.
  <https://github.com/FEDevelopers/tech.description/wiki/%EA%B0%80%EC%83%81-%EB%8F%94%EA%B3%BC-%EB%8F%94%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90>

##### 노드 패키지 매니저란 무엇일까?

npm => https://www.npmjs.com에서 필요한 라이브러리를 내려받아 설치하고 삭제등의 관리를 해주는 프로그램
package.json에 있는 명세만 서로 공유하는 방식

##### 웹팩이란 무엇일까?
웹팩 => 프로젝트에 사용된 파일을 분석하여 기존 웹 문서 파일로 변환하는 도구
웹팩이 필요한 이유 => 프레임워크가 .js, .css, .jpg와 같은 기존 웹 문서 파일을 사용하지 않기 때문, 브라우저에서는 .sass파일을 해석하지 못하므로 중간에 누군가 이 파일을 해석해 주어야 한다. 이 역할을 하는 도구가 웹팩(샤론 최 통역가 같은 느낌)

<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F08ff3a45-ed2e-4322-bab1-48350849018b%2FUntitled.png?table=block&id=fa4221db-257e-4bc9-b09e-846b98b15568&spaceId=359809db-cb83-47c2-9cce-0c45f96418ab&width=2000&userId=56059f96-1ce0-4d35-87f6-3200db26ea2a&cache=v2">

+ 웹팩은 js,png,jpg 등과 같은 파일을 적절한 크기로 자르거나 묶어주는 역할도 함. 불필요한 파일을 제외하거나 압축하여 프로젝트의 용량을 줄여준다.


### 리액트 개발 환경 설치하기
reactjs code snippets 플러그인 설치하기
prettier 세팅
|키워드|설명|
|--|--|
|rsc|함수형 컴포넌트 생성|
|rscp|함수형 컴포넌트를 프로퍼티 타입과 함께 생성|