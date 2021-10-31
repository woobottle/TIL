# 4. 에어비앤비 디자인 시스템 따라 하기

### 4-1 비주얼 테스트로 더 쉽게 개발하기
스토리북 => 비주얼 테스트를 위한 도구    
비주얼 테스트 => 화면을 구성하는 컴포넌트들을 독립적으로 관리하고 변화를 살펴볼 수 있는 방법(실제 가구를 집에 배치하기 전에 제품 사진만 따로 모아둔 책자에서 다양한 색상의 가구를 확인하는 것과 비슷)     

/pagkage.json
```json
"storybook": "start-storybook -p 9001 -c .storybook",
```

/src/stories/InputStory.jsx
```jsx
import React from 'react';
import { storiesOf } from '@storybook/react';
import Input from '../03/Input';


storiesOf('Input', module)
  .add('기본 설정', () => <Input name="name" />)
  .add('label 예제', () => <Input name="name" label="이름" />);
```


/.storybook/config.js
```js
import { configure } from '@storybook/react';

function loadStories() {
  require('../src/stories/InputStory');
}

configure(loadStories, module);
```

story 폴더 아래에 Story.jsx로 되어있는 파일들 다 가져오는 내용
```js
import { configure } from '@storybook/react';
import interopRequireDefault from 'babel-runtime/helpers/interopRequireDefault';
function loadStories() {
  const context = require.context('../src/stories', true, /Story\.jsx$/);
  context.keys().forEach((srcFile) => {
    interopRequireDefault(context(srcFile));
  });
}

configure(loadStories, module);
```

onchange 액션 발생시 아래에 로그 찍는 코드 
```jsx
import { action } from '@storybook/addon-actions';

storiesOf('Input', module)
  .add('기본 설정', () => <Input name="name" />)
  .add('label 예제', () => <Input name="name" label="이름" />)
  .add('onChange 예제', () => <Input name="name" onChange={action('onChange 이벤트 발생')} />);
```

/.storybook/addons.js
```js
import '@storybook/addon-actions/register';
import 'storybook-addon-jsx/register'; // jsx 같이 보여주는 코드
```
### 4-2 CSS로 컴포넌트 스타일 적용하기
node-sass 라이브러리는 scss 파일을 컴파일하여 css파일로 생성해 줌   

스토리북 서버는 리액트 서버와 웹팩 설정이 다르므로 sass를 추가하려면 sass-loader를 프로젝트에 추가해주어야 한다.

### 4-3 스타일 컴포넌트 만들기
개별 컴포넌트에만 스타일을 먹이기 위해서 등장한게 `react-with-styles` 라이브러리, css를 공통으로 쓰면 작업량이 늘어날 수록 덮어 씌워지는게 많아진다.

`yarn add react-with-styles aphrodite react-with-styles-interface-aphrodite`

aphrodite => 서버 출력을 도와주는 라이브러리(화면 출력을 시작하는 순간에 스타일 코드를 서버에서 생성하여 같이 출력하는 방법)

```jsx
import React, { PureComponent } from 'react';
import PropTypes from 'prop-types';
import withStyles, { css } from './withStyles';

class Text extends PureComponent {
  render() {
    const { children, styles } = this.props;
    return <span {...css(styles.default)}>{children}</span>;
  }
}

Text.propTypes = {
  childern: PropTypes.node.isRequired,
};

export default withStyles(({ color, size }) => ({
  default: {
    color: color.default,
    fontSize: size.md,
  },
}))(Text);
```

### 4-4 테스트 위주 개발 방법 사용해 보기
jest 이용

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import Input from '../../03/Input';

describe('<Input>', () => {
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<Input />, div);
    ReactDOM.unmountComponentAtNode(div);
    expect(React.isValidElement(<Input />)).toBeTruthy();
  });
});
```

enzyme 라이브러리 => 컴포넌트의 기능만을 손쉽게 검사해주는 도구


### 4-5 CheckBox 컴포넌트 만들면서 복습하기