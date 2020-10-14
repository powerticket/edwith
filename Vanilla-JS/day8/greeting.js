const form = document.querySelector(".js-form"),
  input = form.querySelector("input");

const greeting = document.querySelector(".js-greeting");

const USER_LS = "currentUser";
const SHOWING = "showing";

function printGreeting(text) {
  form.classList.remove(SHOWING);
  greeting.classList.add(SHOWING);
  greeting.innerText = `Hello ${text}`;
}

function handleSubmit(event) {
  event.preventDefault();
  const currentValue = input.value;
  saveName(currentValue);
  printGreeting(currentValue);
  
}

function saveName(text) {
  localStorage.setItem(USER_LS, text);
}

function askName() {
  form.classList.add(SHOWING);
  form.addEventListener("submit", handleSubmit)
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