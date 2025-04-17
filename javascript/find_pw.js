document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const idInput = document.getElementById("id");
  const emailInput = document.getElementById("email");

  form.addEventListener("submit", (e) => {
    const id = idInput.value.trim();
    const email = emailInput.value.trim();

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (id === "") {
      e.preventDefault();
      alert("아이디를 입력해주세요");
      return;
    }

    if (!emailRegex.test(email)) {
      e.preventDefault();
      alert("유효한 이메일 주소를 입력해주세요");
      return;
    }

    console.log("입력된 아이디:", id);
    console.log("입력된 이메일:", email);
  });
});
