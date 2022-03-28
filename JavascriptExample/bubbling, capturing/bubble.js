const divs = document.querySelectorAll('div');

divs.forEach(div => {
  div.addEventListener(
    "click",
    function (e) {
      e.stopPropagation()
      console.log(this.classList);
    }
  );
})