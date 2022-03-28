console.log('script start')

setTimeout(() => console.log('first setTimeout'))

queueMicrotask(() => console.log('micro task queue'))
Promise.resolve('a').then(() => console.log('promise'))
console.log("script middle");
requestAnimationFrame(() => console.log("animation frame"));
console.log("script end");
