window.onload = () => {
    var btnSignin = document.getElementById("btnSignin");
    btnSignin.addEventListener("click", () => {
      const id = document.querySelector("#loginId");
      const pw = document.querySelector("#loginPw");
      
      const idVal = id.value;
      const pwVal = pw.value;
      fetch("http://localhost/user/" + idVal)
        .then((response) => {
          if (response.status == 200) {
            return response.json();
          } else {
            throw new error(response.status);
          }
        })
        .then((result) => {
          if (result.pw == pwVal) {
            alert("로그인 성공");
            id.value = "";
            pw.value = "";
          } else {
            alert("비밀번호 확인");
            pw.value = "";
          }
        })
        .catch((error) => {
          alert("아이디가 존재하지 않습니다.");
          id.value = "";
          pw.value = "";
        });
    });
    
    var duplicatedId = document.querySelector("#duplicatedId");
    duplicatedId.addEventListener("click", () => {
      const id = document.querySelector("#registerId");
      fetch("http://localhost/user/" + id.value)
        .then((response) => {
          if(response.status == 200){
            alert("이미 아이디가 존재 ㅋ")
            id.value = ""
          }else{
            throw new error(response.status)
          }
        }).catch((error) => {
          alert("아이디 사용가능 ㅋ");
          btnSignup.hidden = false
        })
    });
    var btnSignup = document.querySelector("#btnSignup");
    btnSignup.addEventListener("click", () => {
      const id = document.querySelector("#registerId")
      const pw = document.querySelector("#registerPw")
      const pwch = document.querySelector("#registerPwCh")
      if(pw.value && pw.value == pwch.value){
        fetch("http://localhost/user", {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json; charset=UTF-8'
          },
          body: JSON.stringify({id:id.value, pw: pw.value}),
      }).then((response) => {
        alert("회원가입 완료")
        id.value = ""
        pw.value = ""
        pwch.value = ""
        btnSignup.hidden = true
      })
      }else{
        if(!pw.value){
          alert("비밀번호를 입력하세요.")
        }else{
          alert("비밀번호가 일치하지 않습니다.")
        }
        pw.value = ""
        pwch.value = ""
      }
    })
  };