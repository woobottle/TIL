# 3. 리액트 컴포넌트

### 3-1 컴포넌트를 표현하는 jsx
JSX => Javascript XML의 줄임말 'Javascript에 XML을 추가한 확장형 문법'

```jsx
  render() {
    return (
      <div>
        <img src=".../~~~" />
        <div>안녕하세요</div>
      </div>
    );
  }
```

위의 jsx는 react에 의해 아래와 같이 변환된다.

```js
React.createElement(
  "div",
  null,
  React.createElement("img", {
    src: ".../~~~",
  }),
  React.createElement(
    "div",
    null,
    "안녕하세요",
  )
)
```


### 3-2 컴포넌트와 구성 요소
컴포넌트의 등장 배경 => 웹 사이트의 화면은 각 요소가 비슷하고 반복적으로 사용되는 경우가 많음, 블록처럼 조립

> 경로문에서 확장자를 제거할 수 있는 이유는 웹팩의 '코드 검색 확장자' 기능 덕분   
> 웹팩은 임포트된 파일을 분석하여 하나의 자바스크립트 파일을 생성할 때 파일 위치를 검색   
> 1. 확장자가 있는 파일을 먼저 임포트
> 2. 확장자가 없으면 확장자 옵션(extensions)에 정의된 확장자 목록을 보고 해당 확장자 이름을 포함한 파일이 있는지 확인하여 임포트
> `import 'Myfile'`의 경우 `MyFile.js > MyFile.jsx` 순서로 파일을 확인하여 임포트
> 3. 경로에 파일이 없으면 같은 이름의 폴더는 없는지 검색

### 3-3 컴포넌트에 데이터를 전달하는 프로퍼티
부모 컴포넌트에서 자식 컴포넌트로 `props`를 통해서 데이터를 전달할때 이것을 '단방향으로 데이터가 흐른다' 라고 합니다.

* 문자열형 프로퍼티 사용하기
```jsx
import React, { Component } from 'react';
import PropTypes from 'prop-types';

class PropsComponent extends Component {
  render() {
    return <div className="message-container">{this.props.name}</div>;
  }
}

PropsComponent.propTypes = {
  name: PropTypes.string,
};

export default PropsComponent;
```

* 다양한 프로퍼티 사용하기

```jsx
import React, { Component } from 'react';
import PropTypes from 'prop-types';

class PropsComponent extends Component {
  render() {
    const { name, boolValue, numValue, nodeValue, funcValue } = this.props;

    return <div className="message-container">{this.props.name}</div>;
  }
}

PropsComponent.propTypes = {
  name: PropTypes.string,
  boolValue: PropTypes.bool,
  numValue: PropTypes.number,
  nodeValue: PropTypes.node,
  funcValue: PropTypes.func,
};

export default PropsComponent;
```

* 자식 프로퍼티 사용하기

```jsx
<ChildProperty children={<div><span>자식노드</span></div>}>

class ChildProperty extends Component {
  render() {
    return <div>{this.props.children}</div>
  }
}

ChildProperty.propTypes = {
  children: PropTypes.node,
};
```

### 3-4 컴포넌트 상태 관리 하기

```jsx
import React, { Component } from 'react';

class StateExample extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      formData: 'no data',
    };

    this.handleData = this.handleData.bind(this);
    setTimeout(this.handleData, 400);
  }

  handleData() {
    const data = 'new data';
    const { formData } = this.state;
    this.setState({
      loading: false,
      formData: data + formData,
    });
  }
  render() {
    return <div></div>;
  }
}

export default StateExample;
```

* state값은 setState() 함수로 변경해주자
직접 바꿔주면 안되는 이유 -> render() 함수로 화면을 그려주는 시점은 리액테 엔진이 정하기 때문!, state값을 직접 변경하면 render가 호출되지 않는다.

* setState의 함수로 인자를 전달하면 이전 state 값을 따로 읽는 과정을 생략할 수 있다.
```jsx
handleData(data) {
  this.setState(function(prevState) {
    const newState = {
      loading: false,
      formData: data + prevState.formData,
    };
    return new State;
  })
}

handleDate(data) {
  this.setState(prevState => {
    loading: false,
    formData: data + prevState.formData
  })
}
```

### 3-5 컴포넌트의 생명 주기

### 3-6 클래스형 컴포넌트

* Component 알아보기
```jsx
import React from 'react';
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    console.log('생성 함수')
  }
  componentDidMount() { // 상속받은 생명주기 함수 }
  myMethod() { // 추가 확장 함수 }
  render() { // 상속받은 화면 출력 함수 }
}
```
* PureComponent 알아보기

얕은 비교를 통해 데이터가 변경된 경우 render 함수를 호출한다.

```jsx
import React, { Component } from 'react';
import shallowEqual from 'shallow-equal';

export default class PureComponent extends Component {
  shouldComponentUpdate(nextProps, nextState) {
    return !shallowEqual(this.props, nextProps) || !shallowEqual(this.state, nextState);
  }
}
```


### 3-7 함수형 컴포넌트

<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3b94b004-bce9-4b06-9699-a92c120a14bd%2FUntitled.png?table=block&id=df6b184b-e5c5-421a-a0ac-c07463dec25c&spaceId=359809db-cb83-47c2-9cce-0c45f96418ab&width=2000&userId=56059f96-1ce0-4d35-87f6-3200db26ea2a&cache=v2">

```jsx
import React from 'react';
import PropTypes from 'prop-types';

const SFC = (props, context) => {
  const { somePropValue } = props;
  const { someContextValue } = context;
  return <div>Hello, {somePropValue}</div>;
};

SFC.propTypes = { somePropValue: PropTypes.any };
SFC.defaultProps = { someContextValue: 'default value' };

export default SFC;
```

**함수형 컴포넌트는 state와 생명주기 함수를 사용할 수 없다.**


### 3-8 배열 컴포넌트

### 3-9 컴포넌트에서 콜백 함수와 이벤트 처리하기
JSX DOM 이벤트 프로퍼티 => [onClick, onSubmit, onMouseMove, onMouseOver, onMouseOut, onKeyDown, onKeyPress]

<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc311c3ed-c6ca-462f-8497-05599db236d9%2FUntitled.png?table=block&id=9282254e-9bd3-46b2-b54b-6af1f93c10fa&spaceId=359809db-cb83-47c2-9cce-0c45f96418ab&width=2000&userId=56059f96-1ce0-4d35-87f6-3200db26ea2a&cache=v2">


단방향 흐름-방식 => 원본데이터의 무결성을 지켜주므로 데이터 수정으로 인한 파편화를 줄여줍니다.

### 3-10 Input 컴포넌트 만들면서 복습하기