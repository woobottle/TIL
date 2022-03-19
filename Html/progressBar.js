const percent = document.querySelector('.percent')

// 0 -> 300 -> 0

const counter = () => {
  let count = 0;
  let is_plus = true;

  return () => {
    if(is_plus) {
      count += 1
    } 
    if (!is_plus) {
      count -= 1
    }

    if (count >= 100) {
      is_plus = false;
    } 
    if (count <= 0) {
      is_plus = true;
    }

    percent.textContent = `${count}`;
  }
}

const counterNumber = counter()
setInterval(() => counterNumber(), 30);
// 3초에 100을 올려야함

