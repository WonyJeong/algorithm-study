const search = document.querySelector(".search");
const send = document.querySelector(".send");

const div2 = document.querySelector(".exercise2")
const save = div2.querySelector(".save"),
    stockName = div2.querySelector(".stockName"),
    stockCode = div2.querySelector(".stockCode"),
    stockPrice = div2.querySelector(".stockPrice"),
    stockEstimatePrice = div2.querySelector(".stockEstimatePrice");

send.addEventListener("click", function(){
    fetch(`http://localhost/stockList/?stockCode=${search.value}`).then(res => {
        console.log(res)
        return res.json()
    }).then(data => {
        console.log(data)
        const answerTable = document.querySelector(".answer1");
        const tr = document.createElement("tr");
        const stockList = [
            data[0].stockName,
            data[0].stockCode,
            data[0].stockPrice,
            data[0].stockEstimatePrice
        ]

        for (i=0; i<stockList.length; i++){
            const td = document.createElement("td")
            td.innerText = stockList[i]
            tr.appendChild(td)
        }

        answerTable.append(tr)

    }).catch(error => {
        console.log(error)
    })
})


function saveItem(){
    if (stockName.value != ""){   
        fetch('http://localhost/stockList/', {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({
            id : stockCode.value,
            'stockName' : stockName.value,
            'stockCode' : stockCode.value,
            'stockPrice' : parseFloat(stockPrice.value),
            'stockEstimatePrice' : parseFloat(stockEstimatePrice.value),
        }),
        }).then(res =>{
            console.log(res)
            return res.json()
        }).then(data =>{
            console.log(data)
        }).then(error => {
            console.log(error)
        })
    }else {
        alert("empty.....")
    }
}
save.addEventListener("click", saveItem)


// save.addEventListener("click", function(){



//     fetch('http://localhost/stockList/A000', {
//         method : 'PUT',
//         headers : {'Content-Type' : 'application/json'},
//         body : JSON.stringify({
//             id : stockCode.value,
//             'stockName' : stockName.value,
//             'stockCode' : stockCode.value,
//             'stockPrice' : parseFloat(stockPrice.value),
//             'stockEstimatePrice' : parseFloat(stockEstimatePrice.value),
//         }),
//     }).then(res =>{
//         console.log(res)
//         return res.json()
//     }).then(data =>{
//         console.log(data)
//     }).then(error => {
//         console.log(error)
//     })
// })
