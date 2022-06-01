function solution(progresses, speeds) {
  var answer = [];
  // 필요한 날자들을 먼저 구해버리고 그것으로 계산
  const days = progresses.map((progress, index) => {
    return Math.ceil((100 - progress) / speeds[index]);
  });

  let standard = days[0];
  let count = 0;
  days.forEach((day) => {
    if (day <= standard) {
      count += 1;
    } else {
      answer.push(count);
      standard = day;
      count = 1;
    }
  });
  answer.push(count);
  return answer;
}
