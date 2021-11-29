# 가상 메모리

가상메모리도 중요하구나!!!

> 실제 각 프로세스마다 충분한 메모리를 할당하기에는 메모리 크기가 한계가 있음   

예: 리눅스는 하나의 프로세스가 4GB임   
멀티 프로세스 몇개 띄우면 메모리 터짐, 멀티 스레드로 실행하거나 해야함

> 폰 노이만 구조 기반이므로, 폰 노이만 구조의 핵심은 코드는 메모리에 반드시 있어야 한다


메모리 용량이 부족해지기 때문에 위 기술이 등장   

* 가상 메모리: 메모리가 실제 메모리보다 많아 보이게 하는 기술
  * 실제 사용하는 메모리는 작다는 점에 착안해서 고안된 기술
  * 프로세스간 공간 분리로, 프로세스 이슈가 전체 시스템에 영향을 주지 않을 수 있음

<img src="https://user-images.githubusercontent.com/72545732/143040986-2a08067e-988f-4a47-b8eb-cd5ef0870e8e.png">

자 그림을 보자 프로세스가 4기가 차지하는데 이것도 커널과 사용자 모드로 나뉘고 커널 모드중 일부만 메모리를 사용하고 있다.

<hr>

* 가상 메모리 기본 아이디어
  * 프로세스는 가상 주소를 사용하고, 실제 해당 주소에서 데이터를 읽고/쓸때만 물리 주소로 바꿔주면 된다.
  * virtual address(가상 주소): 프로세스가 참조하는 주소 (0~4gb 정도의 주소를 할당 일부만 실제 메모리 주소를 가리킴)
  * physical address(물리 주소): 실제 메모리 주소
* MMU(Memory Management Unit) (하드웨어)
  * cpu에 코드 실행시, 가상 주소 메모리 접근이 필요할 때, 해당 주소를 물리 주소값으로 변환해주는 하드웨어 장치

<hr>

* cpu는 가상 메모리를 다루고, 실제 해당 주소 접근시 MMU 하드웨어 장치를 통해 물리 메모리 접근
  * 하드웨어 장치를 이용해야 주소 변환이 빠르기 때문에 별도의 장치를 둠
<img src="https://user-images.githubusercontent.com/72545732/143042306-0a6a9360-350e-413c-a0e4-88dc8f22f864.png">

* 프로세스 생성시, 페이지 테이블 정보 생성
  * PCB등에서 해당 페이지 테이블 접근 가능하고, 관련 정보는 물리 메모리에 적재
  * 프로세스 구동시, 해당 페이지 테이블 base 주소가 별도 레지스터에 저장(CR3)
  * CPU가 가상 주소 접근시, MMU가 페이지 테이블 base 주소를 접근해서, 물리 주소를 가져옴

### 페이징 시스템
* 페이징개념
  * 크기가 동일한 페이지로 가상 주소 공간과 이에 매칭하는 물리 주소 공간을 관리
  * 하드웨어 지원이 필요
  * 리눅스에서는 4KB로 paging (4gb를 4kb로 다 쪼개고 번호를 붙여서 물리메모리에 넣고 빼고 하는거)
  * 페이지 번호를 기반으로 가상 주소/물리 주소 매핑 정보를 기록/사용

<img src="https://user-images.githubusercontent.com/72545732/143044883-100fffdc-ebec-4cd0-a9a6-fb5241100ae3.png">




가상 메모리

> 실제 각 프로세스마다 충분한 메모리 할당은 불가
ex: 리눅스는 하나의 프로세스가 4GB임
> 폰 노이만 구조 기반이므로, 코드는 메모리에 반드시 있어야함

한정된 메모리에서 어떻게 여러 프로세스를 운영해야 할까 에서 나온 개념

프로세스에서 실제 한 시점에 cpu가 사용하는 부분은 제한적이다.

<img width="697" alt="Pasted Graphic 16" src="https://user-images.githubusercontent.com/72545732/143769530-bc93e07f-fa1e-463e-aaad-4052d3f63922.png">


cpu가 프로세스의 주소에 접근할때 메모리에 올라가있는 주소를 cpu에게 알려주어서 동작이 가능하게끔 하자

