//https://www.youtube.com/watch?v=rJesac0_Ftw
var xhttp = new XMLHttpRequest();
const url = 'http://everysports.iptime.org:5000/home/estimatestock'
xhttp.open('GET', url, true)

// console.log(xhttp.status);

// const parseData = JSON.parse(xhttp.responseText);
//load되면 뭐해야되는지
xhttp.onload = function() {
    const data = JSON.parse(xhttp.responseText);
    console.log(data[0]);
};
xhttp.send();