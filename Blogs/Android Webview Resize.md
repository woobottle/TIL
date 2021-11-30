# webview 화면 resizing 

웹뷰에서 키보드가 하단에서 올라오게 되면 위의 화면은 키보드로 가려져서 화면이 줄어듭니다.   
이때 화면을 스크롤 하거나 줄이거나, 줄여지지 않는 방법을 알아보겠습니다.  

```java
// AndroidManifest.xml
<activity
  android:name="kr.co.bus.app.MainActivity"
  android:configChanges="keyboard|keyboardHidden|screenLayout|screenSize|orientation"
  android:windowSoftInputMode="adjustResize"
  android:screenOrientation="portrait"
  android:theme="@style/WebviewTheme"
  >
  <intent-filter>
      <action android:name="android.intent.action.MAIN" />
      <category android:name="android.intent.category.LAUNCHER" />
  </intent-filter>
</activity>
```

windowSoftInputMode에서 옵션을 주어서 제어할 수 있습니다.
stateOption과 adjustOption을 하나씩 사용하거나 둘중 하나만 사용합니다.   
두 그룹중 어느 하나의 그룹을 복수개 사용하면 정의되지 않은 결과를 가져올 수 있습니다.   

example

사용하는 알맞은 예시입니다

```java
android:windowSoftInputMode="adjustResize|stateVisible"
```

아래의 코드는 정의되지 않은 결과를 가져올 수 있습니다

```java
android:windowSoftInputMode="adjustResize|adjustPan"
```

아래 이미지는 기본 상태 화면입니다  

<img src="https://user-images.githubusercontent.com/72545732/143866209-4f160d17-84c3-4a05-82d9-9d7aee4465a8.png" width="30%" height="50%">


우리가 필요한 기능을 적용한 예시부터 바로 살펴보겠습니다.

### adjustResize

<img src="https://user-images.githubusercontent.com/72545732/143866259-660f1c61-8e92-4710-b010-b827f8fecdc1.png" width="30%" height="50%">

`android:windowSoftInputMode="adjustResize"`를 적용한 화면입니다.   
상단의 화면은 스크롤이 가능하고 하단에 존재하는 툴바가 키보드 위로 올라온 것을 확인할 수 있습니다.  
키보드 위로 기존의 웹뷰가 resizing 됩니다   

### adjustPan

<img src="https://user-images.githubusercontent.com/72545732/143866011-eaae2a7e-e75a-4685-8720-0cb027d44963.png" width="30%" height="50%">

`android:windowSoftInputMode="adjustPan"`를 적용한 화면입니다.   
상단의 화면은 스크롤이 가능하고 하단에 존재하는 툴바가 키보드 위로 올라오지 않은 것을 확인할 수 있습니다.  
키보드 위로 기존의 웹뷰가 resizing 되지 않습니다   
위 화면에서는 최하단의 툴바는 키보드로 인해 노출이 되지 않습니다.  

### adjustUnspecified

<img src="https://user-images.githubusercontent.com/72545732/143866060-3f1d067a-12eb-4be2-a54c-bfd4be8af01c.png" width="30%" height="50%">

`android:windowSoftInputMode="adjustUnspecified"`를 적용한 화면입니다.   
상단의 화면은 스크롤이 가능하고 하단에 존재하는 툴바가 키보드 위로 올라온 것을 확인할 수 있습니다.  
키보드 위로 기존의 웹뷰가 resizing 됩니다

adjustUnspecified는 시스템이 adjustPan|adjustResize중 자동으로 선택합니다. 해당 창의 콘텐츠가 스크롤 할 수 있는 레이아웃이라면 화면을 자동으로 resizing 해줍니다

> 어떻게 동작하는지 신기하네요


### stateOptions
제가 문서를 읽고 파악한 stateOptions 옵션은 액티비티간 전환시나 액티비티에 입력 포커스가 있는경우에 옵션을 주어서 제어하는 경우인것 으로 파악하였습니다.    
현재는 웹뷰만 작업, 따로 액티비티간 전환을 하거나 액티비티에 직접 인풋창을 생성하지 않고 있으므로 문서에 나온 개념만 나열하고 넘어가겠습니다.   

##### stateUnspecified
시스템이 적당한 상태를 선택하거나 테마 설정에 의존합니다

##### stateUnchanged
액티비티가 앞으로 나올때 키보드가 마지막으로 사용된 상태(숨김 또는 표시)를 유지합니다

##### stateHidden
다른 액티비티에서 해당 액티비티로 이동하는 경우 키보드가 숨겨집니다.

##### stateAlwaysHidden
액티비티의 기본 창에 입력포커스가 있는경우 항상 숨겨집니다

##### stateVisible
액티비티로 이동하는 경우 키보드가 표시됩니다.

##### stateAlwaysVisible
액티비티로 이동하는 경우 키보드가 표시됩니다.


출처 : https://developer.android.com/guide/topics/manifest/activity-element#wsoft