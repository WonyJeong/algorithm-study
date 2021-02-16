const clockContainer = document.querySelector(".js-clock");
const clockTitle = document.querySelector("h1");

const getTime = () => {
  const date = new Date();

  const hours = date.getHours();
  const minutes = date.getMinutes();

  const second = date.getSeconds();

  minutes_ = minutes < 10 ? "0" + minutes : minutes;
  second_ = second < 10 ? "0" + second : second;

  clockTitle.innerText = `${hours}:${minutes_}:${second_}`;
};

const init = () => {
  setInterval(() => {
    getTime();
  }, 1000);
};

init();