<img src="https://user-images.githubusercontent.com/72545732/143769531-568a55f5-41ee-4a2c-8764-4410f293dbad.png">

<img width="997" alt="Virtual" src="https://user-images.githubusercontent.com/72545732/143769569-aa5ac853-05fb-4b05-b466-79e567f437ca.png">


페이징 시스템

페이징 
	•	크기가 동일한 페이지로 가상 주소 공간과 이에 매칭하는 물리 주소 공간을 관리
	•	리눅스에서는 4KB로 Paging(프로세스에 할당된 4Gb가 4kb로 분리된다고 보면 됨)
	•	페이지 번호를 기반으로 가상주소/물리주소 매핑정보를 사용

프로세스의 PCB에 Page Table 구조체를 가리키는 주소가 들어있음

<img width="832" alt="Pasted Graphic 19" src="https://user-images.githubusercontent.com/72545732/143769580-e31aee79-af9e-404b-a2f5-e045c20640eb.png">

<img width="930" alt="• paging system" src="https://user-images.githubusercontent.com/72545732/143769584-1b8605bd-7693-4505-8c74-d13c68bfd858.png">

<img width="958" alt="Process1" src="https://user-images.githubusercontent.com/72545732/143769586-a3620ddd-054b-43e3-8de0-934a531cfd0e.png">



페이징 시스템과 MMU(컴퓨터 구조)

<img width="985" alt="Virtual" src="https://user-images.githubusercontent.com/72545732/143769608-f9738ca0-2d30-4f7c-89c0-320596e6a559.png">


페이징 시스템 장점


다중 단계 페이징 시스템
	•	페이징 정보를 단계를 나누어 생성
	•	필요없는 페이지는 생성하지 않으면, 공간 절약 가능


<img width="952" alt="Pasted Graphic 23" src="https://user-images.githubusercontent.com/72545732/143769610-4a8593af-0528-4f02-bb0c-02c78346a102.png">


필요없는 페이지는 생성하지 않는 것이 다중 단계 페이징 시스템

<img width="826" alt="Pasted Graphic 24" src="https://user-images.githubusercontent.com/72545732/143769617-6d891433-0235-4d7e-bceb-edd89f20308c.png">

<img width="942" alt="Virtual address" src="https://user-images.githubusercontent.com/72545732/143769634-0d447db4-ba32-4a1e-bd5d-9f20e95a9bb7.png">


cpu -> mmu -> cr3 register -> mmu -> memory

cr3 레지스터 가기전에 tlb 캐시 테이블 줘서 캐싱시 동작

<img width="900" alt="Pasted Graphic 26" src="https://user-images.githubusercontent.com/72545732/143769646-f58b089f-4413-45cb-b0ed-50430163a83a.png">


페이징 시스템과 공유 메모리
=> 프로세스간 동일한 물리 주소를 가리킬 수 있음(공간 절약, 메모리 할당 시간 절약)

<img width="875" alt="Process A (Parent Process)" src="https://user-images.githubusercontent.com/72545732/143769652-2f42b009-65e4-4b35-a4fe-56261d012d0d.png">


왼쪽의 프로세스 두개에서 1기가씩 커널에 대한 주소가 참조되는데 이걸 페이지 테이블에서 동일한 물리 메모리 주소를 가리키게 하면 공간의 낭비가 없다.

프로세스 복사를 할때 실제로 프로세스를 복사 하지 않고 페이지 테이블에서 process a의 page table에서 가리키는 값을 Process B의 페이지 테이블에도 가리키게 함.

<img width="981" alt="Pasted Graphic 29" src="https://user-images.githubusercontent.com/72545732/143769664-b72ba133-e5f4-4c50-bd06-348dbcf5a3d6.png">


요구 페이징
	•	어느 블록을 어느 시점에 올려두어야 할까??

<img width="970" alt="Pasted Graphic 30" src="https://user-images.githubusercontent.com/72545732/143769669-9c86201e-b307-409c-92c1-acdc08e6969e.png">

page table의 invalid bit가 invalid면 메모리에 올리는 필요할 때마다 적재하는 페이징 

