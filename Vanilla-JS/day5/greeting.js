const form = document.querySelector(".js-form"),
  input = form.querySelector("input");

const greeting = document.querySelector(".js-greeting");

const USER_LS = "currentUser";
const SHOWING = "showing";

function printGreeting(text) {
  greeting.classList.add(SHOWING);
  greeting.innerText = `Hello ${text}`;
}

function askName() {
  form.classList.add(SHOWING);
}

function loadName() {
  const currentUser = localStorage.getItem(USER_LS);
  if (currentUser) {
    printGreeting(currentUser);
  } else {
    askName();
  }
}

function init() {
  loadName();
}

init();