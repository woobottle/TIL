# 9. 정적 타입 그리고 타입스크립트

자바스크립트는 동적 타입 언어다. 따라서 변수의 타입은 런타임에 결정된다. 이와 반대인 정적 타입언어도 존재한다. 정적타입 언어는 변수의 타입이 컴파일 타임에 결정된다.

동적 타입 언어: 자바스크립트, 파이썬, php   
정적 타입 언어: ja필a, c++   

### 9.1 타입스크립트
타입스크립트는 자바스크립트의 모든 기능을 포함하면서 정적 타입을 지원하는 superset이다.   

##### 9.1.1 동적 타입 언어와 정적 타입 언어

동적 타입 언어
* 타입에 대한 고민을 하지 않아도 되므로 배우기 쉽다
* 코드의 양이 적을 때 생산성이 높다
* 타입 오류가 런타임 시 발견된다

정적 타입 언어
* 변수를 선언할 때마다 타입을 고민해야 하므로 진입 장벽이 높다
* 코드의 양이 많을 때 동적 타입 언어에 비해 생산성이 높다
* 타입 오류가 컴파일 시 발견된다.

**정적 타입 언어가 생산성이 높은 이유**
정적 타입 언어의 코드는 타입으로 서로 연결되어 있다. 덕분에 연관된 코드 간의 이동이 수비고, 변수명이나 함수명을 변경하는 등의 리팩터링도 쉽다.   
단축키 한 번 이면 IDE가 필요한 임포트 코드르 자동으로 넣어 준다.

* 타입 추론(자동으로 타입을 인식하는 기능) 덕분에 기존의 자바스크립트 코드를 크게 변경하지 않아도 타입스크립트를 비교적 쉽게 적용할 수 있다.

```ts
let v1 = 123;
v1 = 'abc'; // typeerror
```

```ts
let v1: number | string = 123;
v1 = 'abc';
```


### 9.2 타입스크립트의 여러 가지 타입
##### 9.2.1 타입스크립트의 다양한 타입

```ts
const size: number = 123;
const isBig: boolean = size >= 100;
const msg: string = isBig ? '크다' : '작다';

const values: number[] = [1,2,3];
const values2: Array<number> = [1,2,3];
values.push('a'); // 타입에러

const data: [string, number] = [msg, size];
data[0].substr(1);
data[1].substr(1); // 타입 에러
```

* null과 undefined 타입
```ts
let v1: undefined = undefined;
let v2: null = null;
v1 = 123 // 타입 에러

let v3: number | undefined = undefined;
v3 = 123;
```

ts에서는 undefined와 null은 타입으로 사용될 수 있다.

* 문자열 리터럴과 숫자 리터럴 타입
```ts
let v1: 10 | 20 | 30;
v1 = 10;
v1 = 15; // 타입 에러

let v2: '경찰관' | '소방관';
v2 = '의사'; // 타입 에러
```

* void와 never 타입
```ts
function f1(): void {
  console.log('hello')
}
function f2(): never {
  throw new Error('some error');
}
function f3(): never {
  while (true) {
    // ...
  }
}
```

* object 타입
```ts
let v: object;
v = { name: 'abc' };
console.log(v.prop1) // 타입 에러
```

=> 객체의 속성에 대한 정보가 없기 때문에 특정 속성값에 접근하면 타입 에러가 발생한다.

* 교차 타입과 유니온 타입
=> 여러 타입의 교집합과 합집합을 각각 교차(intersection) 타입과 유니온(union) 타입으로 표현할 수 있다.    
교차 타입 &      
유니온 타입 |    

```ts
let v1: (1 | 3 | 5) & ( 3 | 5 | 7) // 3밖에 안된다
v1 = 3;
v1 = 1; // 타입 에러
```


* type 키워드로 타입에 별칭 주기
```ts
type Width = number | string;
let width: Width;
width = 100;
width = '100px';
```

##### 9.2.2 열거형 타입

```ts
enum Fruit {
  Apple, 
  Banana,
  Orange,
}
const v1: Fruit = Fruit.Apple;
const v2: Fruit.Apple | Fruit.Banana = Fruit.Banana;
```

```ts
enum Fruit {
  Apple, // 자동으로 0이 할당된다.
  Banana = 5,
  Orange,
}
console.log(Fruit.Apple, Fruit.Banana, Fruit.Orange) // 0, 5, 6
```

