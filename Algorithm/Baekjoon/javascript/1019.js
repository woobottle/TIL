const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const first = +input[0];
const first = 19;
const result = Array.from({length: 10}, (i) => 0)

const calc = (start, end, ten) => {
  count = ~~(start / 10) - ~~(end / 10) + 1
  result.forEach((el, index) => {
    result[index] += count * ten;
  })
}

const increase_by_num = (num, ten) => {
  while(num) {
    result[num % 10] += ten;
    num /= 10;
  }
}

const solution = (start, end, ten) => {
  while(start % 10 !== 0 && start <= end) {
    increase_by_num(start, ten);
    start += 1;
  }

  if (start > end) {
    return;
  }

  while (end % 10 !== 9 && end >= start) {
    increase_by_num(end, ten);
    end -= 1;
  }

  calc(start, end, ten);
  solution(~~(start / 10), ~~(end / 10), ten * 10)
}

solution(1, first, 1);
for(let i of result) {
  console.log(i)
}
