// window.addEventListener("resize", handleResize)
// 윈도우 사이즈가 변경될 때만!!!!! handleResize 함수 호출하자!!!
// handleResize()라고 적게 되면 지금 바로 함수를 호출하라는 의미


//classList.add(A) : className에 A 덧붙여서 추가
//classList.remove(A) : className에 A 덧붙여진거 삭제
//classList.toggle(A) : className에 A 없으면 추가 있으면 삭제
//toggle do that if there is a class, remove the class from classList. Likewise, If there isnt a class, add the class to classList
const clockContainer = document.querySelector(".js-clock"),
    clockTitle = clockContainer.querySelector("h1");

function getTime(){
    const date = new Date();
    const minutes = date.getMinutes();
    const hours = date.getHours();
    const seconds = date.getSeconds();
    clockTitle.innerText = `${
        hours < 10 ? `0${hours}` : hours
    }:${
         minutes < 10 ? `0${minutes}` : minutes
    }:${
        seconds < 10? `0${seconds}` : seconds
    }`;
}

function init() {
    getTime();
    setInterval(getTime, 1000); // 매초마다 얻은 시간 표현
    // 함수() 이렇게 쓰는 부분에서 바로 호출
    // 함수 이렇게만 써놓으면 getTime()써질 때 1초마다 업데이트 하라는 뜻
}

init()
