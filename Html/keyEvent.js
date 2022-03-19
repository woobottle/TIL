const keydown = document.querySelector('#keydown')
const keyup = document.querySelector("#keyup");
const keypress = document.querySelector("#keypress");

keydown.addEventListener('keydown', function(e) {
  console.log('this is keydown', e.target.value)
})

keyup.addEventListener('keyup', function(e) {
  console.log('this is keyup', e.target.value)
})

keypress.addEventListener("keypress", function (e) {
  console.log('this is keypress', e.target.value);
});
