# 6.리덕스로 상태 관리하기

리덕스의 장점 
* 컴포넌트 코드로부터 상태 관리 코드를 분리할 수 있다.
* 서버 렌더링 시 데이터 전달이 간편하다
* 로컬 스토리지에 데이터를 저장하고 불러오는 코드를 쉽게 작성할 수 있다.
* 같은 상탯값을 다수의 컴포넌트에서 필요로 할 때 좋다.
* 부모 컴포넌트에서 깊은 곳에 있는 자식 컴포넌트에 상탯값을 전달할 때 좋다.
* 알림창과 같은 전역 컴포넌트의 상탯값을 관리할 때 좋다.
* 페이지가 전환되어도 데이터는 살아 있어야 할 때 좋다.

### 6.1 리덕스 사용 시 따라야 할 세 가지 원칙

* 전체 상탯값을 하나의 객체에 저장한다.
* 상탯값은 불변 객체다.
* 상탯값은 순수 함수에 의해서만 변경되어야 한다.

##### 하나의 객체에 프로그램의 전체 상탯값을 저장한다.

##### 상탯값을 불변 객체로 관리한다.

상탯값은 오직 액션 객체에 의해서만 변경된다
```js
const incrementAction = {
  type: 'INCREMENT',
  amount: 123,
}
const conditionalIncrementAction = {
  type: 'CONDITIONAL_INCREMENT',
  amount: 2,
  gt: 10,
  lt: 100,
}
store.dispatch(incrementAction);
store.dispatch(conditionalIncrementAction);
```
dispatch에 의해서 상탯값이 변경된다.

##### 오직 순수 함수에 의해서만 상탯값을 변경해야 한다.

`(state, action) => nextState` => 리듀서의 구조

리듀서는 이전 상탯값과 액션 객체를 입력으로 받아서 새로운 상탯값을 만드는 순수 함수다.   
순수 함수는 부수 효과를 발생시키지 않아야 한다.(부수효과 => 전역변수의 값을 수정하거나 API 요청을 보내는 등 함수 외부의 상태를 변경시키는 것)   
또한 순수함수는 같은 인수에 대해 항상 같은 값을 반환해야 한다.    

```js
const now = new Date();
const hour = now.getHours();
const minute = now.getMinutes();
expect(sayHello1('홍길동')).toBe(
  `홍길동님 안녕하세요. 지금은 ${hour}시 ${minute}분 입니다.`
)
expect(sayHello2('홍길동', '11:30')).toBe(
  `홍길동님 안녕하세요. 지금은 11시 30분 입니다.`
)
```

sayHello2가 순수함수다 => 같은 인수에 대해 항상 같은 값을 반환

### 6.2 리덕스의 주요 개념 이해하기

액션 -> 미들웨어 -> 리듀서 -> 스토어

#### 6.2.1 액션
type 속성을 가진 자바스크립트 객체다.   

액션 타입을 유일한 값으로 만들기 위해 접두사 이용하기
```js
store.dispatch({ type: 'todo/ADD', title: '영화 보기', priority: 'high' })
store.dispatch({ type: 'todo/REMOVE', id: 123 })
store.dispatch({ type: 'todo/REMOVE_ALL' })
```

액션 타입은 변수로 만들어 관리한다.
```js
export const ADD = 'todo/ADD';
export const REMOVE = 'todo/REMOVE';
export const REMOVE_ALL = 'todo/REMOVE_ALL';

export function addTodo({ title, priority }) {
  return { type: ADD, title, priority };
}
export function removeTodo({ id }) {
  return { type: REMOVE, id };
}
export function removeAllTodo() {
  return { type: REMOVE_ALL };
}
```

#### 6.2.2 미들웨어
미들웨어는 리듀서가 액션을 처리하기 전에 실행되는 함수다.   

미들웨어의 기본구조   
`const middleware = store => next => action => next(action)`   

미들웨어를 설정하는 방법
```js
import { createStore, applyMiddleware } from 'redux';
const middleware1 = store => next => action => {
  console.log('middleware1 start');
  const result = next(action);
  console.log('middleware1 end');
  return result;
}
const middleware2 = store => next => action => {
  console.log('middleware2 start');
  const result = next(action);
  console.log('middleware2 end');
  return result;
}
const myReducer = (state, action) => {
  console.log('myReducer');
  return state;
}
const store = createStore(myReducer, applyMiddleware(middleware1, middleware2));
store.dispatch({ type: 'someAction' })
```

