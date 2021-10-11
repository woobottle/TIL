# 3. 중요하지만 헷갈리는 리액트 개념 이해하기


// ui 라이브러리를 사용하지 않은 코드
```html
<html>
  <body>
    <div class="todo">
      <h3>할 일 목록</h3>
      <ul class="list"></ul>
      <input class="desc" type="text" />
      <button onClick="onAdd()">추가</button>
      <button onClick="onSaveToServer()">서버에 저장</button>
    </div>
    <script>
      let currentId = 1;
      const todoList = [];
      function onAdd(){
        const inputEl = document.querySelector('.todo .desc');
        const todo = { id: currentId, desc: inputEl.value };
        todoList.push(todo);
        currentId += 1;
        const elemList = document.querySelector('.todo .list');
        const liEl = makeTodoElement(todo);
        elemList.appendChild(liEl) 
      }
      function makeTodoElement(todo) {
        const liEl = document.createElement('li');
        const spanEl = document.createElement('span');
        const buttonEl = document.createElement('button');
        spanEl.innerHTML = todo.desc;
        buttonEl.innerHTML = '삭제';
        buttonEl.dataset.id = todo.id;
        buttonEl.onclick = onDelete;
        liEl.appendChild(spanEl);
        liEl.appendChild(buttonEl);
        return liEl;
      }
      function onDelete(e) {
        const id = Number(e.target.dataset.id);
        const index = todoList.findIndex(item => item.id === id);
        if (index >= 0){
          todoList.splice(index, 1);
          const elemList = document.querySelector('.todo .list');
          const liEl = e.target.parentNode;
          elemList.removeChild(liEl);
        }
      }
      function onSaveToServer() {
        // todoList 전송
      }
    </script>
  </body>
</html>
```

위의 코드를 react로 짜기
```jsx
function MyComponent() {
  const [desc, setDesc] = useState("");
  const [currentId, setCurrentId] = useState(1);
  const [todoList, setTodoList] = useState([]);
  function onAdd() {
    const todo = { id: currentId, desc };
    setCurrentId(currentId + 1);
    setTodoList({...todoList, todo})
  }
  function onDelete(e) {
    const id = Number(e.target.dataset.id);
    const newTodoList = todoList.filter(todo => todo.id !== id);
    setTodoList(newTodoList);
  }
  function onSaveToServer(){

  }
  return (
    <div>
      <h3>할 일 목록</h3>
      <ul>
        {todoList.map(todo => (
          <li key={todo.id}>
            <span>{todo.desc}</span>
            <button data-id={todo.id} onClick={onDelete}>삭제</button>
          </li>
        )}
      </ul>
      <input type="text" value={desc} onChange={e => setDesc(e.target.value)}/>
      <button onClick={onAdd}>추가</button>
      <button onClick={onSaveToServer}>서버에 전송</button>
    </div>
  )
}
```

### 컴포넌트의 속성값과 상태값

상태값을 이용하는 코드
```jsx
import React, { useState } from 'react';

function MyComponent() {
  const [color, setColor] = useState("red");
  function onClick() {
    setColor('blue');
  }

  return (
    <button style={{ backgroundColor: color }} onClick={onClick}>좋아요</button>
  )
}
```

속성값을 이용한 코드
```jsx
function Title(props) {
  return <p>{props.title}</p>
}
```

부모 컴포넌트에서 속성값을 내려 주는 코드
```jsx
function Todo() {
  const [count, setCount] = useState(0);
  function onClick() {
    setCount(count + 1);
  }
  return (
    <div>
      <Title title={`현재 카운트 ${count}`} />
      <button onClick={onClick}>증가</button>
    </div>
  )
}
```

이렇게 하면 부모가 재렌더링 될때마다 자식까지 재렌더링이 되어버림
이게 싫으면 `React.memo`를 사용해보자

```jsx
function Title(props) {
  return <p>{props.title}</p>
}

export default React.memo(Title)
```
이렇게 하면 title 속성값이 변할때만 Title을 렌더링 시켜버림

