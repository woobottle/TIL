class Node {
  constructor(data) {
    this.data = data
    this.next = null
  }
}

class Relation {
  constructor(inclusives, exclusives) {
    this.inclusives = inclusives;
    this.exclusives = exclusives;
    this.Nodes = {}
  }

  set_inclusive_graph(inclusive) {

  }

  set_exclusive_graph(exclusive) {

  }

  get_inclusives(first, second) {

  }

  get_exclusive(first, second) {

  }
}

const inclusives = [
  { superset:  'q1', subset: 'q2' },
  { superset:  'q2', subset: 'q3' },
  { superset:  'q4', subset: 'q5' },
]

const exclusives = [
  ['q2', 'q4'],
  ['q2', 'q6']
] // # 배반 pair는 순서를 구분하지 않습니다. 

const relations = new Relation(inclusives, exclusives) 
// # inclusive, exclusive 는 위에서 사용자가 정의한 위험률 관계입니다. 
// # inclusives와 exclusives 정의는 변경될 수 있습니다.

relations.get_inclusives('q1', ['q2', 'q4']) // # returns ['q1', 'q2'] 'q1'이 가장 크고 그 다음이 'q2'입니다.
relations.get_inclusives('q2', ['q1', 'q3']) // # returns ['q1', 'q2', 'q3'] 
relations.get_inclusives('q2', ['q1']) // # returns ['q1', 'q2']
relations.get_inclusives('q4', ['q1']) // # returns []

relations.get_exclusive('q3', ['q6', 'q5']) // # returns ['q6', 'q5']  q3 <-> q6, q3 <-> q5
relations.get_exclusive('q1', ['q2', 'q4']) // # returns []