페이지 폴트(page fault)
	•	어떤 페이지가 실제 메모리에 없을때 일어나는 인터럽트
	•	운영체제가 페이지 폴트가 일어나면 페이지를 물리 메모리에 올림, 페이지 테이블 수정

<img width="998" alt="Pasted Graphic 31" src="https://user-images.githubusercontent.com/72545732/143769681-87a2e8d9-4a3f-451e-b440-ffa95c26abfa.png">

	•	페이지 폴트가 자주 일어나면 
	•	실행되기 전에, 해당 페이지를 물리 메모리에 올려야 함
	•	시간이 오래 걸림
	•	페이지 폴트가 안 일어나게 하려면
	•	향후 실행/참조될 코드/데이터를 미리 물리 메모리에 올리면 됨
	•	앞으로 있을 일을 예측해야 함 - 신의 영역


### 페이지 교체 정책
특정 페이지를 물리 메모리에 올리려 하는데 물리 메모리가 다 차있다면?? -> 기존의 페이지를 내리고 새로운 페이지를 올려야 함 

	•	최적 페이지 교체 알고리즘
	•	앞으로 가장 오랫동안 사용하지 않을 페이지를 내리자
	•	일반 OS에서는 구현 불가

	•	LRU (Least Recently Used)
	•	가장 오래전에 사용한 페이지를 교체하자(이중에 자주 사용)
	•	메모리 지역성에 기반

	•	LFU(Least Frequently Used)
	•	가장 적게 사용된 페이지를 내리자

스레싱
	•	반복적으로 페이지 폴트가 발생해서, 과도하게 페이지 교체 작업이 일어나, 실제로는 아무일도 하지 못하는 상황

세그멘테이션
	•	가상 메모리를 서로 크기가 다른 논리적 단위인 세그먼트로 분할
	•	페이징 기법에서는 가상 메모리를 같은 크기의 블록으로 분할

<img width="968" alt="Pasted Graphic 32" src="https://user-images.githubusercontent.com/72545732/143769699-043b4c7a-6d9b-414d-80df-381b47c68937.png">

다양한 컴퓨터 시스템에 이식성을 중요시하는 리눅스는 페이징 기법을 기반으로 구현,
일부 시스템에서는 페이징 기법은 지원하는데 세그멘테이션 기법은 지원 안하는 경우도 있음












파일시스템: 운영체제가 저장매체에 파일을 쓰기위한 자료구조 또는 알고리즘

파일시스템 && 시스템 콜
	•	동일한 시스템콜을 사용해서 다양한 파일 시스템 지원 가능토록 구현
	•	window에서 fat, ntfs, ext4 어떤걸 썼든지 시스템 콜에 대한 결과는 다 같아야 한다.

inode 방식 파일 시스템
	•	파일시스템 기본 구조
	•	슈퍼 블록: 파일 시스템 정보 및 파티션 정보
	•	아이노드 블록: 파일 상세 정보
	•	데이터 블록: 실제 데이터

inode와 파일
	•	파일: inode 고유값과 자료구조에 의해 주요 정보 관리
	•	'파일이름:inode'로 파일이름은 inode 번호와 매칭
	•	파일 시스템에서는 inode를 기반으로 파일 엑세스
	•	inode 기반 메타 데이터 저장

<img width="437" alt="Disk Block" src="https://user-images.githubusercontent.com/72545732/143769714-db593baa-fb61-4750-bd0d-9ff4ea4aea6e.png">

	•	inode 기반 메타 데이터(파일 권한, 소유자 정보, 파일 사이즈, 생성시간등)

<img width="493" alt="ext file system inode structure" src="https://user-images.githubusercontent.com/72545732/143769718-dc3587e4-ce01-4e78-8819-1ecc29736152.png">


<img width="897" alt="Pasted Graphic 4" src="https://user-images.githubusercontent.com/72545732/143769745-f383b629-2cc6-4810-abbf-c6a6d7d48cb1.png">

<img width="943" alt="Pasted Graphic 5" src="https://user-images.githubusercontent.com/72545732/143769750-e02d3091-f6e7-4eb2-bc22-0ee6e0b2d921.png">

<img width="1036" alt="Pasted Graphic 6" src="https://user-images.githubusercontent.com/72545732/143769756-9cc2c5d6-2e54-411d-8c13-ea866ef638cd.png">