* 불변 객체로 관리하는 속성값과 상태값

속성값은 변경할 수 가 없다.
```jsx
function Title(props) {
  props.title = 'abc';
}
```

위의 코드는 불가! => 자식 컴포넌트에 전달되는 속성값은 상위 컴포넌트에서 관리하기 때문에 수정하지 못하도록 막혀있다!

상태값은 변경할 수 있다.
```jsx
function MyComponent() {
  const [count, setCount] = useState({ value: 0 });
  function onClick() {
    count.value = 2;
    setCount(count)
  }
}
```
=> 상태값을 직접 수정할수는 있지만 화면은 갱신 x
=> 상태값 변경함수를 호출해도 화면은 갱신 x
=> **리액트는 상태값 변경 유무를 이전 값과의 단순 비교를 통해 판단하는데 count 객체의 참조값은 그대로이다. 그래서 갱신 x**(virtual Dom 한번 짜봐야겠다.)

* 리액트 포털(portal)
=> 리액트 포털을 이용해서 특정 돔 요소에 리액트 요소를 렌더링 할 수 있다.
```jsx
function Modal({ title, desc }) {
  const domNode = document.getElementById("modal");
  return ReactDOM.createPortal(
    <div>
      <p>{title}</p>
      <p>{desc}</p>
    </div>,
    domNode,
  );
}
```

### 리액트 요소와 가상 돔
리액트 메모리에 가상 돔을 올려 놓고 이전과 이후를 비교하면서 변경된 부분만 실제 돔에 반영하는 전략을 취한다!!!

아래는 React가 createElement를 사용하는 예시
```jsx
const element = <a href="http://google.com">click</a>
const element = React.createElement(
  'a',
  { href: 'http://google.com' },
  'click here'
)
```

리액트 요소의 구조
```jsx
const element = (
  <a key="key1" style={{ width: 100 }} href="http://google.com">
    click here
  </a>
)
console.log(element);
const consoleLogResult = {
  type: 'a', // type 속성값이 문자열이면 HTML TAG!!
  key: 'key1', // 리액트 요소의 key값으로 들어감
  ref: null, // ref 속성값 입력해주면 들어옴
  props: {
    href: 'http://google.com",
    style: {
      widht: 100,
    },
    children: 'click here',
  },
  // ...
}
```

**리액트 요소는 불변 객체이다**
```jsx
const element = <a href="http://google.com">click here</a>;
element.type = 'b' // 에러
```

리액트는 전달된 리액트 요소를 이전의 리액트 요소와 비교해서 변경된 부분만 실제 돔에 반영한다.
```jsx
let seconds = 0
function update() {
  seconds += 1;
  const element = (
    <div>
      <h1>안녕하세요</h1>
      <h2>지금까지 {seconds}초가 지났습니다.</h2>
    </div>
  )
  ReactDOM.render(element, document.getElementById('root'));
}
setInterval(update, 1000); // 1초마다 h2의 부분만 업데이트 시킴
```

### 리액트 요소가 돔 요소로 만들어지는 과정
리액트에서 데이터 변경에 의한 화면 업데이트는 렌더 단계 + 커밋 단계
렌더 단계 => 실제 돔에 반경된 변경 사항을 파악하는 단계
커밋 단계 => 변경 사항을 실제 돔에 반영하는 단계

실제 돔으로 만드는 과정을 보여줄 예제 코드
```jsx
function Todo({ title, desc }) {
  cosnt [priority, setPriority] = useState("high");
  function onClick() {
    setPriority(priority === 'high' ? 'low' : 'high');
  }
  return (
    <div>
      <Title title={title} /> 
      <p>{desc}</p>
      <p>{priority === 'high' ? '우선순위 높음' : '우선순위 낮음'}</p>
      <button onClick={onClick}>우선순위 변경</button>
    </div>
  )
}

const Title = React.memo(({ title }) => {
  return <p style={{ color: "blue" }}>{title}</p>
});

ReactDOM.render(
  <Todo title="리액트 공부하기" desc="실전 리액트 프로그래밍을 열심히 읽는다"/>
  document.getElementById('root');
)
```

