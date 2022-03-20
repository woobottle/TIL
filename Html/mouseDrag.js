const spider = document.querySelector(".spider")
const spiderWeb = document.querySelector('.spider-web')

const screen = { x: window.screen.width, y: window.screen.height }
const initialPointer = { x: 0, y: 0 }
const offset = { x: 0, y: 0 }

const mouseMoveHandler = (e) => {
  const cursorX = e.clientX;
  const cursorY = e.clientY;
  
  offset.x = cursorX - initialPointer.x;
  offset.y = cursorY - initialPointer.y;

  // left가 x, top이 y
  spider.style.transform = `translate(${offset.x}px, ${offset.y}px)`;
};

const shootWeb = () => {
  spiderWeb.style.transform = `translateX(${screen.x}px)`;
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
  removeEventListener('mousemove', mouseMoveHandler);
  shootWeb();
})

spider.addEventListener("mousedown", (e) => {
  initialPointer.x = e.clientX - offset.x; // clientX,Y 는 viewport를 기준으로 x,y 위치를 반환함
  initialPointer.y = e.clientY - offset.y;
  
  addEventListener("mousemove", mouseMoveHandler);
  initialWeb();
});

// getBoundingClientRect 는 dom 요소의 뷰포트에서의 위치를 반환해준다.
// boxPosition.x = dragBox.getBoundingClientRect().x;
// boxPosition.y = dragBox.getBoundingClientRect().y;

// mouseup
// mousedown
// mousemove