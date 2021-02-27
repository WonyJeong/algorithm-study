window.onload = () => {
  const ex1Answer = document.querySelector("#ex1Answer");
  const inputEx1 = document.querySelector("#inputEx1");
  const btnEx1 = document.querySelector("#btnEx1");

  const getStockItem = (prop) => {
    fetch(`http://localhost/stockList/?stockCode=${prop}`).then(async (res) => {
      const tr = document.createElement("tr");
      const item = await res.json();
      const td1 = document.createElement("td");
      const td2 = document.createElement("td");
      const td3 = document.createElement("td");
      const td4 = document.createElement("td");
      td1.innerText = item[0].stockCode;
      td2.innerText = item[0].stockName;
      td3.innerText = item[0].stockPrice;
      td4.innerText = item[0].stockEstimatePrice;
      tr.append(td1);
      tr.append(td2);
      tr.append(td3);
      tr.append(td4);
      ex1Answer.append(tr);
    });
  };

  const updateItem = (stockCode) => {
    const data = JSON.stringify({
      stockPrice: 123456,
      temp: 1,
    });
    fetch(`http://localhost/stockList/0`, {
      method: "put",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        stockCode,
        stockPrice: 123456,
      }),
    })
      .then(async (res) => {
        console.log(await res.json());
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const handleSendButton = () => {
    const stockCode = inputEx1.value;
    // getStockItem(stockCode);
    updateItem(stockCode);
  };

  const init = () => {
    btnEx1.addEventListener("click", () => {
      if (asd != "" && asdasd != "") {
        fetch().then().catch();
      }
    });
  };
  init();
};