열거형 타입이 컴파일 된 결과
```ts
var Fruit;
(function(Fruit) {
  Fruit[Fruit['Apple'] = 0] = 'Apple';
  Fruit[Fruit['Banana'] = 5] = 'Banana';
  Fruit[Fruit['Orange'] = 6] = 'Orange';
})(Fruit || Fruit = {}));
console.log(Fruit.Apple, Fruit.Banana, Fruit.Orange) // 0, 5, 6
```

* 열거형 타입을 위한 유틸리티 함수

열거형 타입의 원소 개수를 알려 주는 함수
```ts
function getEnumLength(enumObject: any) {
  const keys = Object.keys(enumObject);
  // enum의 값이 숫자이면 두 개씩 들어가므로 문자열만 계산한다.
  return keys.reduce(
    (acc, key) => (typeof enumObject[key] === 'string' ? acc + 1 : acc),
    0,
  );
}
```

열거형 타입에 존재하는 값인지 검사하는 함수
```ts
function isValidEnumValue(enumObject: any, value: number | string) {
  if (typeof value === 'number') {
    return !!enumObject[value];
  } else {
    return (
      Object.keys(enumObject)
        .filter(key => isNaN(Number(key)))
        .some(key => enumObject[key] === value)
    )
  }
}
```

* 상수 열거형 타입

열거형 타입은 컴파일 후에도 남아 있기 때문에 번들 파일의 크기가 불필요하게 커질 수 있다.   
열거형 타입의 객체에 접근하지 않는다면 굳이 컴파일 후에 객체로 남겨 놓을 필요는 없다.   
상수 열거형 타입을 사용하면 컴파일 결과에 열거형 타입의 객체를 남겨 놓지 않을 수 있다.    

```ts
const enum Fruit {
  Apple,
  Banana,
  Orange,
}
const fruit: Fruit = Fruit.Apple;


const enum Language {
  Korean = 'ko',
  English = 'en',
  Japanese = 'jp',
}
const lang: Language = Language.Korean;
```

상수 열거형 타입이 컴파일된 결과
```ts
const fruit = 0;
const lang = 'ko';
```


##### 9.2.3 함수 타입
```ts
function getInfoText(name: string, age: number): string {
  const nameText = name.substr(0, 10);
  const ageText = age >= 35 ? 'senior' : 'junior';
  return `${nameText} ${ageText}`
}

const v1: string = getInfoText('mike', 23);
```

```ts
function getInfoText(name: string, gender?: string, age: number) { // 다음과 같은 식으로 중간에 선택 매개변수 선언해버리면 에러 발생

}
```


매개변수에 기본값 정의하기
```ts
function getInfoText{
  name: string,
  age: number = 15,
  language = 'koream',
} : string{

}
```

나머지 매개변수
```ts
function getInfoText(name: string, ...rest: string[]): string {

}
```


* this 타입
```ts
function getParam(index: number): string {
  const params = this.splt(','); // 에러가 안남
  if (index < 0 || params.length <= index) {
    return '';
  }
  return this.split(',')[index];
}
```

```ts
function getParam(this: string, index: number): string {
  const params = this.splt(','); // 타입에러
}
```

* 함수 오버로드
```ts
function add(x: number | string, y: number | string): number;
function add(x: number | string, y: number | string): string;
function add(x: number | string, y: number | string): number | string {
  if (typeof x === "number" && typeof y === "number") {
    return x + y;
  } else {
    const result = Number(x) + Number(y);
    return result.toString();
  }
}

const v1: number = add(1, 2); // 타입을 number | string으로 해주어야 함, 아니면 저런식으로 오버로드
console.log(add(1, "2"));
```

* 명명된 매개변수
```ts
interface Param {
  name: string;
  age?: number;
  language?: string;
}
function getInfoText({ name, age = 15, language }: Param) : string }

```

### 9.3 인터페이스

* 읽기 전용 속성
```ts
interface Person {
  readonly name: string;
  age?: number;
}
const p1: Person {
  name: 'mike',
}
p1.name = 'james' // 컴파일 에러
```

##### 9.3.2 인터페이스로 정의하는 인덱스 타입

* 인덱스 타입의 예
```ts
interface Person {
  readonly name: string;
  age?: number;
  [key: string]: string | number;
}
const p1: Person {
  name: 'mike',
  age: 25,
  birthday: '1997-01-01',
}
```

##### 9.3.3 그 밖에 인터페이스로 할 수 있는 것
* 인터페이스로 함수 타입 정의하기
```ts
interface GetInfoText {
  (name: string, age: number): string;
}
const getInfoText: GetInfoText = function(name, age) {
  const nameText = name.substr(0, 10);
  const ageText = age >= 35 ? 'senior' : 'junior';
  return `${nameText}${ageText}`
}
```

