function loadDoc(){
    var xhttp;
    /*
    if (window.XMLHttpRequest) { //code for firefox, chrome, safari ... any other browsers
        xhttp = new XMLHttpRequest();
    } else { // code for IE 8 before
        xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    */
   xhttp = new XMLHttpRequest(); //서버에 통신을 보내겠다
   //서버에 요청을 보내고 온 반응(상태) onreadyStateChange를 통해 확인한다
   xhttp.onreadystatechange = function() {
        // request에 대한 처리가 끝났고 브라우저로 보낼 반응이 준비됨

        console.log(`readyStaete ${this.readyState}`);
        console.log(`status ${this.status}`);
        if(this.readyState == 4 && this.status == 200) {// 서버준비, XMLHttpRequest 응답했음
            document.querySelector(".demo").innerHTML = this.responseText;
            //A.innerHTML = B (js)  A.html(B) (jquery)
        }

         // 서버준비안됨. XMLHttpRequest 응답받지 못함.
   } //onreadystatechange
   xhttp.open('get', 'ajax_info.txt', true);
   xhttp.send();

} //loadDoc

