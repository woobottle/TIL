function solution(bridge_length, weight, truck_weights) {
  var day = 0;
  // 실제 구현으로 가자
  const bridge = new Array(bridge_length).fill(0);
  const trucks = [...truck_weights];
  do {
    day += 1;
    bridge.pop();

    const bridgeCurrentWeight = bridge.reduce((prev, curr) => prev + curr, 0);
    bridgeCurrentWeight + trucks[0] <= weight
      ? bridge.unshift(trucks.shift())
      : bridge.unshift(0);
    trucks.push(0);
  } while (bridge.reduce((prev, curr) => prev + curr, 0) !== 0);
  return day;
}
