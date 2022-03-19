const debounce = (func, delay) => {
  let timer
  
  return (...args) => {
    if(timer) clearTimeout(timer)
    timer = setTimeout(() => func.apply(this, args), delay)
  }

}

const debounceInput = document.querySelector("#debounce-input")
let i = 0;
debounceInput.addEventListener('keyup', debounce(() => { i += 1; console.log(i) }, 1000))




const throttle = (func, delay) => {
  let timer = null;
  // 클로저를 이용 timer를 제어
  // timer가 null일 때만 setTimeout 실행
  // setTimeout내에서 콜백 실행후 timer null로 변환해줌
  return (...args) => {
    if (!timer) {
      timer = setTimeout(() => {
        func.apply(this, args);
        timer = null;
      }, delay);
    }
  };
};

const throttleInput = document.querySelector("#throttle-input");
let j = 0;
throttleInput.addEventListener("keyup", 
  throttle(() => { j += 1; console.log(j) }, 1000)
);



