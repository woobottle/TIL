function solution(n) {
  var answer = "";
  // 3진수로 바꾸고 1일때 1, 2일때 2, 0일때 4
  const remainder = ["4", "1", "2"];
  while (n > 0) {
    let body = n % 3;
    answer = remainder[body] + answer;
    n = Math.floor((n - 1) / 3);
  }
  return answer;
}
