window.onload = () => {
  const table = document.querySelector("#ex1Answer");
  const btnAdd = document.querySelector("#btnEx2");
  const ipCode = document.querySelector("#stockCode");
  const ipName = document.querySelector("#stockName");
  const ipPrice = document.querySelector("#stockPrice");
  const ipEsti = document.querySelector("#stockEstimatePrice");
  let stockerList = [];

  const postData = () => {
    const newItem = {
      stockCode: ipCode.value,
      stockName: ipName.value,
      stockPrice: ipPrice.value,
      stockEstimatePrice: ipEsti.value,
    };
    fetch("http://localhost/stockList", {
      method: "POST",
      headers: {
        "Content-Type": "application/json;charset=utf-8",
      },
      body: JSON.stringify(newItem),
    }).then(async (res) => {
      console.log(await res.json());
    });
  };

  const addTable = () => {
    stockerList.map((item) => {
      const tr = document.createElement("tr");
      const td1 = document.createElement("td");
      const td2 = document.createElement("td");
      const td3 = document.createElement("td");
      const td4 = document.createElement("td");
      td1.innerText = item.stockCode;
      td2.innerText = item.stockName;
      td3.innerText = item.stockPrice;
      td3.innerText = item.stockEstimatePrice;
      tr.append(td1);
      tr.append(td2);
      tr.append(td3);
      tr.append(td4);
      table.append(tr);
    });
  };

  const getDate = () => {
    fetch("http://localhost/stockList")
      .then(async (res) => {
        if (res.status === 200) {
          let json = await res.json();
          json.map((item) => {
            stockerList.push({
              stockCode: item.stockCode,
              stockName: item.stockName,
              stockPrice: item.stockPrice,
              stockEstimatePrice: item.stockEstimatePrice,
            });
          });
        } else {
          throw new Error(res.status);
        }
      })
      .then(() => {
        addTable();
      })
      .catch((err) => {
        console.log("에러가 발생했습니다. ", err);
      });
  };

  const init = () => {
    btnAdd.addEventListener("click", postData);
    getDate();
  };

  init();
};
