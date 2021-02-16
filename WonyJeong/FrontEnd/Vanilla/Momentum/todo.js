const toDoForm = document.querySelector(".js-toDoForm");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.querySelector(".js-toDoList");

const TODOS_LS = "toDos";

let toDos = [];

const deleteToDo = (event) => {
  const btn = event.target;
  const li = btn.parentNode;
  toDoList.removeChild(li);
  const cleanToDos = toDos.filter((item) => item.id !== parseInt(li.id));
  toDos = cleanToDos;
  saveToDos();
};

const saveToDos = () => {
  localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
};

const paintToDo = (text) => {
  const li = document.createElement("li");
  const span = document.createElement("span");
  const delBtn = document.createElement("button");
  const newId = toDos.length;
  span.innerText = text;
  delBtn.innerText = "X";
  delBtn.addEventListener("click", deleteToDo);

  li.appendChild(span);
  li.appendChild(delBtn);
  toDoList.appendChild(li);

  li.id = newId;

  const toDoObj = {
    id: newId,
    text,
  };

  toDos.push(toDoObj);
  saveToDos();
};

const handleTodoSubmit = (event) => {
  event.preventDefault();
  const currentValue = toDoInput.value;
  paintToDo(currentValue);
};

const loadToDos = () => {
  const loadedToDos = localStorage.getItem(TODOS_LS);
  if (loadedToDos !== null) {
    const parsed = JSON.parse(loadedToDos);
    parsed.forEach((item) => {
      paintToDo(item.text);
    });
  }
};

const initTodo = () => {
  loadToDos();
  toDoForm.addEventListener("submit", handleTodoSubmit);
};

initTodo();