첫 번째로 만들어지는 리액트 요소
```jsx
const initialElementTree = {
  type: Todo,
  props: {
    title: '리액트 공부하기',
    desc: '실전 리액트 프로그래밍을 열심히 읽는다',
  }
}
```

Todo 컴포넌트 함수 호출 결과
```jsx
const elementTree = {
  type: 'div',
  props: {
    children: [
      {
        type: Title,
        props: { title: '실전 리액트 공부하기' },
      },
      {
        type: 'p',
        props: { children: '실전 리액트 프로그램이을 열심히 읽는다' },
      },
      {
        type: 'p',
        props: { children: '우선순위 높음' },
      },
      {
        type: 'button',
        props: {
          onClick: function() {
            /* Todo 컴포넌트의 onClick 함수 */
          },
          children: '우선순위 변경',
        }
      }
    ],
  }
}
```
1. 트리의 루트는 div로 변경된다.
2. 아직 Title 컴포넌트가 존재하기 때문에 실제 돔으로 되지는 않는다.
3. 리액트 요소가 실제 돔으로 만들어지기 위해서는 모든 리액트 요소의 type 속성이 문자열이여야 한다.(이래야 html로 변환 가능)

Title 컴포넌트 함수 호출 결과
```js
const elementTree = {
  type: 'div',
  props: {
    children: [
      {
        type: 'p',
        props: {
          style: { color: 'blue' },
          children: '리액트 공부하기',
        },
      }, // 이 부분이 Title 컴포넌트 실행으로인해 바뀐거
      {
        type: 'p',
        props: {
          children: '실전 리액트 프로그래밍을 열심히 읽는다',
        }
      }
    ]
  }
}
```

위의 코드를 보면 전부다 type이 문자열이다. 이 형태가 가상 돔이다.

엄밀히 말하면 리액트 요소는 파이퍼(fiber)라는 구조체로 변환한다. 파이버는 리액트 버전 16부터 도입된 구조체 이름.
파이버로 동작할때도 모든 type속성값이 문자열이 될 때까지 연산한 다는 사실에는 변함 x


리액트 훅 기초 익히기
-----

### 상탯값 추가하기: useState


배치로 처리되는 상탯값 변경 함수
```jsx
function MyComponent() {
  const [count, setCount] = useState({ value: 0 });
  function onClick() {
    setCount({ value: count.value + 1}) 
    setCount({ value: count.value + 1})
  }
  console.log('render called'); // 1번만 실행된다
  return (
    <div>
      <h2>{count.value}</h2>
      <button onClick={onClick}>증가</button>
    </div>
  )
}
```
1. count는 1만 올라간다. 상태값 변경함수는 비동기로 동작한다.
2. 리액트는 효율적으로 렌더링하기 위해 여러 개의 상탯값 변경 요청을 배치로 처리한다.
3. onClick 함수가 호출되어도 로그는 한번만 출력됨.

위의 상황을 해결하려면 아래와 같이 수정하자!!
```jsx
function MyComponent() {
  const [count, setCount] = useState(0);
  function onClick() {
    setCount(prev => prev + 1);
    setCount(prev => prev + 1);
  }
}
```

=> 상탯값 변경 함수로 입력된 함수는 자신이 호출되기 직전의 상탯값을 매개변수로 받는다.

상탯값 변경 함수는 비동기로 처리되지만 그 순서가 보장된다.

useState훅 하나로 여러 상탯값 관리하기
```jsx
import React, { useState } from 'react';

function Profile() {
  const [state, setState] = useState({ name: '', age: 0 });
  return (
    <div>
      <p>{state.name}</p>
      <p>{state.age}</p>
      <input 
        type="text"
        value={state.name}
        onChange={e => setState({ ...state, name: e.target.value })}
      />
      <input 
        type="text"
        value={state.age}
        onChange={e => setState({ ...state, age: e.target.value })}
      />
    </div>
  )
}
```

