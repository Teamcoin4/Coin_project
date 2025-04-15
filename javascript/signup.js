document.addEventListener("DOMContentLoaded", () => {
  const signupForm = document.querySelector('form[action="/signup"]');
  const usernameInput = document.getElementById("username");
  const checkUsernameBtn = document.querySelector('button[type="button"]');
  const passwordInput = document.getElementById("password");
  const confirmPasswordInput = document.getElementById("confirm_password");

  checkUsernameBtn.addEventListener("click", () => {
    const username = usernameInput.value.trim();

    if (!username) {
      alert("아이디를 입력해 주세요.");
      return;
    }

    alert("중복 확인 기능은 아직 구현되지 않았습니다.");
  });

  signupForm.addEventListener("submit", (e) => {
    const password = passwordInput.value;
    const confirmPassword = confirmPasswordInput.value;

    if (password !== confirmPassword) {
      e.preventDefault();
      alert("비밀번호가 일치하지 않습니다.");
      return;
    }
  });
});
