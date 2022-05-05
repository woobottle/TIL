function solution(id_list, reports, k) {
  var answer = {};
  const reportedMember = {};
  board = {};

  id_list.forEach((report) => {
    board[`${report}`] = { report: new Set(), reported: new Set() };
    reportedMember[`${report}`] = 0;
    answer[`${report}`] = 0;
  });

  reports.forEach((report) => {
    const [reportee, reporter] = report.split(" ");
    board[`${reporter}`].reported.add(reportee);
    board[`${reportee}`].report.add(reporter);
  });

  for (const [key, value] of Object.entries(board)) {
    reportedMember[`${key}`] = value.reported.size;
  }

  for (const [key, value] of Object.entries(reportedMember)) {
    const reported = board[`${key}`].reported.size;
    if (reported >= k) {
      for (let item of board[`${key}`].reported) {
        answer[item] += 1;
      }
    }
  }

  return Object.values(answer);
}

// function solution(id_list, report, k) {
//   let reports = [...new Set(report)].map((a) => {
//     return a.split(" ");
//   });

//   let counts = new Map();
//   for (const [reporter, reportee] of reports) {
//     counts.set(reportee, counts.get(reportee) + 1 || 1);
//   }

//   let good = new Map();
//   for (const [reporter, reportee] of reports) {
//     if (counts.get(reportee) >= k) {
//       good.set(reporter, good.get(reporter) + 1 || 1);
//     }
//   }

//   let answer = id_list.map((a) => good.get(a) || 0);
//   return answer;
// }