### 컴포넌트에서 부수 효과 처리하기: useEffect
useEffect 훅의 사용 예시
```jsx
import React, { useState, useEffect } from 'react';

function MyComponent() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    document.title = `업데이트 횟수 ${count}`
  });
  return <button onClick={() => setCount(count + 1)}>increase</button>
}
```

1. useEffect는 렌더링 결과가 실제 돔에 반영된 후 호출된다
2. 버튼을 클릭할때마다 렌더링이 되고 렌더링이 끝나면 useEffect 호출

useEffect 훅에서 API 호출하기
```jsx
import React, { useState, useEffect } from 'react';

function Profile({ userId }) {
  const [user, setUser] = useState(null);
  useEffect(
    () => {
      getUserApi(userId).then(data => setUser(data));
    }, [userId],
  );
  return (
    <div>
      {!user && <p>사용자 정보를 가져오는 중..</p>}
      {user && (
        <>
          <p>{user.name}</p>
          <p>{user.age}</p>
        </>
      )}
    </div>
  )
}
```
의존성 배열안의 값이 변경될때만 useEffect가 호출됨

useEffect 훅을 이용해서 이벤트 처리 함수를 등록하고 해제하기
```jsx
import React, { useEffect, useState } from 'react';

function WidthPrinter() {
  const [width, setWidth] = useState(window.innerWidth);
  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener('resize', onResize);
    return () => {
      window.removeEventListener('resize', onResize);
    }
  }, []);
}
```

1. useEffect 에서 반환된 함수는 useEffect 함수가 호출되기 직전에 호출되고, 컴포넌트가 사라지기 직전에 마지막으로 호출된다.
2. 의존성 배열로 빈 배열을 입력하면 컴포넌트가 생성될 때만 useEffect가 호출되고, 컴포넌트가 사라질 때만 반환된 함수가 호출된다.

### 훅 직접 만들기
커스텀 훅을 이름은 use로 시작하기

useUser 커스텀 훅
```jsx
function useUser(userId) {
  const [user, setUser] = useState(null);
  useEffect(() => {
    getUserApi(userId).then(data => setUser(data));
  }, [userId]);
  return user;
}

function Profile({ userId }){
  const user = useUser(userId);
}
```

### 훅 사용 시 지켜야 할 규칙

1. 하나의 컴포넌트에서 훅을 호출하는 순서는 항상 같아야 한다.
2. 훅은 함수형 컴포넌트 또는 커스텀 훅 안에서만 호출되어야 한다.

위반한 경우
```jsx
function MyComponent() {
  const [value, setValue] = useState(0);

  // 조건에 따라 훅을 호출하면 순서가 보장 되지 않음
  if (value === 0) {
    const [v1, setV1] = useState(0)
  } else {
    const [v1, setV1] = useState(0)
    const [v2, setV2] = useState(0)
  }
  // 루프 안에서 호출하는 것도 순서 보장 x
  for(let i =0; i< value; i ++) {
    const [num, setNum] = useState(0)
  })
  // func1() 함수가 언제 호출될지 몰라서 순서 보장 x
  function func1() {
    const [num, setNum] = useState(0)
  }
}
```

여러개의 훅 사용하기
```jsx
functon Profile() {
  const [age, setAge] = useState(0);
  const [name, setName] = useState('');

  useEffect(() => {
    setAge(23);
  }, [])
}
```

=> **리액트가 age와 name 상탯값을 구분할 수 있는 유일한 정보는 훅이 사용된 순서다.**
=> 만약 setAge가 실행되지 않았더라면 name의 값이 23이 될것이다.

리액트가 내부적으로 훅을 처리하는 방식
```jsx
let hooks = null;

export function useHook() {
  hooks.push(hookData);
}

function process_a_component_rendering(component) {
  hooks = []; 
  component(); // 컴포넌트 내부에서 hook을 사용한 만큼 hooks 배열에 데이터를 추가한다. 그래서 순서가 중요
  let hooksForThisComponent = hooks; // 생성된 배열을 저장
  hooks = null;
}
```