```
middleware1 start
middleware2 start
myReducer
middleware1 end
middleware2 end
```

##### 미들웨어 활용 예

로그를 출력해 주는 미들웨어
```js
const printLog = store => next => action => {
  const.log(`prev state = ${store.getState()}`);
  const result = next(action);
  const.log(`next state = ${store.getState()}`);
  return result;
}
```

실행을 연기할 수 있는 미들웨어
```js
const delayAction = store => next => action => {
  const delay = action.meta && action.meta.delay;
  if (!delay) {
    return next(action);
  }
  const timeoutId = setTimeout(() => next(action), delay);
  return function cancel() { // cancel을 호출하면 next 함수의 호출을 막을수 있다.
    clearTimeout(timeoutId);
  };
};
```

```js
const cancel = store.dispatch({
  type: 'SomeAction',
  meta: { delay: 1000 },
})
//...
cancel(); // middelware 액션 처리를 취소할 수 있다.
```

로컬 스토리지에 값을 저장하는 미들웨어 
```js
const saveToLocalStorage = store => next => action => {
  if (action.type === 'SET_NAME') {
    localStorage.setItem('name', action.name);
  }
  return next(action);
}
```

#### 6.2.3 리듀서
액션이 발생했을 때 새로운 상탯값을 만드는 함수 `(state, action) => nextState`

리듀서 함수의 작성 예
```js
function reducer(state = INTIAL_STATE, action) {
  switch (action.type) {
    //...
    case REMOVE_ALL:
      return {
        ...state,
        todos: [],
      };
    case REMOVE:
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.id),
      };
    default:
      return state;
  }
}

const INITIAL_STATE = { todos: [] };
```

중첩된 객체의 데이터 수정하기
```js
function reducer(state = INITIAL_STATE, action) {
  switch (action.type) {
    case ADD:
      return {
        ...state,
        todos: [
          ...state.todos,
          { id: getNewId(), title: action.title, priority: action.priority },
        ]
      }
  }
}
```

중첩되어 있으면 단계가 깊어질 수록 코드는 복잡해진다.(전개 연산자 많이 써야함)

##### 이머를 이용해서 리듀서 작성하기
```js
import product from 'immer';

const person = { name: 'mike', age: 22 };
const newPerson = produce(person, draft => {
  draft.age = 32;
})
```

이머를 사용해서 리듀서 함수 작성하기
```js
function reducer(state = INITIAL_STATE, action) {
  return produce(state, draft => {
    switch (action.type) {
      case ADD:
        draft.todos.push(action.todo); // immer를 사용했기 때문에 새로운 객체가 반환된다.
        break;
      case REMOVE_ALL:
        draft.todos = [];
        break;
      case REMOVE:
        draft.todos.filter(todo => todo.id !== action.todo.id);
        break;
      default:
        break;
    }
  })
}
```

##### 리듀서 작성 시 주의할 점: 순수 함수

```js
function reducer(state = INITIAL_STATE, action) {
  return produce(state, draft => {
    switch (action.type) {
      case SAY_HELLO:
        const random = Math.floor(Math.random() * 10 + 1); // 랜덤 함수는 값이 매번 달라지므로 호출 x
        // ...
        break;
      case INCREMENT:
        callApi({ url: '/', data: action }); // api 호출은 부수효과이기 때문에 API를 호출하는 함수는 순수 함수가 아니다. API 호출은 액션 생성자 함수나 미들웨어에서 한다.
    }
  })
}
```

##### createReducer 함수로 작성한 리듀서 함수
```js
const reducer = createReducer(INITIAL_STATE, {
  [ADD]: (state, action) => state.todos.push(action.todo),
  [REMOVE_ALL]: state => (state.todos = []),
  [REMOVE]: (state, action) => (state.todos = state.todos.filter(todo => todo.id !== action.id)),
});
```

#### 6.2.4 스토어
리덕스의 상탯값을 가지는 객체.   
스토어는 하나만 만드는 게 좋다.   

외부에서 상탯값 변경 여부를 알기 위해서는 스토어에 이벤트 처리 함수를 등록하면 된다.(like. typeorm의 subscribe)    

```js
const INITIAL_STATE = { value: 0 };
const reducer = createReducer(INITIAL_STATE, {
  INCREMENT: state => (state.value += 1),
});
const store = createStore(reducer);

let prevState;
store.subscribe(() => {
  const state = store.getState();
  if (state === prevState){
    console.log('상탯값 같음')
  } else {
    console.log('상탯값 변경됨')
  }
  prevState = state;
});

store.dispatch({ type: 'INCREMENT' });
```

