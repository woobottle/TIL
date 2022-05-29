function solution(records) {
  var answer = [];
  const users = new Map();
  records.forEach((record) => {
    const [type, uid, name] = record.split(" ");
    if (type === "Enter") users.set(uid, name);
    if (type === "Change") users.set(uid, name);
  });

  records.forEach((record) => {
    const [type, uid, name] = record.split(" ");
    if (type === "Enter") answer.push(`${users.get(uid)}님이 들어왔습니다.`);
    if (type === "Leave") answer.push(`${users.get(uid)}님이 나갔습니다.`);
  });
  return answer;
}