리액트는 훅이 사용된 순서를 저장하고 배열에 저장된 순서를 기반으로 훅을 관리한다.

콘텍스트 API로 데이터 전달하기
-----

콘텍스트 api를 사용하지 않은 코드
```jsx
function App() {
  return (
    <div>
      <div>상단 메뉴</div>
      <Profile usename="mike" />
      <div>하단 메뉴</div>
    </div>
  );
}

function Profile({ username }) {
  return (
    <div>
      <Greeting username={username} />
    </div>
  )
}

function Greeting({ username }) {
  return <p>{username}</p>
}
```

컨텍스트 api를 사용한 코드
```jsx
const UserContext = React.createContext('');

function App() {
  return (
    <div>
      <UserContext.Provider value="mike">
        <div>상단 메뉴</div>
        <Profile />
        <div>하단 메뉴</div>
      </UserContext.Provider>
    </div>
  )
}

function Profile() {
  return (
    <div>
      <Greeting />
    </div>
  )
}

function Greeting() {
  return (
    <UserContext.Consumer>
      {username => <p>{username}</p>}
    </UserContext.Consumer>
  )
}
```

`React.createContext(defaultValue) => {Provider, Consumer}`

Consumer 컴포넌트는 값을 찾기위해 상위로 올라가면서 가까운 Provider 컴포넌트를 찾는다. 만약 못찾으면 기본값이 사용됨

* Provider 컴포넌트의 속성값이 변경되면 하위의 모든 Consumer 컴포넌트는 다시 렌더링 된다.
* 중요한 점은 중간에 위치한 컴포넌트의 렌더링 여부와 상관없이 Consumer 컴포넌트는 다시 렌더링 된다.

Profile 컴포넌트가 다시 렌더링 되지 않도록 React.memo를 사용한 코드
```jsx
const UserContext = React.createContext('');

function App() {
  const [username, setUsername] = useState('');
  return (
    <div>
      <UserContext.Provider value={username}>
        <Profile />
      </UserContext.Provider>
      <input 
        type="text"
        value={username}
        onChange={e => setUsername(e.target.value)}
      />
    </div>
  )
}

const Profile = React.memo(() => {
  return (
    <div>
      <Greeting />
    </div>
  )
}

function Greeting() {
  return (
    <UserContext.Consumer>
      {username => <p>{username}</p>}
    </UserContext.Consumer>
  )
}
```

1. username 상태값이 변경되면 App 컴포넌트는 다시 렌더링 된다.
2. Profile 컴포넌트는 React.memo로 만들어 졌고 속성값이 없기 때문에 최초 한 번만 렌더링
3. Profile 컴포넌트의 렌더링 여부와 상관없이 Greetin 컴포넌트의 Consumer 컴포넌트는 다시 렌더링 된다.
4. 위의 방법으로 중간 컴포넌트의 렌더링 여부와 상관없이 Provider 컴포넌트의 값이 변경되면 Consumer 컴포넌트가 다시 렌더링 된다.

### 컨텍스트 API 활용하기

여러 컨텍스트를 중첩해서 사용하기
```jsx
const UserContext = React.createContext('');
const ThemeContext = React.createContext('dark');

function App() {
  return (
    <div>
      <ThemeContext.Provider value="light">
        <UserContext.Provider value="mike">
          <Profile />
        </UserContext.Provider>
      </ThemeContext.Provider>
    </div>
  )
}

function Profile() {
  return (
    <div>
      <Greeting />
    </div>
  )
}

function Greeting() {
  return (
    <ThemeContext.Consumer>
      {theme => (
        <UserContext.Consumer>
          {username => (
            <p
              style={{ color: theme === 'dark' ? 'gray' : 'green' }}
            >{username}
            </p>
          )}
        </UserContext.Consumer>
      )}
    </ThemeContext.Consumer>
  )
}
```

1. Provider 컴포넌트를 중첩해서 사용 가능
2. Consumer 컴포넌트도 중첩해서 사용 가능
3. 데이터 변경시 해당 Consumer 컴포넌트만 렌더링 된다.

