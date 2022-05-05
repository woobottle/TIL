function solution(s) {
  var answer = [];
  const totalLength = s.length;

  for (let i = 1; i <= totalLength; i++) {
    // 압축 하는 방법
    answer.push(compressedString(i, s).length);
  }
  return Math.min(...answer);
}

function compressedString(unit, sentence) {
  let count = 1;
  result = [""];
  for (let repeat = 0; repeat <= sentence.length / unit; repeat++) {
    const sliceGroup = sentence.slice(repeat * unit, repeat * unit + unit);
    if (result[result.length - 1] === sliceGroup) {
      count++;
    } else {
      if (count > 1) {
        result.push(count);
      }
      result.push(sliceGroup);
      count = 1;
    }
  }
  return result.join("");
}
