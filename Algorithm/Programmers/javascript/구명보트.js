function solution(people, limit) {
  let answer = 0;
  const sortedPeople = [...people].sort((a, b) => b - a);
  let leftPoint = 0;
  let rightPoint = sortedPeople.length - 1;

  while (leftPoint <= rightPoint) {
    const leftPerson = sortedPeople[leftPoint];
    const rightPerson = sortedPeople[rightPoint];
    const sum = leftPerson + rightPerson;
    if (sum <= limit) {
      leftPoint++;
      rightPoint--;
    } else {
      leftPoint++;
    }
    answer++;
  }
  return answer;
}

// https://programmers.co.kr/learn/courses/30/lessons/42885