하위 컴포넌트에서 콘텍스트 데이터를 수정하기
```jsx
const UserContext = React.createContext({ username '', helloCount: 0 });
const SetUserContext = React.createContext(() => {});

function App() {
  const [user, setUser] = useState({ username: 'mike', helloCount: 0 });
  return (
    <div>
      <SetUserContext.Provider value={setUser}>
        <UserContext.Provider value={user}>
          <Profile />
        </UserContext.Provider>
      </SetUserContext.Provider>
    </div>
  )
}

function Greeting() {
  return (
    <SetUserContext.Consumer>
      {setUser => (
        <UserContext.Consumer>
          {({username, helloCount }) = (
            <React.Fragment>
              <p>{username}</p>
              <p>{helloCount}</p>
              <button
                onClick={() => 
                  setUser({ username, helloCount: helloCount + 1})
                }
              >인사하기</button>
            </React.Fragment>
          )}
        </UserContext.Consumer>
      )}
    </SetUserContext.Consumer>
  )
}
```

### 컨텍스트 API 사용 시 주의할 점

불필요한 렌더링이 발생하는 예
```jsx
const UserContext = React.createContext({ username: '' });

function App() {
  const [username, setUsername] = useState("");
  return (
    <div>
      <UserContext.Provider value={{ username }}>
    </div>
  )
}
```
1. 컴포넌트가 렌더링 될때마다 새로운 객체가 생성된다

불필요한 렌더링이 발생하지 않는 코드
```jsx
function App() {
  const [user, setUser] = useState({ username: "" })
  return (
    <div>
      <UserContext.Provider value={user}>
    </div>
  )
}
```
1. 컨텍스트 데이터 전체를 상탯값으로 관리한다.
2. username 값이 변경될 때만 새로운 객체가 전달되므로 불필요한 렌더링이 발생하지 않는다.

### ref 속성값으로 자식 요소에 접근하기

돔 요소에 접근하기 위해 ref 속성값을 사용한 예
```jsx
import React, { useRef, useEffect } from 'react';

function TextInput() {
  const inputRef = useRef();

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return (
    <div>
      <input type="text" ref={inputRef} />
      <button>저장</button>
    </div>
  )
}
```


함수형 컴포넌트에서 ref 속성값을 사용한 예
```jsx
function TextInput({ inputRef }) {
  return (
    <div>
      <input type="text" ref={inputRef} />
      <button>저장</button>
    </div>
  )
}

function Form() {
  const inputRef = useRef();
  useEffect(() => {
    inputRef.current.focus();
  }, []);
  return (
    <div>
      <TextInput inputRef={inputRef} />
      <button onClick={() => inputRef.current.focus()}>텍스트로 이동</button>
    </div>
  )
}
```
위의 코드에서 일관성을 위해 ref라는 속성값으로 사용하는게 좋다. 하지만 컴포넌트에 ref 속성값을 사용하면 리액트가 내부적으로 처리해버리기 때문에 손자 요소에 연결할 수가 없다. 이런경우 forwardRef 함수를 사용

forWardRef 함수로 ref 속성값을 직접 처리하기
```jsx
const TextInput = React.forwardRef((props, ref) => {
 <div>
   <input type="text" ref={ref} />
   <button>저장</button>
 </div>
})

function Form() {
  return (
    <div>
      <TextInput ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>텍스트로 이동</button>
    </div>
  )
}
```

=> 아 ref 그대로 사용하기 위해서 사용하는 거구나


