# 6. 컨텍스트로 데이터 관리하기

### 6-1 컨텍스트의 기초 개념 알아보기
리액트에서는 부모와 자식간에 프로퍼티와 state로 데이터를 공유하였습니다.
컨텍스트는 부모와 자식 컴포넌트가 연결되어 있지 않아도 데이터를 공유할 수 있게 해줍니다.
컨텍스트 => '데이터 공유 저장소' + '데이터 전파'를 담당한다고 이야기 합니다.

기존의 좋지 못한 예
쓰지 않는 props를 계속 중간에서 넘겨주어야 한다.

parent component(data) -> parent1 component(data) -> parent2 component(data) -> child(data) use data


* Observer Pattern
=> 데이터는 공급자가 관리하고 소비자는 공급자를 구독하여 데이터를 얻는 방식

1. 소비자는 공급자가 제공하는 콜백 함수로 데이터를 변경할 수 있습니다.
- 단 소비자가 공급자의 데이터를 변경할때는 직접 변수에 접근하여 값을 변경하는 것이 아니라 콜백함수를 받아 데이터 변경 요청을 해야한다.

=> 이와 같은 단방향 데이터 흐름은 변경된 데이터의 일관성을 유지하는데 매우 효과적입니다.
단방향 데이터 흐름의 핵심은 한쪽에서만 변수에 직접 접근할 수 있다는 건가?

### 6-2 컨텍스트 제대로 사용하기
소비자가 여러개의 공급자 데이터를 구독하는 다양한 방법

### 6-3 컨테스트 API 활용하기
```jsx
const MyContext = React.createContext(defaultValue);
```


```jsx
import React from 'react';

const { Provider, Consumer } = React.createContext({});
export { Consumer };

export default class LoadingProvider extends React.Component {
  constructor(props) {
    super(props);

    this.state = {};
    this.setLoading = this.setLoading.bind(this);
  }

  setLoading(key, value) {
    const newState = {[key]: value};
    this.setState(newState);
  }

  render() {
    const context = {
      ...this.state,
      setLoading: this.setLoaindg,
    };
    
    return <Provider value={context}>{this.props.children}</Provider>
  }
}
```
### 6-4 컨텍스트로 모달 만들기

```jsx
import React, { PureComponent } from 'react';
import Modal from './Modal';
import Text from '../04/Text';
import Button from '../04/Button';

const { Provider, Consumer } = React.createContext({});
export { Consumer };

class ModalProvider extends PureComponent {
  constructor(props) {
    super(props);

    this.state = { showModal: false };
    this.handleClose = this.handleClose.bind(this);
    this.handleOpen = this.handleOpen.bind(this);
  }
  handleClose() {
    this.setState({ showModal: false });
  }
  handleOpen() {
    this.setState({ showModal: true });
  }
  render() {
    return (
      <Provider value={{ openModal: this.handleOpen, closeModal: this.handleClose }}>
        {this.props.children}
        {this.state.showModal && (
          <Modal>
            <div>
              <Text>정말로 삭제하시겠습니까?</Text>
            </div>
            <Button primary>예</Button>
            <Button onPress={() => this.setState({ showModal: false })}>아니요</Button>
          </Modal>
        )}
      </Provider>
    );
  }
}

export default ModalProvider;
```

### 6-5 입력 폼 만들며 컨텍스트 복습하기