### 6.3 데이터 종류별로 상탯값 나누기

리덕스 코드도 각 기능 폴더 하위에 작성해서 관리하는 게 좋다.

friend/state.js
```js
import createReducer from "../common/createReducer";

// 액션 타입
const ADD = 'friend/ADD';
const REMOVE = 'friend/REMOVE';
const EDIT = 'friend/EDI';

// 액션 생성자 함수
export const addFriend = friend => ({ type: ADD, friend })
export const removeFriend = friend => ({ type: REMOVE, friend });
export const editFriend = friend => {{ type: EDIT, friend }};

const INITIAL_STATE = { friends: [] };

// 리듀서 함수
const reducer = createReducer(INITIAL_STATE, {
  [ADD]: (state, action) => state.friends.push(action.friend),
  [REMOVE]: (state, action) => (state.friends = state.friends.filter(friend => friend !== action.friend.id)),
  [EDIT]: (state, action) => {
    const index = state.friends.findIndex(
      friend = friend.id === action.friend.id
    );
    if (index >= 0) {
      state.friends[index] = action.friend;
    }
  },
})

export default reducer;
```

timeline/state.js
```js
import createReducer from "../common/createReducer";

// 액션 타입
const ADD = "timeline/ADD";
const REMOVE = "timeline/REMOVE";
const EDIT = "timeline/EDI";
const INCREASE_NEXT_PAGE = 'timeline/INCREASE_NEXT_PAGE';

// 액션 생성자 함수
export const addTimeline = (timeline) => ({ type: ADD, timeline });
export const removeTimeline = (timeline) => ({ type: REMOVE, timeline });
export const editTimeline = (timeline) => ({ type: EDIT, timeline });
export const increaseNextPAge = () => ({ type: INCREASE_NEXT_PAGE });

const INITIAL_STATE = { timelines: [], nextPage: 0 };

// 리듀서 함수
const reducer = createReducer(INITIAL_STATE, {
  [ADD]: (state, action) => state.timelines.push(action.timeline),
  [REMOVE]: (state, action) =>
    (state.timelines = state.timelines.filter(
      (timeline) => timeline.id !== action.timeline.id
    )),
  [EDIT]: (state, action) => {
    const index = state.timelines.findIndex(
      (timeline = timeline.id === action.timeline.id)
    );
    if (index >= 0) {
      state.timelines[index] = action.timeline;
    }
  },
  [INCREASE_NEXT_PAGE]: (state, action) => {( state.nextPage += 1 )}
});

export default reducer;
```

combineReducre 함수 이용해서 reducer들 결합하기
```js
import { createStore, combineReducer } from 'redux';
import timeLineReducer, {
  addTimeline,
  removeTimeline,
  editTimeline,
  increaseNextPage
} from './timeline/state'

import friendReducer, {
  addFriend,
  removeFriend,
  editFriend,
} from './friend/state'

const reducer = combineReducer({
  timeline: timeLineReducer,
  friend: friendReducer,
})
const store = createStore(reducer);
store.subscribe(() => {
  const state = store.getState();
})

store.dispatch(addTimeline({ id: 1, desc: '코딩은 즐거워' }))
```

 
##### 리듀서에서 공통기능 분리하기

src/common/createItemsLogic
```js
import createReducer from "./createReducer";

export default function createItemsLogic(name) {
  const ADD = `${name}/ADD`;
  const REMOVE = `${name}/REMOVE`;
  const EDIT = `${name}/EDIT`;

  // 액션 생성자 함수
  const add = (item) => ({ type: ADD, item });
  const remove = (item) => ({ type: REMOVE, item });
  const edit = (item) => ({ type: EDIT, item })

  // 리듀서 함수
  const reducer = createReducer(
    { [name]: [] }, 
    {
      [ADD]: (state, action) => state[name].push(action.item),
      [REMOVE]: (state, action) => {
        const index = state[name].findIndex(item => item.id === action.item.id);
        state[name].splice(index, 1);
      },        
      [EDIT]: (state, action) => {
        const index = state[name].findIndex(
          (item = item.id === action.item.id)
        );
        if (index >= 0) {
          state[name][index] = action.item;
        }
      },
    }
  );

  return { add, remove, edit, reducer}
}
```

friend/state.js
```js
import createItemsLogic from '../common/createItemsLogic';

const { add, remove, edit, reducer } = createItemsLogic("friends");
export const addFriend = add;
export const removeFriend = remove;
export const editFriend = edit;
export default reducer;
```

