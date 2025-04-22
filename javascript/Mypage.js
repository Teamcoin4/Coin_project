// 닉네임 변경 버튼 클릭 이벤트
document.getElementById("btn-change-nickname").addEventListener("click", function() {
  const nicknameInput = document.getElementById("nickname");
  const newNickname = nicknameInput.value.trim();
  
  if (newNickname) {
    alert(`닉네임이 "${newNickname}"(으)로 변경되었습니다.`);
    // 실제 로직에서는 서버로 닉네임 변경 요청 등을 처리
  } else {
    alert("닉네임을 입력해주세요.");
  }
});

// 비밀번호 수정 버튼 클릭 이벤트
document.getElementById("btn-change-password").addEventListener("click", function() {
  // 실제 로직에서는 비밀번호 수정 페이지로 이동 or 팝업 표시 등
  alert("비밀번호 수정 페이지로 이동합니다(예시).");
});

// 계정 상태 토글 버튼
document.getElementById("btn-account-toggle").addEventListener("click", function() {
  // 예시로 버튼 텍스트만 '활성화 하기' ↔ '비활성화 하기'로 바꿔 봅니다.
  if (this.textContent === "활성화 하기") {
    this.textContent = "비활성화 하기";
    alert("계정이 활성화되었습니다.");
  } else {
    this.textContent = "활성화 하기";
    alert("계정이 비활성화되었습니다.");
  }
});
