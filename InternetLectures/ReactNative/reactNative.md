# 리액트 네이티브가 동작하는 법
 
React Native는 돔을 조작하는게 아니라 java, swift로 된 언어로 번역해준다.   
bridge라는 것이 있어 이것을 가능하게 해준다.(안드로이드와 ios에게 전달해주는 역할)

우리가 코드를 작성해주는 부분은 오로지 react 작성하는 부분  

1. ios와 안드로이드에서는 event를 감지한다.
2. 이 event를 bridge를 통해 자바스크립트에게 전송하고
3. 자바스크립트에서 실행 결과를 브릿지를 통해 다시 네이티브 쪽의 운영체제로 전달


react-native 는 html을 생산하는것이 아니다   
div -> View   
p -> Text   


`<View style={styles.container}></View>` => border같은 일부 속성은 style에서 사용할수가 없다


react native내의 api 사용하면 기능들 많음  
expo 자체적으로 제공하는 sdk가 있으므로 이걸 사용하면 개발에 편의성이 증가한다.  
expo sdk는 react native를 복제해서 작업 되는 것  


모든 `<View />` 는 flexbox 이다. flex-direction 기본 값은 Col   
웹 에서는 우리가 `<div style="display: flex; flex-direction:row;"></div>` 이런식으로 해줬었음

```js
export default function App() {
  return (
    <View style={{ flex: 1, flexDirection: "row" }}>
      <View style={{ flex: 1, backgroundColor: "red" }}></View>
      <View style={{ flex: 1, backgroundColor: "blue" }}></View>
      <View style={{ flex: 1, backgroundColor: "green" }}></View>
    </View>
  );
}
```


asyncStirage => 디바이스 내부에 저장하기 위해 사용하는 api