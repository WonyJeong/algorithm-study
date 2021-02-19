$("#btnEx2").click(()=>{
    console.log("123")
    data = {
        id : 0,
        stockCode:$("#stockCode").val(),
        stockName:$("#stockName").val(),
        stockPrice:$("#stockPrice").val() + 0.0,
        stockEstimatePrice:$("#stockEstimatePrice").val() + 0.0
    }
    console.log(data)
   $.ajax({
        type : 'post',
        data : data,
        url : `http://localhost/stockList/`,
        success : (response, status)=>{
            console.log(response)
        },
        error : (error) =>{}
   }) 
})

})