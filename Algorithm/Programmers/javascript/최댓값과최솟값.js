function solution(s) {
  const splited = s.split(" ");
  const minNumber = Math.min(...splited);
  const maxNumber = Math.max(...splited);

  var answer = `${minNumber} ${maxNumber}`;

  return answer;
}