ref 속성값으로 함수 사용하기
```jsx
function Form() {
  const [text, setText] = useState(INITIAL_TEXT);
  const [showText, setShowText] = useState(true);
  return (
    <div>
      {showText && (
        <input 
          type="text"
          ref={ref => ref && setText(INITIAL_TEXT)}
          value={text}
          onChange={e => setText(e.target.value)}
        />
      )}
      <button onClick={() => setShowText(!showText)}>
        보이기/가리기
      </button>
    </div>
  )
}

const INITIAL_TEXT = '안녕';
```
1. 위 함수는 input에 값을 넣어도 값이 바뀌지 않는다.
2. 렌더링 될때마다 새로운 함수를 ref 속성값으로 넣고 있기 때문이다.
3. 리액트는 ref 속성값으로 새로운 함수가 들어오면 이전 함수에 null을 넣어서 호출하고, 새로운 함수에는 요소의 참조값을 넣어서 호출한다. 
4. 텍스트가 입력되면 컴포넌트가 렌더링 되고, ref 속성값에 입력된 새로운 함수가 호출되면서 text는 계속 INITIAL_TEXT로 바뀌어 버린다.

ref 속성값으로 고정된 함수 사용하기
```jsx
function Form() {
  const [text, setText] = useState(INITIAL_TEXT);
  const [showText, setShowText] = useState(true);
  const setInitialText = useCallback(ref => ref && setText(INITIAL_TEXT), []) // useCallback의 메모이제이션 기능을 사용하자!

  return (
    <div>
      {showText && (
        <input 
          type="text"
          ref={setInitialText}
          value={text}
          onChange={e => setText(e.target.value)}
        />
      )}
      <button onClick={() => setShowText(!showText)}>
        보이기/가리기
      </button>
    </div>
  )
}

const INITIAL_TEXT = '안녕';
```

리액트 내장 훅 살펴보기
----

### Consumer 컴포넌트 없이 콘텍스트 사용하기: useContext

훅을 사용지 않고 콘텍스트 API를 사용하기
```jsx
const UserContext = React.createContext();
const user = { name: 'mike', age:23 };

function ParentComponent() {
  return (
    <UserContext.Provider value={user}>
      <ChildComponent />
    </UserContext.Provider>
  )
}

function ChildComponent() {
  return (
    <div>
      <UserContext.Consumer>
        {user => (
          <>
            <p>{user.name}</p>
            <p>{user.age}</p>
          </>
        )}
      </UserContext.Consumer>
    </div>
  )
}
```

useContext 훅 사용하기
```jsx
function ChildComponent() {
  const user = useContext(UserContext);
  console.log(user.name)
}
```
=> 이 훅을 사용하면 간편해진다.

### 렌더링과 무관한 값 저장하기: useRef

```jsx
import React, { useState, useRef, useEffect } from 'react';

function Profile() {
  const [age, setAge] = useState(20);
  const prevAgeRef = useRef(20);
  useEffect(() => {
    prevAgeRef.current = age;
  }, [age])
  const prevAge = prevAgeRef.current;
  const text = age === prevAge ? 'same' : age > prevAge ? 'older' : 'younger';
  return (
    <div>
      <p>{age}</p>
      <button 
        onCli={() => {
          const age = Math.floor(Math.random() * 50 + 1)
          setAge(age)
        }}  
      >
        나이 변경
      </button>
    </div>
  )
}
```

### 메모이제이션 훅: useMemo, useCallback

* useMemo
=> useMemo 훅은 계산량이 많은 함수의 반환값을 재활용하는 용도로 사용된다.
```jsx
import React, { useMemo } from 'react';
import { runExpensiveJob } from './util';

function MyComponent({ v1, v2 }) {
  const value = useMemo(() => runExpensiveJob(v1, v2), [v1, v2]);
  return <p>{value}</p>
}
```
1. useMemo훅은 이 함수가 반환한 값을 기억한다.
2. useMemo내의 의존성 배열이 변경되지 않ㄴ으면 이전에 반환된 값을 재사용 한다.
3. 배열의 값이 변경됐으면 첫 번째 매개변수로 입력된 함수를 실행하고 그 반환값을 기억한다.

* useCallback

useCallback이 필요한 예시
```jsx
import React, { useState } from 'react';
import { saveToServer } from './api';
import UserEdit from './UserEdit';

function Profile() {
  const [name, setName] = useState('');
  const [age, setAge] = useState(0);
  return (
    <div>
      <p>{name}</p>
      <p>{age}</p>
      <UserEdit 
        onSave={() => saveToServer(name, age)}
        setName={setName}
        setAge={setAge}
      />
    </div>
  )
}
```

