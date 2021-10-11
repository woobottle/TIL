# 4. 리액트 실전 활용법

useEffect 훅을 제대로 사용하는 방법
가독성과 생산성을 높이는 컴포넌트 코드 작성 방법
렌더링 속도를 올리기 위한 성능 최적화 방법

### 가독성과 생산성을 고려한 컴포넌트 코드 작성법

* 추천하는 컴포넌트 파일 작성법

```jsx
MyComponent.propTypes = {}

export default function MyComponent({ prop1, prop2 });

const COLUMNES = [
  { id: 1, name: 'phoneNumber', width: 200, color: 'white'},
  { id: 2, name: 'city', width: 100, color: 'grey' }
];

const URL_PRODUCT_LIST = '/api/products';
function getTotalPrice({ price, total })
```
1. 파일의 최상단에는 속성값 타입 정의
2. 컴포넌트 바깥의 변수와 함수는 파일의 가장 밑에 정의한다.

서로 연관된 코드를 한 곳으로 모으기
```jsx
function Profile({ userId }) {
  const [user, setUser] = useState(null);
  const [width, setWidth] = useState(window.innerWidth);
  useEffect(() => {
    getUserApi(userId).then(data => setUser(data));
  }, [userId])
  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", onResize);
    return () => {
      window.removeEventListener("resize", onResize);
    };
  }, []);
}
```

1. 모든 상태값을 컴포넌트 상단에서 정의함


기능별로 코드를 구분하기
```jsx
function Profile({ userId }) {
  const [user, setUser] = useState(null);
  useEffect(() => {
    getUserApi(userId).then(data => setUser(data));
  }, [userId])
  
  const [width, setWidth] = useState(window.innerWidth);
  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", onResize);
    return () => {
      window.removeEventListener("resize", onResize);
    };
  }, []);
}
```

1. 기능별로 코드를 구분하였다. 
2. 코드를 한 곳에 모을때는 연관된 코드끼리 모으는 게 좋다.

각 기능을 커스텀 훅으로 분리하기
```jsx
function Profile({ userId }) {
  const user = useUser(userId);
  const width = useWindowWidth();
}

function useUser(userId) {
  const [user, setUser] = useState(null);
  useEffect(() => {
    getUserApi(userId).then(data => setUser(data));
  }, [userId])
  return user;
}

function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);
  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", onResize);
    return () => {
      window.removeEventListener("resize", onResize);
    };
  }, []);
  return width;
}
```

1. 기능을 재사용하는 곳이 없다고 하더라도 컴포넌트 코드가 복잡해지면 커스텀 훅으로 분리하자!!!

* 속성값 타입 정의하기: prop-types

속성값의 타입 정보는 컴포넌트 코드의 가독성을 위해서 필수로 작성하는 게 좋다.
prop-types는 타입을 제공하기 위한 리액트 공식 패키지이다. 

속성값에 타입 정보가 없는 경우
```jsx
function User({ type, age, male, onChangeName, onChangeTitle }) {
  function onClick1() {
    const msg = `${type} ${age}`;

  }
}
```

prop-types를 이용한 속성값의 타입 정보 정의
```jsx
User.propTypes = {
  male: PropTypes.bool.isRequired,
  age: PropTypes.number,
  type: PropTypes.oneOf(["gold", "silver", "bronze"]),
  onChangeName: PropTypes.func,
  onChangeTitle: PropTypes.func.isRequired,
}
```


* 가독성을 높이는 조건부 렌더링 방법
  
간단한 조건부 렌더링 예
```jsx
function GreetingA({ isLogin, name }) {
  if (isLogin) {
    return <p></p>
  } else {
    return <p>권한x</p>
  }
}
```

&& 연산자와 삼항 연산자를 활용해서 조건부 렌더링을 효율적으로 조져보자

&& 연산자 사용시 주의할 점
> 숫자 0은 false 이고 빈 문자열도 false 이다!

* 관심사 분리를 위한 프레젠테이션, 컨테이너 컴포넌트 구분하기

속성값으로부터 새로운 상탯값을 만드는 예
```jsx
function Mycomponent({ todos }) {
  const [doneList, setDoneList] = useState(todos.filter(item => item.done));
  function onChangeName(key, name) {
    setDoneList(
      doneList.map(item => (item.key === key ? {...item, name} : item))
    )
  }
}
```

=> 특정이름을 수정하는 순간 부모가 가진 데이터와 sync가 맞지 않게 된다. (todos prop으로 받아와서 조지기 때문)
이렇게 자식 컴포넌트에서 부모의 데이터를 별도의 상탯값으로 관리하는 것은 안티 패턴이다.

