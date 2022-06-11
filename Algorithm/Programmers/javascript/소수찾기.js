function solution(numbers) {
  var answer = 0;
  const array = numbers.split("").sort((a, b) => b - a);
  const primeNumberArray = getPrimeNumberArray(parseInt(array.join("")));
  const result = [];
  for (let i = 1; i <= numbers.length; i++) {
    result.push(getPermutations(array, i));
  }
  const resultSet = [
    ...new Set(result.flat().map((numbers) => parseInt(numbers.join("")))),
  ];
  resultSet.forEach((number) => {
    if (primeNumberArray[number]) answer += 1;
  });

  return answer;
}

// 최대범위까지 소수인지 아닌지를 가지고 있는 배열 하나 생성
function getPrimeNumberArray(number) {
  const result = Array.from({ length: number + 1 }, () => true);
  result[0] = false;
  result[1] = false;

  for (let i = 2; i <= parseInt(Math.sqrt(number)); i++) {
    for (let j = i * 2; j <= number; j += i) {
      if (result[j] === true) result[j] = false;
    }
  }
  return result;
}

// 순열
function getPermutations(arr, r) {
  const result = [];
  if (r === 1) return arr.map((num) => [num]);
  arr.forEach((fixed, index, org) => {
    const rest = [...org.slice(0, index), ...org.slice(index + 1)];
    const permutations = getPermutations(rest, r - 1);
    const attachment = permutations.map((numbers) => [fixed, ...numbers]);
    result.push(...attachment);
  });
  return result;
}
