let arr = [1,2,3]
for (const a of arr) console.log(a)

arr[Symbol.iterator] = null
// for (const a of arr) console.log(a);


let range = {
  from: 1,
  to: 5,

  [Symbol.iterator]() {
    this.current = this.from
    return this
  },

  next() {
    if (this.current <= this.to) {
      return { done: false, value: this.current++ }
    } else {
      return { done: true }
    }
  }
};


for (let a of range) { console.log(a)} 
// range[Symbol.iterator] = function(){
//   return {
//     current: this.from,
//     last: this.to,

//     next() {
//       if (this.current <= this.last) {
//         return { done: false, value: this.current++ }
//       } else {
//         return { done: true  };
//       }
//     }
//   }
// }

// for (let a of range) console.log(a);


const hihi = "hihi"
const iterator = hihi[Symbol.iterator]()

while (true) {
  const { done, value = "" } = iterator.next()
  if (done) {
    break
  } 
  console.log(value)
}

let arrs = [1,2,3,4,5]
console.log(Array.from(arrs, num => num * num))

const map = new Map([[1,2], [2,3], [3,4]])
for (let a of map) console.log(a)

let iteors = map[Symbol.iterator]()
console.log(iteors.next());
console.log(iteors.next());
console.log(iteors.next());
console.log(iteors.next());

const set = new Set([1,2,3,4])
let setIteors = set[Symbol.iterator]()
console.log(setIteors.next());
console.log(setIteors.next());
console.log(setIteors.next());
console.log(setIteors.next());
console.log(setIteors.next());