* 인터페이스로 클래스 구현하기
```ts
interface Person {
  name: string;
  age: number;
  isYoungerThan(age: number): boolean;
}

class SomePerson implements Person {
  name: string;
  age: number;
  constructor(name: string, age: string) {
    this.name = name;
    this.age = age;
  }
  isYoungerThan(age: number) {
    return this.age < age;
  }
}
```

* 인터페이스 확장하기
```ts
interface Person {
  name: string;
  age: number;
}
interface Programmer {
  favoriteProgrammingLanguage: string;
}

interface Korean extends Person, Programmer {
  isLiveInSeoul: boolean;
}
```

* 인터페이스 합치기
```ts
interface Person {
  name: string;
  age: number;
}
interface Product { 
  name: string;
  price: number;
}
type PP = Person & Product;
const pp: PP = {
  name: 'a',
  age: 23,
  price: 1000,
}
```
### 타입스크립트 고급 기능

##### 9.5.1 제네릭

리팩터링이 필요한 코드
```ts
function makeNumberArray(defaultValue: number, size: number): number[] {
  const arr: number[] = [];
  for (let i = 0; i < size; i++) {
    arr.push(defaultValue);
  }
  return arr;
}
function makeStringArray(defaultValue: string, size: number): string[] {
  const arr: string[] = [];
  for (let i = 0; i < size; i++) {
    arr.push(defaultValue);
  }
  return arr;
}
const arr1 = makeNumberArray(1, 10);
const arr2 = makeStringArray('1', 10);
```

* 제네릭으로 문제 해결하기
```ts
function makeArray<T>(defaultValue: T, size: number): T[] {
  const arr: T[] = [];
  for (let i = 0; i < size; i++) {
    arr.push(defaultValue);
  }
  return arr;
}
const arr1 = makeArray<number>(1,10)
const arr2 = makeArray<string>('empty', 10)
const arr3 = makeArray(1,10) // 첫번째 매개변수의 타입이 타입 T가 되기 때문에 명시하지 않아도 된다.
const arr4 = makeArray('a', 10) // 첫번째 매개변수의 타입이 타입 T가 되기 때문에 명시하지 않아도 된다.
```

* 제네릭으로 스택 구현하기
```ts
class Stack<D> {
  private items: D[] = [];
  push(item: D) {
    this.items.push(item);
  }
  pop() {
    return this.items.pop();
  }
}

const numberStack = new Stack<number>();
numberStack.push(10);
const v1 = numberStack.pop();
```

* extends 키워드로 제네릭 타입 제한하기
```ts
function identity<T extends number | string>(p1: T): T { // extends 키워드로 제네릭의 타입을 제한
  return p1
}
identity(1);
identity('a');
identity([]) // 에러 발생
```

##### 9.5.2 맵드 타입
맵드 타입은 기존 인터페이스의 모든 속성을 선택 속성 또는 읽기 전용으로 만들 때 주로 사용한다
```ts
interface Person {
  name: string;
  age: number;
}
interface PersonOptional {
  name?: string;
  age?: number;
}
interface PersonReadOnly {
  readonly name: string;
  readonly age: number;
}
```

맵드 타입은 in 키워드를 사용해서 정의한다.
```ts
type T1 = { [K in 'prop1' | 'prop2']: boolean };
// { prop1: boolean; prop2: boolean; }
```

인터페이스의 모든 속성을 불 타입 및 선택 속성으로 만들어주는 맵드 타입
```ts
type MakeBoolean<T> = { [P in keyOf T]?: boolean }
const pMap: MakeBoolean<Person> = {};
pMap.name = true;
pMap.age = false;
```

* Partial과 Readonly 내장 타입
```ts
type T1 = Person['name'];
type Readonly<T> = { readonly [P in keyof T]: T[P] };
type Partial<T> = { [P in keyof T]?: T[P] };
type T2 = Partial<Person>;
type T3 = Readonly<Person>;
```

* Pick 내장 타입

```ts
type Pick<T, K extends keyof T> = { [P in K]: T[P] };
interface Person {
  name: string;
  age: number;
  language: string;
}
type T1 = Pick<Person, 'name' | 'language'>;
```

* Record 내장 타입

입력된 모든 속성을 같은 타입으로 만들어주는 맵드 타입
```ts
type Record<K extends string, T> = { [P in K]: T};
type T1 = Record<'p1' | 'p2', Person>;
```


##### 9.5.3 조건부 타입
```ts
type IsStringType<T> = T extends string ? 'yes' : 'no';
type T1 = IsStringType<string>; // 'yes'
type T2 = IsStringType<number>; // 'no'
```

