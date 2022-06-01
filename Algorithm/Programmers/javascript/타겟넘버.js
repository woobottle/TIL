function dfs({ numbers, operators, target }, answer) {
  if (operators.length < numbers.length) {
    dfs({ numbers, operators: [...operators, "+"], target }, answer);
    dfs({ numbers, operators: [...operators, "-"], target }, answer);
    return;
  }

  if (calc(numbers, operators) === target) {
    answer.count += 1;
  }
  return;
}

function solution(numbers, target) {
  var answer = { count: 0 };
  const operatorsStartWithPlus = ["+"];
  const operatorsStartWithMinus = ["-"];
  dfs({ numbers, operators: operatorsStartWithPlus, target }, answer);
  dfs({ numbers, operators: operatorsStartWithMinus, target }, answer);

  return answer.count;
}

function calc(numbers, operators) {
  let result = 0;
  operators.forEach((operator, index) => {
    if (operator === "+") result += numbers[index] * 1;
    if (operator === "-") result += numbers[index] * -1;
  });
  return result;
}
