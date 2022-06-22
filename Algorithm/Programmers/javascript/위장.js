function solution(clothes) {
  let answer = 1;
  const closet = new Map();
  clothes.forEach(([cloth, type]) => {
    if (closet.has(type)) {
      const prev = closet.get(type);
      closet.set(type, [...prev, cloth]);
    } else {
      closet.set(type, [cloth]);
    }
  });

  for ([type, values] of closet.entries()) {
    answer *= values.length + 1;
  }
  return answer - 1;
}