가상 파일 시스템
	•	Network등 다양한 기기도 동일한 파일 시스템 인터페이스를 통해 관리 가능
	•	예: read/write 시스템콜 사용, 각 기기별 read_spec/write_spec 코드 구현(운영체제 내부)

<img width="495" alt="file-system interface" src="https://user-images.githubusercontent.com/72545732/143769763-422c0390-ab45-4b40-8472-753709d523d9.png">

파일시스템 인터페이스를 통해 네트워크 데이터를 읽거나 쓰게끔 할 수 있다
모든 디바이스를 다 파일처럼 다룬다.

리눅스 운영체제와 가상 파일 시스템
	•	모든 것은 파일이라는  철학을 따름
	•	마우스, 키보드와 같은 모든 디바이스 관련된 기술도 파일과 같이 다루어짐,
	•	모든 자원에 대한 추상화 인터페이스로 파일 인터페이스를 활용





부팅의 이해

부트: 컴퓨터를 켜서 동작시키는 절차
부트 프로그램 : 운영체제 커널을 Storage에서 특정 주소의 물리 메모리로 복사하고 커널의 처음 실행위치로 PC(Program Counter)를 가져다 놓는 프로그램

	•	폰노이만 구조에서 모든 코드는 메모리에 있어야 한다.


ROM-BIOS는 메모리에 BIOS프로그램을 올리는 역할

<img width="1016" alt="Memory (RAM)" src="https://user-images.githubusercontent.com/72545732/143769778-019efb11-7323-4485-838b-c1c12c781b74.png">

<img width="1021" alt="Pasted Graphic 8" src="https://user-images.githubusercontent.com/72545732/143769780-9d05343b-9a6e-489f-a4f1-0804f987938e.png">




가상머신의 이해

하드웨어를 소프트웨어로 여러개처럼 보이는 기술

<img width="968" alt="Bare-Metal Virtualization" src="https://user-images.githubusercontent.com/72545732/143769787-54345129-1e49-4ec0-989d-99d08eafb673.png">


하드웨어를 실제로 나눠 버리는 타입1 (약간 파티션 개념??), 타입2보다 성능이 빠르다

<img width="936" alt="Virtual Machine Type2" src="https://user-images.githubusercontent.com/72545732/143769791-ee29c7ac-8c6a-4343-8c74-bc84622ce562.png">


OS위에 OS를 추가로 설치, vm안의 app이 실행되려면 vm os -> vmm -> host os 거쳐야 해서 TYPE1에 비해 느림

전가상화, 반가상화
전가상화 => 각 가상머신이 하이퍼 바이저를 통해서 하드웨어와 통신 중간에 vmm,이 통역사 역할

<img width="949" alt="Pasted Graphic 11" src="https://user-images.githubusercontent.com/72545732/143769804-2e82c825-ac3e-41e4-9eae-774389b03a5f.png">

반가상화 : 각 가상머신에서 직접 하드웨어와 통신

<img width="949" alt="Pasted Graphic 11" src="https://user-images.githubusercontent.com/72545732/143769808-f8fa144b-ef64-4616-8a33-67ac2bc363a4.png">


반가상화는 vm 안의 OS를 수정해야해서 복잡함


vmware

<img width="876" alt="Virtual Machine1" src="https://user-images.githubusercontent.com/72545732/143769826-6e7feae4-5d44-46fb-b072-b41ac0c4438e.png">



또 다른 가상 머신: Docker 
	•	가상 머신은 컴퓨터 하드웨어를 가상화
	•	Docker는 운영체제 레벨에서 별도로 분리된 실행 환경을 제공(커널 추상화)

<img width="990" alt="Pasted Graphic 15" src="https://user-images.githubusercontent.com/72545732/143769829-76cff6e9-2954-4e14-b9d9-9ecbf068502b.png">


Docker는 경량 이미지로 실행환경을 통째로 백업, 실행 가능(실무에 많이 사용됨)

Java Virtual Machine
	•	응용프로그램 레벨 가상화
	•	어느 환경이든 실행을 알아서 해주어라 에서 나온 개념
	•	Java 컴파일러는 bytecode를 생성
