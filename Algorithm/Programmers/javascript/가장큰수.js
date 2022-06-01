function solution(numbers) {
  var answer = "";
  answer = numbers.sort(sortFunc).join("");
  if (answer[0] === "0") return "0";
  return answer;
}

function sortFunc(a, b) {
  const compareA = parseInt(a.toString() + b.toString());
  const compareB = parseInt(b.toString() + a.toString());
  return compareB - compareA;
}
