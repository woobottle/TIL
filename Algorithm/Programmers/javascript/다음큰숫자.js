function solution(n) {
  var answer = 0;
  const binaryString = changeToBinary(n);
  const currentOneCount = getOneCount(binaryString);
  let target = n + 1;
  while (true) {
    const next = target++;
    const nextBinaryString = changeToBinary(next);
    if (currentOneCount === getOneCount(nextBinaryString)) {
      answer = next;
      break;
    }
  }

  return answer;
}

function changeToBinary(number) {
  return number.toString(2);
}

function getOneCount(target) {
  let count = 0;
  for (let i = 0; i < target.length; i++) {
    if (target[i] === "1") count++;
  }
  return count;
}
