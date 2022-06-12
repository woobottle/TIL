function solution(citations) {
  var answer = 0;
  for (let h = 0; h <= citations.length; h++) {
    const quotations = citations.filter((el) => el >= h).length;
    if (quotations >= h) answer = Math.max(answer, h);
  }

  return answer;
}