컴포넌트는 재사용할수록 이득인데 비즈니스 로직이나 상탯값을 가지고 있으면 재사용하기 힘들다.

책의 저자가 추천하는 프레젠테이션 컴포넌트의 정의
* 비즈니스 로직이 없다
* 상탯값이 없다. 단 마우스오버와 같은 UI 효과를 위한 상탯값은 제외한다.

### useEffect 훅 실전 활용법

* 의존성 배열을 관리하는 방법

```jsx
function Profile({ userId }) {
  const [user, setUser] = useState();
  useEffect(() => {
    fetchUser(userId).then(data => setUser(data));
  }, [])
}
```
위의 코드는 렌더링이 될때마다 api가 호출되므로 비효율적이다.

```jsx
function Profile({ userId }) {
  const [user, setUser] = useState();
  useEffect(() => {
    fetchUser(userId).then(data => setUser(data));
  }, [userId])
}
```
userId가 변경될때만 api가 호출되게 하자

* useEffect 훅에서 async/await 사용하기

```jsx
useEffct(async() => {
  const data = await fetchUser(userId);
  setUser(data);
}, [userId])
```

1. 이렇게 하면 에러 난다. useEffect 훅의 반환값은 항상 함수 타입이어야 하는데 이렇게 하면 Promise객체가 반환된다.

이것의 해결책
```jsx
useEffect(() => {
  async function fetchAndSetUser() {
    const data = await fetchUser(userId);
    setUser(data);
  }
  fetchAndSetUser();
}, [userId])
```

**useEffect 훅 내에서 async await 함수를 만들고 호출시키자**

제일 좋은 형태!!
useCallback 활용해서 렌더링 될때마다 함수 재정의 되게 하지 않고 useEffect 외부에서 async/await 함수 정의
```jsx
function Profile({ userId }) {
  const [user, setUser] = useState();
  const fetchAndSetUser = useCallback(
    async needDetail => {
      const data = await fetchUser(userId, needDetail);
      setUser(data);
    }, [userId]
  );
  useEffect(() => {
    fetchAndSetUser(false);
  }, [fetchAndSetUser])
}
```
1. useCallback을 이용 fetchAndSetUser 함수가 필요할 때만 갱신되도록 개선
2. fetchAndSetUser 함수는 userId가 변경될때만 호출된다.


### 의존성 배열을 없애는 방법

useEffect 함수 내에서 분기처리하기
```jsx
function Profile({ userId }) {
  const [user, setUser] = useState();
  async function fetchAndSetUser(needDetail) {
    const data = await fetchUser(userId, needDetail);
    setUser(data);
  }
  useEffect(() => {
    if (!user || user.id !== userId) {
      fetchAndSetUser(false);
    }
  })
}
```

1. if 문으로 fetchAndSetUser 호출 시점을 관리한다.
2. 이렇게 의존성 배열을 입력하지 않으면 useEffect 내에서 사용된 모든 변수는 가장 최신화된 값을 참조하게 된다.


* useState의 상탯값 변경 함수에 함수 입력하기

이전 상탯값을 기반으로 다음 상탯값을 계산하는 경우
```jsx
function MyComponent() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    function onClick() {
      setCount(count + 1);
    }
    window.addEventListener("click", onClick);
    return () => window.removeEventListener("click", onClick);
  }, [count]);
}
```

상탯값 변경 함수에 함수를 입력해서 의존성 배열을 제거
```jsx
function MyComponent() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    function onClick() {
      setCount(prev => prev + 1);
    }
    window.addEventListener("click", onClick);
    return () => window.removeEventListener("click", onClick);
  })
}
```

* useReducer 활용하기
  
여러 상탯값을 참조하면서 값을 변경하는 코드
```jsx
function Timer({ initialTotalSeconds }) {
  const [hour, setHour] = useState(Math.floor(initialTotalSeconds / 3600));
  const [minute, setMinute] = useState(
    Math.floor((initialTotalSeconds % 3600) / 60)
  );
  const [second, setSecond] = useState(initialTotalSeconds % 60);

  useEffect(() => {
    const id = setInterval(() => {
      if (second) {
        setSecond(second - 1);
      } else if (minute) {
        setMinute(minute - 1);
        setSecond(59);
      } else if (hour) {
        setHour(hour - 1);
        setMinute(59);
        setSecond(59);
      }
    }, 1000);
    return () => clearInterval(id);
  }, [hour, minute, second]);
}
```

