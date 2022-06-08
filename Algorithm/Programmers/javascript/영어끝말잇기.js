function solution(n, words) {
  var answer = [0, 0];
  const wordsLength = words.length;
  const previousWords = new Set();
  previousWords.add(words[0]);

  for (let i = 1; i < wordsLength; i++) {
    const word = words[i];
    const people = (i % n) + 1;
    const turn = ~~(i / n) + 1;
    const isLastWordSameWithFirstWord =
      words[i - 1][words[i - 1].length - 1] === word[0];

    if (previousWords.has(word) || !isLastWordSameWithFirstWord) {
      answer = [people, turn];
      break;
    }

    previousWords.add(word);
  }

  return answer;
}
