const spider = document.querySelector(".spider")
const spiderWeb = document.querySelector('.spider-web')

const screen = { x: window.screen.width, y: window.screen.height }
const initialPointer = { x: 0, y: 0 }
// 이동할 거리
const offset = { x: 0, y: 0 }

const spiderMoveHandler = (e) => {
  // clientX,Y 는 viewport를 기준으로 x,y 위치를 반환함
  // 모바일에서는 touches를 통해 커서의 위치를 가져올 수 있다.
  const cursorX = e.clientX || e.touches[0].clientX;
  const cursorY = e.clientY || e.touches[0].clientY;

  offset.x = cursorX - initialPointer.x;
  offset.y = cursorY - initialPointer.y;

  // left가 x, top이 y
  spider.style.transform = `translate(${offset.x}px, ${offset.y}px)`;
};

const shootWeb = () => {
  spiderWeb.style.transform = `translateX(${screen.x * 1.5}px)`;
  spiderWeb.style.transition = `1s`;
}

const initialWeb = () => {
  spiderWeb.style.transform = 'none';
  spiderWeb.style.transition = 'none';
}

spider.addEventListener('click', () => {
  shootWeb();
})

spider.addEventListener('mouseup', () => {
  removeEventListener('mousemove', spiderMoveHandler);
  shootWeb();
})

spider.addEventListener("mousedown", (e) => {
  // drag로 이동한 경우 translate로 offset의 x,y 만큼 이동한 상황이다.
  // translate는 현재 위치를 기반으로 이동하므로 이전에 이동한 offset의 values 만큼 빼주어야 한다.
  initialPointer.x = e.clientX - offset.x;
  initialPointer.y = e.clientY - offset.y;
  
  addEventListener("mousemove", spiderMoveHandler);
  initialWeb();
});

spider.addEventListener("touchend", () => {
  removeEventListener("touchmove", spiderMoveHandler);
  shootWeb();
});

spider.addEventListener("touchstart", (e) => {
  // spider를 터치시 아래 요소들도 같이 터치되는 것을 막기위해 사용
  e.preventDefault();
  initialPointer.x = e.clientX || e.touches[0].clientX - offset.x; // clientX,Y 는 viewport를 기준으로 x,y 위치를 반환함
  initialPointer.y = e.clientY || e.touches[0].clientY - offset.y;

  addEventListener("touchmove", spiderMoveHandler);
  initialWeb();
});


// getBoundingClientRect 는 dom 요소의 뷰포트에서의 위치를 반환해준다.
// boxPosition.x = dragBox.getBoundingClientRect().x;
// boxPosition.y = dragBox.getBoundingClientRect().y;

// mouseup
// mousedown
// mousemove