useReducer 훅을 사용해서 의존성 배열을 제거
```jsx
function Timer({ initialTotalSeconds }) {
  const [state, dispatch] = useReducer(reducer, {
    hour: Math.floor(initialTotalSeconds / 3600),
    minute:  Math.floor((initialTotalSeconds % 3600) / 60),
    second: initialTotalSeconds % 60,
  });
  const { hour, minute, second } = state;
  useEffect(() => {
    const id = setInterval(dispatch, 1000); // dispatch는 변하지 않는 값이므로 의존성 배열을 삭제할 수 있다.
    return () => clearInterval(id);
  });
}

function reducer(state) {
  const { hour, minute, second } = state
  if (second) {
    return { ...state, second: second - 1}
  } else if (minute) {
    return { ...state, minute: minute - 1, second: 59}  
  } else if (hour) {
    return { hour: hour - 1, minute: 59, second: 59 }
  } else {
    return state;
  }
}
```

* useRef 활용하기

자주 변경되는 속성값을 의존성 배열에 추가한 코드
```jsx
function MyComponent({ onClick }) {
  useEffect(() => {
    window.addEventListener("click", () => {
      onClick();
    })
  }, [onClick]);
}
```

1. 속성값으로 전달되는 함수는 그대로인데 렌더링 할때마다 변경되는 경우가 많다(useRef 내에서 함수값 그대로 사용하는 경우 등)

useRef 훅으로 useEffect 함수가 자주 호출되지 않도록 개선
```jsx
function MyComponent({ onClick }) {
  const onClickRef = useRef();
  useEffect(() => {
    onClickRef.current = onClick;
  })
  useEffect(() => {
    window.addEventListener("click", () => {
      onClickRef.current();
    })
  })
}
```

1. onClick을 useRef에 저장한다. useRef에는 렌더링 결과와 무관한 값만 저장하자
2. useRef에 저장된 값이 변경돼도 컴포넌트가 다시 렌더링 되지 않기 때문 
3. useEffect 내에서 사용된 useRef 값은 의존성 배열에 추가할 필요 x

useRef 값을 useEffect 함수에서 변경하는 이유
> ```jsx
> function MyComponent({ onClick }) {
  > const onClickRef = useRef();
  > onClickRef.current = onClick;
  > }
> ```
> 
> 이와 같이 하는 이유는 나중에 도입될 React의 concurrent 모드 때문이다
> concurrent 모드에서는 함수가 실행됐다고 하더라도 중간에 렌더링이 취소될 수 있다.
> 렌더링은 취소가 되었는데 useRef 값에는 잘못된 값이 저장될 수 있으므로 컴포넌트 함수에서 직접 useRef의 값을 수정하면 안된다.


### 렌더링 속도를 올리기 위한 성능 최적화 방법

리액트가 실행될 때 가장 많은 CPU 리소스를 사용하는 것은 렌더링이다.
리액트는 UI 라이브러리이기 때문에 프로그램이 실행되는 동안에 화면을 그리고 또 그린다.
리액트는 데이터와 컴포넌트 함수로 화면을 그린다. 그 과정에서 대부분의 연산은 컴포넌트 함수의 실행과 가상 돔에서 발생한다.

리액트에서는 데이터 변경시 렌더링을 하는데 다음과 같은 단계를 거친다
1. 이전 렌더링 결과를 재사용할지 판단한다. (속성값이나 상탯값의 이전 이후 값을 비교한다. (React.memo))
2. 컴포넌트 함수를 호출한다.
3. 가상 돔끼리 비교해서 변경된 부분만 실제 돔에 반영한다.

* React.memo로 렌더링 결과 재사용하기

컴포넌트를 React.memo로 감싸게 되면 내부의 props가 변경되었는지 판별하고 변경되었을 때만 렌더링을 하게 된다.

React.memo 함수의 사용 예
```jsx
function MyComponent(props) {

}
function isEqual(prevProps, nextProps) {
  // true 또는 false를 반환
}
React.memo(MyComponent, isEqual)
```

속성값을 불변객체로 관리해야 렌더링 시에 더 빨라진다.
수정 가능한 객체로 선언했다면 brute force 밖에 방법이 없다. 이러면 렌더링이 오래걸린다.

리액트에서 속성값의 변경 여부를 계산하는 알고리즘
> 리액트에서 React.memo 의 두번째 인자로 값을 넘기지 않으면 리액트에서 기본으로 제공하는 함수가 사용된다.
> 
> 불변 객체라면 참조값만 비교해서 값의 변경 유무를 알 수 있다.
> `prevObj === nextObj`
> 
> 리액트는 속성값의 변경여부를 판단하기 위해 속성값에 직접 연결된 모든 속성을 비교한다.
> `prevProps.prop1 === nextProps.prop1 && prevProps.prop2 === nextProps.prop2`
> 이렇게 하는 이유는 jsx문법이 createElement로 변환된 코드를 보면 이해할 수 있다.
> ```jsx
> function Parent() {
>   return <Child name="mike" age={23} />
> }
> function Parent() {
>   return React.createElement(Child,{ name: 'mike', age: 23})
> }
> ```
> 렌더링 할때마다 새로운 속성값 객체가 생성된다.
> 객체의 내부 속성값은 변경되지 않더라도 최상위 객체의 참조값은 항상 변하게 된다.
> 따라서 리액트는 최상위 객체에 직접 연결된 모든 값을 단순 비교한다.

