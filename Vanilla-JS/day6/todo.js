const toDoForm = document.querySelector(".js-toDoForm"),
  toDoInput = toDoForm.querySelector("input"),
  toDOList = document.querySelector(".js-toDoList");

const TODOS_LS = "toDos";

function paintToDo(text) {
  const li = document.createElement("li");
  const delBtn = document.createElement("button");
  const span = document.createElement("span")
  delBtn.innerText = "❌";
  span.innerText = text;
  li.appendChild(delBtn);
  li.appendChild(span);
  toDOList.appendChild(li);
}

function loadToDos() {
  const toDos = localStorage.getItem(TODOS_LS);
  if (!toDos) {

  }
}

function handleSubmit(event) {
  event.preventDefault();
  const currentValue = toDoInput.value;
  toDoInput.value = ""
  paintToDo(currentValue);
  console.log(currentValue)
}

function init() {
  toDoForm.addEventListener("submit", handleSubmit);
}

init();