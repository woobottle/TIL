## ContextSwitching

이것이 필요한 이유는 여러개의 작업을 번갈아 가면서 실행시켜 사용자에게 여러 프로그램이 동시에 실행되는 것처럼 보이기 위함이다. 그에 따른 소모되는 비용과 진행 과정은 아래에 있다.   
cpu가 task를 바꿔가며 실행하기 위해 context switching이 필요하게 됨   

컴퓨터가 매번 하나의 task만 처리한다면
----
* task 하나가 실행되면 끝날때까지 기다려야 한다.
* 작업을 진행중이라면 응답을 처리하기까지 오래걸리거나 사용성이 현격히 떨어질 수 있다.

=> contextSwitch 탄생

**핵심: 빠른 속도로 task를 바꿔가며 실행해서 사용자에게 여러 작업이 동시에 실행되는 것처럼 보이게 할 수 있다.**

ContextSwitching 이란
-----
* 현재 진행하고 있는 Task(Procss, Thread)의 상태를 저장하고 다음 진행할 Task의 상태 값을 읽어 적용하는 과정

ContextSWitching 진행 과정
-----
* Task의 대부분 정보는 Register에 저장되고 PCB(Process Control Block)으로 관리되고 있다.
* 현재 실행하고 있는 Task의 PCB정보를 저장
* 다음에 실행할 Task의 PCB 정보를 읽어 Register에 적재하고 CPU가 이전에 진행하던 과정을 연속적으로 수행

Context Switching Cost
----
* Cache 초기화 (l1 cache, l2 cache, l3cache를 비워야 한다)
* Memory mapping 초기화

Process Vs Thread
-----
* process가 thread보다 비용이 더 많이듬 
* thread는 stack을 제외한 모든 메모리를 공유함(data, code, stack, heap 이중 stack만 공유)
* process는 전부 다 바꿔줘야 하지만 Thread는 스택만 갈아주면 된다.


##### PCB 구성요소
* Process State: 프로세스 상태(Create, Ready, Running, Waiting, Terminated)
* Process Counter: 다음 실행할 명령어의 주소값
* CPU Registers

##### Register??
* cpu(central processing unit)가 요청을 처리하는 데 필요한 데이터를 일시적으로 저장하는 기억장치.
* cpu와 직접 연결되어 있어서 속도가 빠르다
* 컴퓨터의 기억장치 구성   
  ![image](https://user-images.githubusercontent.com/50283326/135751076-46c44e2b-839e-4861-a1e0-7e18bdcfe47a.png)
  ![image](https://user-images.githubusercontent.com/50283326/135752274-fb86c5ed-5236-451f-9943-e106ed3cf31d.png)
* cpu에서는 직접 메모리에 접근할수 없다. 레지스터를 활용하여 접근해야 한다. 레지스터가 메모리에서 주솟값을 참조하여 값을 가져온다. 이 가져온 값들을 cpu의 누산기 레지스터에서 계산 하는 형식
* 레지스터에는 프로그램 카운터, 명령어 레지스터, 메모리 주소 레지스터, 메모리 버퍼 레지스터, 입출력 주소 레지스터, 입출력 버퍼 레지스터 등이 있다.
* 프로그램 카운터는 다음에 실행할 메모리의 주소가 들어있다. 
* 컴퓨터의 메모리에는 값도 있고 어셈블리 언어도 있는것 같다.
* 메모리에서 가져온 값이 값이면 값을 이용, 명령어면 해당 명령어를 실행하는 느낌인가?
* 최종결과는 메모리 버퍼 레지스터에 저장되고 이를 통해 메모리로 전송됩니다.
* 컴퓨터 에서는 `C=A+B` 를 컴파일러로 어셈블리 언어로 바꾸고 어셈블러를 통해 0101010으로 바꾼다
* `C=A+B` =>(컴파일러) load [10]; add [11]; store[12]; =>(어셈블러) 0101010100
* 메모리 주소 레지스터에서 주소참조 값을 읽어와서 메모리 버퍼 레지스터에 저장
* 메모리 버퍼 레지스터에 있는 값이 명령이면 명령어 레지스터로 아니면 누산기 레지스터로
* 프로세서의 구조를 아키텍처라 한다.
  

##### 32비트, 64비트
* 명령을 한번에 처리할 수 있는 레지스터의 비트 수
* 하나의 레지스터가 저장가능한 공간의 크기가 32비트인지 64비트 인지를 나타내는 것 (32비트는 4줄 64비트는 8줄)
* 접근할 수 있는 메모리의 범위가 기하급수적으로 커진다, 16비트(65535), 32비트 (4294967295)
* 16비트 시절 메모리 공간을 아끼기 위해서 모두 같은 메모리 공간에서 프로그램을 실행 시켜야 했고, 프로그램 간의 메모리 침범은 매우 빈번했다.
* ipv4에서 ipv6가 나온 개념

##### ipv4, ipv6
ipv4는 프로토콜의 주소가 32비트라는 제한된 공간에 있었고 사이트는 늘어가는데 32비트 주소 공간은 너무 부족했다    
그래서 ipv6 프로토콜 64비트로 주소를 표현할 수 있는 것이 나왔다.

<hr>

1. <https://nesoy.github.io/articles/2018-11/Context-Switching>
2. <http://itnovice1.blogspot.com/2019/08/blog-post_99.html>
3. <https://www.youtube.com/watch?v=Fg00LN30Ezg&t=998s>
4. <https://ko.wikipedia.org/wiki/IPv6>