* 속성값과 상탯값을 불변 변수로 관리하는 방법

렌더링을 할 때마다 새로운 함수를 만들어서 자식 컴포넌트의 속성값으로 전달
```jsx
function Parent() {
  const [selectedFruit, setSelectedFruit] = useState('apple');
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>increase count</button>
      <SelectFruit
        selected={selectedFruit}
        onChange={fruit => setSelectedFruit(fruit)}
      />
    </div>
  )
}
```

1. 버튼을 클릭할 때마다 SelectFruit 컴포넌트 함수도 호출된다.
2. SelectFruit 컴포넌트로 전달되는 onChange 속성값이 변하기 때문이다. 
3. onChange 속성값은 부모 컴포넌트가 렌더링될때마다 새로운 함수로 만들어지고 있다.

useState, useReducer의 상탯값 변경함수는 변하지 않는다는 점을 이용하면 이 문제를 쉽게 해결할 수 있다.

useState의 상탯값 변경 함수를 입력해서 속성값을 고정
```jsx
function Parent() {
  const [selectedFruit, setSelectedFruit] = useState('apple');
  <SelectFruit 
    selected={selectedFruit}
    onChange={setSelectedFruit}
  />
}
```

useCallback을 이용해서 속성값을 고정
```jsx
function Parent(){
  const onChangeFruit = useCallback(fruit => {
    setSelectedFruit(fruit);
    sendLog({ type: 'fruit change', value: fruit });
  }, []); 

  <SelectFruit 
    selected={selectedFruit}
    onChange={onChangeFruit}
  />
}
```
1. 의존성 배열로 빈 배열을 입력했으므로 이 함수는 항상 고정된 값을 가진다.

* 객체의 값이 변하지 않도록 관리하기

함수와 마찬가지로 컴포넌트 내부에서 객체를 정의해서 자식 컴포넌트의 속성 값으로 입력하면, 자식 컴포넌트는 객체의 내용이 변경되지 않았는데도 속성값이 변경된다고 인식한다 => 렌더링 되어버림

렌더링을 할 때마다 새로운 객체를 만들어서 자식 컴포넌트의 속성값으로 전달
```jsx
function SelectFruit({ selectedFruit, onChange }) {
  return (
    <div>
      <Select 
        options={[
          {name: 'apple', price: 500},
          {name: 'banana', price: 1000},
          {name: 'orange', price: 1500},
        ]}
        selected={selectedFruit}
        onChange={onChange}
      />
    </div>
  )
}
```

1. SelectFruit 컴포넌트가 렌더링 될때마다 options 속성값으로 새로운 객체가 입력된다.

변하지 않는 값은 상수 변수로 관리하기
```jsx
function SelectFruit({ selectedFruit, onChange }) {
  return (
    <div>
      <Select 
        options={FRUITS}
        selected={selectedFruit}
        onChange={onChange}
      />
    </div>
  )
}

const FRUITS = [
  {name: 'apple', price: 500},
  {name: 'banana', price: 1000},
  {name: 'orange', price: 1500},
]
```

상탯값을 이용해서 속성값을 계산
```jsx
function SelectFruit({ selectedFruit, onChange }) {
  const [maxPrice, setMaxPrice] = useState(1000);

  return (
    <div>
      <Select 
        options={FRUITS.filter(item => item.price <= maxPrice)}
        selected={selectedFruit}
        onChange={onChange}
      />
    </div>
  )
}

const FRUITS = [
  {name: 'apple', price: 500},
  {name: 'banana', price: 1000},
  {name: 'orange', price: 1500},
]
```

useMemo훅을 이용하여 속성값을 계산
```jsx
function SelectFruit({ selectedFruit, onChange }) {
  const fruits = useMemo(() => FRUITS.filter(item => item.price <= maxPrice), [maxPrice])
};
return (
  <div>
    <Select options={fruits} selected={selectedFruit} onChange={onChange} />
  </div>
)
```

* 가상 돔에서의 성능 최적화

