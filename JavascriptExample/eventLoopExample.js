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

let test = () => {
  setTimeout(() => {
    console.log('a');
    setTimeout(() => {
      console.log('b');
      setTimeout(() => {
        console.log('c');
        setTimeout(() => {
          console.log('d');
          setTimeout(() => {
            console.log('e')
          }, 1000)
        }, 1000)
      }, 1000)
    }, 1000)
  }, 1000)
}

test = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log('a')
      resolve(new Promise((resolve) => {
        setTimeout(() => {
          console.log('b')
          resolve(new Promise((resolve) => {
            setTimeout(() => {
              console.log('c');
              resolve(new Promise((resolve) => {
                setTimeout(() => {
                  console.log('d')
                  resolve(new Promise((resolve) => {
                    setTimeout(() => {
                      console.log('e');
                      resolve()
                    }, 1000)
                  }))
                }, 1000)
              }))
            }, 1000)
          }))
        }, 1000)
      }));
    }, 1000)
  })
}


// test();

// let a = () =>
//   new Promise((resolve, reject) => setTimeout(() => resolve("a"), 1000));
// let b = () =>
//   new Promise((resolve, reject) => setTimeout(() => resolve("b"), 1000));
// let c = () =>
//   new Promise((resolve, reject) => setTimeout(() => reject(new Error('this is error')), 1000));

// Promise.all([a(), b()]).then(data => console.log(data)) // 전부 성공해야 반환, 실패하면 실패한 것 반환
// Promise.allSettled([a(), b(), c()]).then(data => console.log(data)); // status와 value를 같이 반환
// Promise.any([a(), b(), c()]).then(data => console.log(data)) // 주어진 모든 프로미스 중 하나라도 이행하는 순간 반환
// Promise.race([a(), b(), c()]).then((data) => console.log(data)); // 가장먼저 실행되는 것 반환


// test = () => {
//   a()
//     .then((data) => {
//       console.log(data);
//       return b();
//     })
//     .then((data) => {
//       console.log(data);
//       return c();
//     })
//     .then((data) => {
//       console.log(data); 
//     })
//     .catch(err => console.log(err))
// }

// test()


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

// Promise.all([a(), b(), c(), d()]).then(() => console.log('done'))


// const makeBrowser = function() {
//   const uiInterface = getUiInterface();
//   const broserEngine = getBroserEngine();
//   const renderingEngine = genRenderingEngine();
//   const networking = getNetworking();
//   const javascriptEngine = getJavascriptEngine();
//   const uiBackend = getUiBackend();
//   const dataPersistence = getDataPersistence();
// } 

// let a = () =>
//   new Promise((resolve, reject) => setTimeout(() => resolve("a"), 1000));
// let b = () =>
//   new Promise((resolve, reject) => setTimeout(() => resolve("b"), 1000));
// let c = () =>
//   new Promise((resolve, reject) => setTimeout(() => resolve('c'), 1000));
// let d = () =>
//   new Promise((resolve, reject) => setTimeout(() => resolve("d"), 1000));
// let e = () =>
//   new Promise((resolve, reject) => setTimeout(() => resolve("e"), 1000));

// const tt = (data) => 
//   new Promise((resolve) => setTimeout(() => resolve(data), 1000));

// let alphabets = ['a', 'b', 'c', 'd', 'e']

// alphabets.map(async alpha => console.log(await tt(alpha)));
// alphabets.forEach(async alpha => console.log(await tt(alpha)));
// for(let alpha of alphabets) {
//   (async function(){
//     console.log(await tt(alpha))
//   }())
// }

let a = () =>
  new Promise((resolve, reject) => setTimeout(() => resolve("a"), 1000));
let b = () =>
  new Promise((resolve, reject) => setTimeout(() => resolve("b"), 1000));
let c = () =>
  new Promise((resolve, reject) => setTimeout(() => reject(new Error('c')), 1000));
let d = () =>
  new Promise((resolve, reject) => setTimeout(() => resolve("d"), 1000));
let e = () =>
  new Promise((resolve, reject) => setTimeout(() => resolve("e"), 1000));

(async function () {
  try {
    console.log(await a());
    console.log(await b());
    console.log(await c());
    console.log(await d());
    console.log(await e());
  } catch(err) {
    console.log(err);
  }
})();