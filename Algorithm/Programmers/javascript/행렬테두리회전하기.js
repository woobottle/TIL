function getArray({ rows, columns }) {
  const array = Array.from({ length: rows }, (_, i) =>
    Array.from({ length: columns }, (_, ii) => i * columns + ii + 1)
  );
  return array;
}

function solution(rows, columns, queries) {
  var answer = [];
  const array = getArray({ rows, columns });

  for (query of queries) {
    const [x1, y1, x2, y2] = [
      query[0] - 1,
      query[1] - 1,
      query[2] - 1,
      query[3] - 1,
    ];
    const temp = [];

    for (let i = y1; i < y2; i++) temp.push(array[x1][i]);
    for (let i = x1; i < x2; i++) temp.push(array[i][y2]);
    for (let i = y2; i > y1; i--) temp.push(array[x2][i]);
    for (let i = x2; i > x1; i--) temp.push(array[i][y1]);

    answer.push(Math.min(...temp));
    temp.unshift(temp.pop());

    for (let i = y1; i < y2; i++) array[x1][i] = temp.shift();
    for (let i = x1; i < x2; i++) array[i][y2] = temp.shift();
    for (let i = y2; i > y1; i--) array[x2][i] = temp.shift();
    for (let i = x2; i > x1; i--) array[i][y1] = temp.shift();
  }
  return answer;
}
