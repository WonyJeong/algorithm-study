//https://www.youtube.com/watch?v=rJesac0_Ftw
let buttonclicked = 1
const animalContainer = document.querySelector(".animal-info")
const btn = document.querySelector(".btn");
btn.addEventListener("click", function(){
    var xhttp = new XMLHttpRequest();
    const url = `https://learnwebcode.github.io/json-example/animals-${buttonclicked}.json`;
    
    xhttp.open('GET', url, true);

    // console.log(xhttp.status);

    // const parseData = JSON.parse(xhttp.responseText);
    //load되면 뭐해야되는지
    xhttp.onload = function() {
        if (xhttp.status >= 200 && xhttp.statusText < 400){
            const data = JSON.parse(xhttp.responseText);
            // console.log(data[0]);
            renderHTML(data);
        } else {
            console.log("We connected to the server, but it returned an error.")
        }
    };

    xhttp.onerror = function(){
        console.log("Connection error");
    }


    xhttp.send();
    buttonclicked++;
    if (buttonclicked > 3) {
        btn.classList.add("hide-me");
    }
});

function renderHTML(data) {
    let htmlString = "";

    for (i = 0; i < data.length; i++) {
        htmlString += `<p> ${data[i].name} is a ${data[i].species} that likes to eat.`;
        for (j = 0; j < data[i].foods.likes.length; j++){
            if (j == 0){
                htmlString += `${data[i].foods.likes[j]}`;
            } else {
                htmlString += ` and ${data[i].foods.likes[j]}`;
            }
        }


        htmlString += ` and dislikes `

        for (j = 0; j < data[i].foods.dislikes.length; j++){
            if (j == 0){
                htmlString += `${data[i].foods.dislikes[j]}`;
            } else {
                htmlString += ` and ${data[i].foods.dislikes[j]}`;
            }
        }

        htmlString += `.</p>`
    }
    animalContainer.insertAdjacentHTML('beforeend', htmlString);
}

