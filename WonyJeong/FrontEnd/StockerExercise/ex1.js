$("#btnEx1").click(() => {
  const stockCode = $("#inputEx1").val();
  if (stockCode !== null) {
    $.ajax({
      type: "get",
      dataType: "jsonp",
      jsonpCallback: "callback",
      url: `http://localhost/stockList/?stockCode=${stockCode}`,
      success: (data, status) => {
        let answerContainer = document.querySelector("#ex1Answer");
        const response = data[0];
        const stockItem = [
          response.stockCode,
          response.stockName,
          response.stockEstimatePrice,
          response.stockPrice,
        ];
        let tr = document.createElement("tr");
        stockItem.map((item) => {
          let td = document.createElement("td");
          td.innerText = item;
          tr.append(td);
          answerContainer.append(tr);
        });
      },
      error: (error) => {
        if (error.status === 404) {
          console.log("404 ERROR!");
        }
      },
    });
  }
});
