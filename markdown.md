마크다운 사용법
===========

<hr>

## 마크다운이란
일반 텍스트 기반의 경량 마크업 언어이다.<br>
markdown은 html로 변환이 가능하다.<br>
마크업 언어에 비해 문법이 쉽고 간단하다.<br>
응용 소프트웨어와 함께 배포되는 Readme 파일이나 온라인 게시물 등에 많이 쓰인다.

## 마크다운 문법

#### 문서 제목
```
Document Title
==============
```

Document Title
==============

#### 문서 소제목

```
Document Subtitle
-----------------
```
Document Subtitle
-----------------

#### 줄 바꿈

마크다운에서 엔터키 한번은 먹지 않는다.  
띄어쓰기 두번을 해야지 먹는다  

#### 헤더 적용  
h6 까지 적용
```
# H1
## H2
### H3
#### H4
##### H5
###### H6
```

# H1
## H2
### H3
#### H4
##### H5
###### H6


#### 인용문

```
> 인용문
>   > 인용문
>   >   > 인용문
```

> 인용문
>   > 인용문
>   >   > 인용문


#### 서체

```
// 이탤릭체
*이탤릭체*, _이탤릭체_
// 볼드체
**볼드체**, __볼드체__
```

*이탤릭체*, _이탤릭체_  

**볼드체**, __볼드체__  

#### 순서 있는 리스트

```
1. 첫번째
2. 두번째
3. 세번째
```

1. 첫번째
2. 두번째
3. 세번째  

```
1. 첫번째
1. 두번째
1. 세번째
```
1. 첫번째
1. 두번째
1. 세번째  

#### 순서 없는 리스트

```
- 첫 번째
- 두 번째
- 세 번째
```

- 첫 번째
- 두 번째
- 세 번째  

```
* 1
  * 2
    * 3

+ 1
  + 2
    + 3

- 1
  -2
    -3
```

* 1
  * 2
    * 3

+ 1
  + 2
    + 3

- 1
  - 2
    - 3

```
혼합해서 사용도 가능 

+ 1
  * 2
    - 3
      + 4
```

+ 1
  * 2
    - 3
      + 4
      

#### 코드 블럭 사용

```
  '''java
  
  public class ~~~~
  
  '''  
```

#### 링크

* 참조링크
```
[link Keyword](id)
[id]: URL "Title"

Link: [Google](googlelink)
[googlelink]: https://google.com "Go google"
```

* 외부링크
```
[Google](https://google.com)
```
Link: [Google](https://google.com)


* 자동연결
```
일반적인 이메일 링크의 경우 자동으로 연결시켜 준다.
* 이메일링크: <example@example.com>
```
이메일링크: <example@example.com>


#### 위 첨자
```
  <sup>[[3]](#출처)</sup>
```
클릭<sup>[[3]](#출처)</sup>

#### 아래 첨자

```
  <sub>[[3]](#출처)</sub>
```
클릭<sub>[[3]](#출처)</sub>

#### 강조

```
*single asterisks*
**double asterisks**
_single underscore_
__double underscore__
~~cancel line~~
```
*single asterisks*  
**double asterisks**  
_single underscore_  
__double underscore__   
~~cancel line~~   

#### 테이블

```
|제목|내용|
|-|-|
|Title 1| Description 1|
|Title 2| Description 2|
|Title 3| Description 3|
|Title 4| Description 4|
```

|제목|내용|
|-|-|
|Title 1| Description 1|
|Title 2| Description 2|
|Title 3| Description 3|
|Title 4| Description 4|


#### 이미지
```
<img src="example.com" style="width: 50%; height: 50%">
```
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/600px-Markdown-mark.svg.png" style="width: 50%; height: 50%">

<hr>

#### 출처

<https://gist.github.com/ihoneymon/652be052a0727ad59601>
<https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4>