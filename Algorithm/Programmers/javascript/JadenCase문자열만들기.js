function solution(s) {
  let downCase = s.toLowerCase();
  var answer = downCase
    .split(" ")
    .map((el) => el.charAt(0).toUpperCase() + el.substring(1))
    .join(" ");
  return answer;
}