가상 돔이 만들어지고 실제 돔에 반영되는 과정에서 성능을 최적화할 수 있는 부분은 무엇인지 알아보자!!!!!

1. 요소의 타입 또는 속성을 변경하는 경우
```jsx
function App() {
  const [flag, setFlag] = useState(true);
  useEffect(() => {
    setTimeout(() => setFlag(prev => !prev), 1000);
  });
  if(flag) {
    return (
      <div>
        <Counter />
        <p>사과</p>
        <p>바나나</p>
      </div>
    )
  } else {
    return (
      <span>
        <Counter />
        <p>사과</p>
        <p>바나나</p>
      </span>
    )
  }
}

function Counter() {
  const [count, setCount] = useState(0);
  useEffet(() => {
    setTimeout(() => setCount(prev => prev + 1), 1000);
  });
  return <p>{count}</p>
}
```
=> 부모요소의 타입이 바뀌면 아래 자식컴포넌트 들은 삭제후에 다시 추가되므로 상탯값은 초기화 된다.

요소의 속성값을 변경하는 경우
```jsx
function App(){
  return (
    <div
      className={flag ? 'yes' : 'no'}
      style={{ color: 'black', backgroundColor: flag ? 'green' : 'red' }}
    >
      <Counter />
      <p>사과</p>
      <p>바나나</p>
    </div>
  )
}
```
=> 요소의 속성값만 변경하면 해당 속성만 실제 돔에 반영됨!
=> style 속성은 변경된 부분만 실제 돔에 반영된다. (backgroundColor만 반영된단 이야기)

요소를 추가하거나 삭제하는 경우
```jsx
function App() {
  if (flag) {
    return (
      <div>
        <p>사과</p>
        <p>바나나</p>
      </div>
    )
  } else {
    return (
      <div>
        <p>사과</p>
        <p>바나나</p>
        <p>파인애플</p>
      </div>
    )
  }
}
```
=> 1초 마다 파인애플이 추가되었다가 사라짐, 리액트는 가상 돔 비교를 통해 앞의 두 요소가 변경되지 않았다는 것을 안다.
=> 실제 돔에는 파인애플 만 추가하거나 삭제한다.

1초마다 중간에 요소를 추가하고 삭제
```jsx
function App(){
  if (flag) {
    return (
      <div>
        <p>사과</p>
        <p>바나나</p>
      </div>
    )
  } else {
    return (
      <div>
        <p>사과</p>
        <p>파인애플</p>
        <p>바나나</p>
      </div>
    )
  }
}
```
=> 중간에 요소를 추가하면 리액트는 그 뒤에 요소가 변경되지 않았다는 것을 알지 못한다.
=> 바나나가 변경되지 않았다는 것을 알기 위해 모든 값을 비교해야함 (연산량이 늘어남)
=> 리액트는 효율적으로 연산하기 위해 순서 정보를 이용한다.

key 속성값을 입력하는 경우
```jsx
function App(){
  if (flag) {
    return (
      <div>
        <p key="apple">사과</p>
        <p key="banana">바나나</p>
      </div>
    )
  } else {
    return (
      <div>
        <p key="apple">사과</p>
        <p key="pineapple">파인애플</p>
        <p key="banana">바나나</p>
      </div>
    )
  }
}
```
=> key 속성값을 입력하면 같은 키를 가지는 요소끼리만 비교해서 변경점을 찾는다.
=> pineapple 키가 새로 입력됐으므로 실제 돔에는 파인애플 요소만 추가한다.

**순서값을 키로 입력하는 경우 비효율적으로 렌더링 할수 있다**

key 속성값으로 배열의 순서 정보를 입력
```jsx
function App() {
  const fruits = flag ? FRUITS_1 : FRUITS_2;
  return (
    <div>
      {fruits.map((item, index) => {
        <p key={index}>{item}</p>
      })}
    </div>
  )
}

const FRUITS_1 = ['사과', '바나나'];
const FRUITS_2 = ['사과', '파인애플', '바나나'];
```
위의 경우 사과 빼고 전부 렌더링이 새로 된다. 바나나의 값이 변한것은 아니지만 순서 인덱스가 바뀌었기 때문에
렌더링 된다. => 비효율적 렌더링

배열 중간에 원소를 추가하거나 삭제할 경우 key 속성값으로 순서 정보를 입력하는것은 좋지 않다.


* 돔에서 부모요소 타입 바꾸면 자식요소들 전부 삭제되고 추가된다(자식 요소들의 상탯값은 초기화 된다.)
* 부모요소의 속성을 바꾸면 바뀐 속성만 실제 돔에 반영된다.
* key값을 이용 변경된 것만 효율적으로 렌더링 할수 있게 해야한다