* Exclude, Extract 내장 타입

```ts
type T1 = number | string | never;
type Exclude<T, U> = T extends U ? never : T;
type T2 = Exclude<1 | 3 | 5 | 7, 1 | 5 | 9> // 3, 7
type T3 = Exclude<stirng | number | (() => void), Function> // string | number
type Extract<T, U> = T extends U ? T : never;
type T4 = Extract<1 | 3 | 5 | 7, 1 | 5 | 9> // 1, 5
```


### 9.6 생산성을 높이는 타입스크립트의 기능

const 변수의 타입 추론
```ts
const v1 = 123;
const v2 = '1'
let v3: typeof v1 | typeof v2;
```

##### 9.6.2 타입 가드

타입 가드를 활용하지 않은 코드
타입 가드가 없다면 `as` 키워드를 사용해서 타입 단언을 해야한다
```ts
function print(value: number | string) {
  if (typeof value === 'number') {
    console.log((value as number).toFixed(2));
  } else {
    console.log((value as string).trim());
  }
}
```

* typeof 키워드

타입 가드를 활용한 코드
```ts
function print(value: number | string) {
  if (typeof value === 'number') {
    console.log(value.toFixed(2));
  } else {
    console.log(value.trim());
  }
}
```

* instanceof 키워드

클래스의 경우 타입가드 사용하는 방법
인터페이스의 경우에는 적용 불가

```ts
class Person {
  name: string;
  age: number;
  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}

class Product {
  name: string;
  price: number;
  constructor(name: string, price: number) {
    this.name = name;
    this.price = price;
  }
}

function print(value: Person | Product) {
  console.log(value.name)
  if (value instanceof Person) {
    console.log(value.age)
  } else {
    console.log(value.price)
  }
}
```


* 식별 가능한 유니온 타입

인터페이스를 구별하기 위해서는 인터페이스간 동일한 키값을 가지게 하고 그것으로 비교하는 것이다(유니온 타입)

```ts
interface Person {
  type: 'person';
  name: string;
  age: number;
}

interface Product {
  type: 'product';
  name: string;
  price: number;
}

function print(value: Person | Product) {
  if (value.type === 'person') {
    console.log(value.age);
  } else {
    console.log(value.price)
  }
}
```


### 9.7 타입스크립트 환경 구축하기

리액트
`npx create-react-app my-cra --template typescript`

넥스트
`touch tsconfig.json` 하고 `npx next`


```shell
npm install typescript react react-dom
npm install @types/react @types/react-dom
npx tsc --init # tsconfig.json 바로 생성해줌
```

타입 스크립트에서 자바스크립트 파일 사용하기

tsconfig.json 파일에 `allowJs: true` 해주기

* window 객체의 타입 정의하기

```ts
import Icon from './icon.png'
window.myValue = 123; // 타입에러

export default functon({ name, age }: { name: string; age: number}) {
  //...
  return (
    <div>
      <img src={Icon}> // 에러 발생
    </div>
  )
}
```

src 폴더 밑에 types.ts 파일 만들고 아래와 같이 입력

```ts
interface Window {
  myValue: number;
}

declare module '*.png' {
  const content: string;
  export default content;
}
```

window 객체에 myValue 추가하고 타입스크립트에 png 확장자를 가지는 모듈의 타입이 문자열이라고 알려준다.

* 자바스크립트 최신 문법 사용하기

tsconfig.json에 추가  
```ts
{
  "compilerOptions": {
    "lib": ["dom", "es5", "scripthost", "es2017"] // 기본값은 dom, es5, scripthost
  }
}
```

폴리필은 직접 추가해야 한다.


### 9.8 리액트에 타입 적용하기

##### 9.8.1 리액트 컴포넌트에서 타입 정의하기

이벤트 객체와 이벤트 처리 함수의 타입
```ts
import React from 'react';
type EventObject<T = HTMLElement> = React.SyntheticEvent<T>;
type EventFunc<T = HTMLElement> = (e: EventObject<T>) => void;
```

함수형 컴포넌트의 타입 정의하기
```ts
import React from 'react';

interface Props {
  name: string;
  age?: number;
}

export default function MyComponent({ name, age = 23 }: Props) {
  return (
    <div>
      <p>{name}</p>
      <p>{age}</p>
    </div>
  );
};

const MyComponent: React.FunctionComponent<Props> = function ({ name, age = 23 }) {
  return (
    <div>
      <p>{name}</p>
      <p>{age}</p>
    </div>
  )
}
```