combineReducer를 사용하게 되면 객체의 깊이가 깊어진다
```js
const state = {
  timeline: {
    common: {
      nextPage: 0
    }
  }
}
```
위와 같은 코드가 계속 나올수 있다.

### 6.4 리액트 상탯값을 리덕스로 관리하기

리액트 컴포넌트의 상태값과 마찬가지로 리덕스의 상탯값도 불변객체이기 때문에 둘이 잘 맞음   

```js
import React, { useEffect, useReducer } from 'react';
import store from '../../common/store';
import { getNextTimeLine } from '../../common/mockData';
import { addTimeLine } from '../state';
import TimelineList from '../component/TimelineList';

export default function TimelineMain() {
  const [, forceUpdate] = useReducer(v => v + 1, 0);
  useEffect(() => {
    const unsubscribe = store.unsubscribe(() => forceUpdate()); // 액션이 처리될때마다 다시그리기 위한 코드
    return () => unsubscribe();
  }, []);
  function onAdd() {
    const timeline = getNextTimeLine();
    store.dispatch(addTimeLine(timeline));
  };
  console.log("TimelineMain render");
  const timelines = store.getState().timeline.timelines;
  return (
    <div>
      <button onClick={onAdd}>타임라인추가</button>
      <TimelineList timelines={timelines}/>
    </div>
  )
}
```

실제 업데이트 되었을때만 화면 렌더링 시켜주기
```js
let prevTimelines = store.getState().timeline.timelines;
  useEffect(() => {
    const unsubscribe = store.unsubscribe(() =>{
      const timelines = store.getState().timeline.timelines;
      if(prevTimelines !== timelines) {
        forceUpdate() // 액션이 처리될때마다 다시그리기 위한 코드
      }
      prevTimelines = timelines;
    })
    return () => unsubscribe();
  }, []);
```

##### 6.4.2 react-redux 패키지 사용하기

```js

import store from './common/store';
import { Provider } from 'react-redux';
import TimelineMain from './timeline/container/TimelineMain';

ReactDOM.render(
  <Provider store={store}>
    <div>
      <TimelineMain />
    </div>
  </Provider>,
  document.getElementById('root')
);
```

```js
import { useSelector, useDispatch } from 'react-redux';


const timelines = useSelector(state => state.friend.friends);
  const dispatch = useDispatch();
  function onAdd() {
    const timeline = getNextTimeLine();
    dispatch(addTimeline(timeline));
  }
  return (
    <div>
      <button onClick={onAdd}>타임라인추가</button>
      <TimelineList timelines={timelines}/>
    </div>
  )
```

##### useSlector 훅으로 여러 상탯값 변경하기
* useSelector 훅을 필요한 상탯값 개수만큼 사용한다
* 메모이제이션을 이용한다
* useSelctor 훅의 두 번째 매개변수를 활용한다.


react-redux의 useSelector 훅을 이용해서 여러개의 상탯값을 반환하고 이 값에 따라 렌더링 여부를 결정해서 불필요한 렌더링을 막자!!

```js
import { shallowEqual } from 'react-redux';

export default function MyComponent() {
  const [value1, value2, value3] = useSelector(
    state => [state.value1, state.value2, state.value3],
    shallowEqual
  )
}
```


### reselect 패키지로 선택자 함수 만들기
=> 데이터 중에 10km이내의 사람들만 보여준다던가 해야하는 동작이 있을수 있는데 이때 reselect 패키지를 사용하면 좋다


### 6.6 리덕스 사가를 이용한 비동기 액션 처리

상탯값 변경은 비동기로 발생할 때가 많다(api콜로 값 받아오고 이걸 적용해야하므로)   
아래는 많이 쓰이는 비동기 액션 처리를 위한 패키지

|패키지명|선택기준|특징|
|---|---|---|
|redux-thunk|* 여러개의 비동기 코드가 중첩되지 않는다 <br> * 비동기 코드의 로직이 간단하다| 가장 간단하게 시작할 수 있다.|
|redux-observable|* 비동기 코드가 많이 사용된다.|* RxJS 패키지를 기반으로 만들어졌다. 따라서 리액티브 프로그래밍을 공부해야 하므로 진입 장벽이 가장 높다.|
|redux-saga|* 비동기 코드가 많이 사용된다|* 제너레이터를 적극적으로 활용한다. <br> * 테스트 코드 작성이 쉽다.|




