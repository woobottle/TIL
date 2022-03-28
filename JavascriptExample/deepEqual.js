const deepEqual = (a, b) => {
  for (let key in a) {
    if (typeof a[key] === 'object') { 
      if (typeof b[key] === "object") {
        return deepEqual(a[key], b[key]);
      } else {
        return false;
      }
    }
    
    if (a[key] !== b[key]) {
      return false;
    }
  }

  return true
}

const deepCopy = (a, temp) => {
  for (let key in a) {
    if (typeof a[key] === "object") {
      deepCopy(a[key], temp[key] = {})
    } else {
      temp[key] = a[key]
    }
  }

  return temp;
};

const a = { b: { c: 'c' }, d: { e: 'e' }}
const b = { b: { c: 'c' }}
const c = deepCopy(a, {})
const d = JSON.parse(JSON.stringify(c))

console.log(a)
console.log(b)
console.log(c)
console.log(d)
console.log(Object.is(a, b))
console.log(Object.is(a, c));
console.log(deepEqual(a, b))
console.log(deepEqual(a, c));