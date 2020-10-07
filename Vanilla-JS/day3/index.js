const title = document.getElementById("title");
console.log(title);
console.error("What!");
title.innerHTML = "Hi! I'm from JS!";
console.dir(title);

function handleResize(event) {
  console.log(event);
}
function handleClick(event) {
  title.style.color = "red";  
}

window.addEventListener("resize", handleResize);
window.addEventListener("click", handleClick);
