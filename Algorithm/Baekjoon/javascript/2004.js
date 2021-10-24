const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const n = +input[0];
const m = +input[1];

const divide_by_five = function(num) {
  let body = 0;
  while(num) {
    body += ~~(num / 5);
    num = ~~(num / 5)
  }
  return body;
}

const divide_by_two = function (num) {
  let body = 0;
  while (num) {
    body += ~~(num / 2);
    num = ~~(num / 2);
  }
  return body;
};

const count_five = divide_by_five(n) - divide_by_five(m) - divide_by_five(n - m);
const count_two =
  divide_by_two(n) - divide_by_two(m) - divide_by_two(n - m);
console.log(Math.min(count_five, count_two))