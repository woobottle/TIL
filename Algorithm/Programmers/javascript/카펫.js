function solution(brown, yellow) {
  var answer = [];
  const total = brown + yellow;
  for (let height = 1; height <= Math.sqrt(total); height++) {
    let isDivisor = total % height === 0;
    let width = ~~(total / height);
    if (
      isDivisor &&
      Number.isInteger(width) &&
      (width + height - 2) * 2 === brown
    ) {
      answer = [width, height];
      break;
    }
  }
  return answer;
}
