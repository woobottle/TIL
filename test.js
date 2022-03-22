// let a = (cb) => setTimeout(cb, 1000)
// let b = (cb) => setTimeout(cb, 1000);
// let c = (cb) => setTimeout(cb, 1000);
// let d = (cb) => setTimeout(cb, 1000);

// let test = () => {
//   a(() => {
//     console.log('a');
//     b(() => {
//       console.log('b')
//       c(() => {
//         console.log('c');
//         d(() => {
//           console.log('d')
//         })
//       })
//     })
//   })
// };

// test();

let a = () =>
  new Promise((resolve, reject) => setTimeout(() => resolve("a"), 1000));
let b = () =>
  new Promise((resolve, reject) => setTimeout(() => resolve("b"), 1000));
let c = () =>
  new Promise((resolve, reject) => setTimeout(() => resolve("c"), 1000));
let d = () =>
  new Promise((resolve, reject) => setTimeout(() => resolve("d"), 1000));

// a()
//   .then((data) => {
//     console.log(data);
//     return b();
//   })
//   .then((data) => {
//     console.log(data);
//     return c();
//   })
//   .then((data) => {
//     console.log(data);
//     return d();
//   })
//   .then((data) => {
//     console.log(data);
//   });

Promise.all([a(), b(), c(), d()]).then(() => console.log('done'))