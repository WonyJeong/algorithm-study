// window.addEventListener("resize", handleResize)
// 윈도우 사이즈가 변경될 때만!!!!! handleResize 함수 호출하자!!!
// handleResize()라고 적게 되면 지금 바로 함수를 호출하라는 의미

const title = document.querySelector("#title");
const CLICKED_CLASS = "clicked"

function handlieClicked() {
    const currentClassName = title.className;
    if (currentClassName !== CLICKED_CLASS) {
        title.className = CLICKED_CLASS;
    } else {
        title.className = "";
    }
}

function init() {
    title.addEventListener("click", handlieClicked);
}
init()

