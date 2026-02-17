const form = document.getElementById("todoForm");
const input = document.getElementById("todoInput");
const list = document.getElementById("todoList");

function createTodoItem(text) {
  const li = document.createElement("li");
  li.className = "item";

  const left = document.createElement("div");
  left.className = "left";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.addEventListener("change", () => {
    li.classList.toggle("done", checkbox.checked);
  });

  const span = document.createElement("span");
  span.className = "task";
  span.textContent = text;

  const delBtn = document.createElement("button");
  delBtn.type = "button";
  delBtn.className = "delete-btn";
  delBtn.setAttribute("aria-label", "Delete task");
  delBtn.textContent = "🗑";
  delBtn.addEventListener("click", () => {
    list.removeChild(li);
  });

  left.appendChild(checkbox);
  left.appendChild(span);

  li.appendChild(left);
  li.appendChild(delBtn);

  return li;
}

function addTask(text) {
  const trimmed = text.trim();
  if (!trimmed) return;

  const item = createTodoItem(trimmed);
  list.appendChild(item);
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  addTask(input.value);
  input.value = "";
  input.focus();
});

// (опционально) стартовые элементы как на скрине
addTask("First item");
addTask("Second item");
addTask("Third item");
