document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const userId = document.getElementById("userId");
  const password = document.getElementById("password");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    if (userId.value.trim() === "" || password.value.trim() === "") {
      alert("아이디와 비밀번호를 모두 입력해주세요");
      return;
    }

    console.log("아이디:", userId.value);
    console.log("비밀번호:", password.value);

    alert("로그인 성공!");

    userId.addEventListener("focus", () => {
      userId.style.borderColor = "#ccc";
    });

    password.addEventListener("focus", () => {
      password.style.borderColor = "#ccc";
    });
  });
});
