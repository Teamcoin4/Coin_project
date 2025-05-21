function submitNickname() {
    const nickname = document.getElementById('nickname').value;
    const regex = /^[a-zA-Z0-9가-힣]{3,15}$/;
  
    if (!regex.test(nickname)) {
      alert("닉네임은 3~15자 이내의 문자와 숫자만 사용할 수 있습니다.");
      return;
    }
  
    alert("닉네임이 변경되었습니다: " + nickname);
    // 이후 서버로 전송하거나 다른 작업 수행
  }
  