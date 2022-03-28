const arr = [1,2,3,4]
console.log(arr.map((el) => el * 2))

Array.prototype.customMap = function (callback) {
  const result = []

  for(let el of this) {
    result.push(callback(el))
  }

  return result
}


console.log(arr.customMap((el) => el * 3))