1. Profile 컴포넌트가 렌더링 될때마다 UserEdit 컴포넌트의 onSave속성값으로 새로운 함수가 입력된다.
2. 따라서 UserEdit에 React.memo를 사용해도 속성값이 매번 바뀌기 때문에 렌더링된다.
3. useCallback 훅을 사용해서 불필요한 렌더링을 막자

useCallback 훅 사용하기
```jsx
import React, { useState, useCallback } from 'react';
import { saveToServer } from './api';
import UserEdit from './UserEdit';

function Profile() {
  const [name, setName] = useState('');
  const [age, setAge] = useState(0);
  const onSave = useCallback(() => saveToServer(name, age), [name, age])
  return (
    <div>
      <p>{name}</p>
      <p>{age}</p>
      <UserEdit 
        onSave={onSave}
        setName={setName}
        setAge={setAge}
      />
    </div>
  )
}
```
1. useCallback내의 의존성 배열의 값이 변하지 않는이상 이전에 생성된 함수가 재사용 된다.


### 컴포넌트의 상탯값을 리덕스처럼 관리하기: useReducer

```jsx
import React, { useReducer } from 'react';

const INITIAL_STATE = { name: 'empty', age: 0 }
function reducer(state, action) {
  switch (action.type) {
    case 'setName' :
      return { ...state, name: action.name }
    case 'setAge' :
      return { ...state, age: action.age }
    default: 
      return state;
  }
}

function Profile() {
  const [state, dispatch] = useReducer(reducer, INITIAL_STATE);
  return (
    <div>
      <p>{state.name}</p>
      <p>{state.age}</p>
      <input 
        type="text"
        value={state.name}
        onChange={e => 
          dispatch({ type: 'setName', name: e.currentTarget.value })
        }
      />
      <input 
        type="number"
        value={state.age}
        onChange={e => 
          dispatch({ type: 'setAge', name: e.currentTarget.value })
        }
      />
    </div>
  )
}
```

useReducer 훅과 컨텍스트 api를 이용해서 이벤트 처리 함수를 전달하기
```jsx
export const ProfileDispatch = React.createContext(null);

function Profile() {
  const [state, dispatch] = useReducer(reducer, INITIAL_STATE);
  return (
    <div>
      <p>{state.name}</p>
      <p>{state.age}</p>
      <ProfileDispatch.Provider value={dispatch}>
        <SomeComponent />
      </ProfileDispatch.Provider>
    </div>
  )
}
```

### 부모 컴포넌트에서 접근 가능한 함수 구현하기: useImperativeHandle
부모 컴포넌트에서 접근이 가능한 함수를 구현해보자
```jsx
import React, { forwardRef, useState, useImperativeHandle } from 'react';

function Profile(props, ref) {
  const [name, setName] = useState('');
  const [age, setAge] = useState(0);

  useImperativeHandle(ref, () => ({
    addAge: value => setAge(age + value),
    getNameLength: () => name.length,
  }));

  return (
    <div>
      <p>{name}</p>
      <p>{age}</p>
    </div>
  )
}

export default forwardRef(Profile);
```

1. 부모 컴포넌트에서 입력한 ref 객체를 직접 처리하기 위해 `forwardRef` 함수 호출
2. useImperativeHandle 훅으로 ref 객체와 부모 컴포넌트에서 접근 가능한 여러 함수를 입력한다.

부모 컴포넌트에서 자식 컴포넌트 함수 호출하기
```jsx
function Parent() {
  const profileRef = useRef();
  const onClick = () => {
    if (profileRef.current) {
      console.log(profileRef.current.getNameLength());
      profileRef.current.addAge(5);
    }
  };

  return (
    <div>
      <Profile ref={profileRef}/>
      <button onClick={onClick}>add age 5</button>
    </div>
  )
}
```

React.memo, useState, useEffect, useContext, useRef, useCallback