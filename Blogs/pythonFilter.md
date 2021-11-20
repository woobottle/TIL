## python에서 Filter

javascript에서 filter를 즐겨 쓰다보니 python에서도 filter를 계속 찾게된다.
아직 익숙치 않아 매번 블로그 뒤지고 있어서 이 참에 한번 깔끔하게 정리해보자

실제 활용 예시 먼저!!!

```python
import re

s = "one2three4five6"
print(list(re.split('(\d)', s))) # ['one', '2', 'three', '4', 'five', '6', '']

print(list(filter(lambda x: x != '', list(re.split('(\d)', s))))) # ['one', '2', 'three', '4', 'five', '6']
```

* 최근 정규 표현식 라이브러리를 사용하려 하고 있다.
* `re.split`을 하면 split 구문이기 때문에 경우에 따라 뒤에 ''가 들어온다. (split안의 내용은 구문중 숫자로 구문을 split한다는 거다)
* 이걸 해결하기 위해 filter를 사용한다.

python의 filter 

> filter(function, iterable)    
> Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
>
>Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None.
>
>See itertools.filterfalse() for the complementary function that returns elements of iterable for which function returns false.

앞에 Function이 들어온다. 그걸 lambda로 대신해주었다. (lambda는 아직 익숙치 않다....)

function을 사용한 예시를 살펴보자

```python
def func(x) :
  if x > 0 :
    return True
  else :
    return False

array = [-2, -1, 0, 1, 2]
print(list(filter(func, array))) # [1,2]
print(list(filter(lambda x: x > 0, array))) # [1,2]
```

코드에 두가지 예시를 넣어두었다. funcdtion을 넣은것과 lambda를 이용한 것


출처: <https://docs.python.org/3/library/ast.html#ast.literal_eval>