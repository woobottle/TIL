function solution(s) {
  var answer = -1;
  const body = Array.from(s);
  const stack = [body.shift()];
  for (let i = 0; i < body.length; i++) {
    if (stack[stack.length - 1] === body[i]) {
      stack.pop();
    } else {
      stack.push(body[i]);
    }
  }
  answer = stack.length === 0 ? 1 : 0;
  return answer;
}
