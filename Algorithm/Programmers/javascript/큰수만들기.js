function solution(number, k) {
  let answer = "";
  let deleteCount = -1;
  let answerArray = [0];

  for (let i = 0; i < number.length; i++) {
    while (deleteCount < k && answerArray[answerArray.length - 1] < number[i]) {
      answerArray.pop();
      deleteCount++;
    }
    if (answerArray.length < number.length - k) answerArray.push(number[i]);
  }
  answer = answerArray.join("");
  return answer;
}

// https://programmers.co.kr/learn/courses/30/lessons/42883#