// window.addEventListener("resize", handleResize)
// 윈도우 사이즈가 변경될 때만!!!!! handleResize 함수 호출하자!!!
// handleResize()라고 적게 되면 지금 바로 함수를 호출하라는 의미

//classList.add(A) : className에 A 덧붙여서 추가
//classList.remove(A) : className에 A 덧붙여진거 삭제
//classList.toggle(A) : className에 A 없으면 추가 있으면 삭제
//toggle do that if there is a class, remove the class from classList. Likewise, If there isnt a class, add the class to classList

const title = document.querySelector("#title");
const CLICKED_CLASS = "clicked"

function handlieClicked() {
    title.classList.toggle(CLICKED_CLASS)
}

function init() {
    title.addEventListener("click", handlieClicked);
}
init()

