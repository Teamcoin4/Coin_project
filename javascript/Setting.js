
// 1) 예산 초기화 기능
const budgetValue = document.getElementById("budgetValue");
const resetBudgetBtn = document.getElementById("resetBudgetBtn");

resetBudgetBtn.addEventListener("click", () => {
  // 실제 로직에 맞게 예산을 재설정
  budgetValue.textContent = "0";
  alert("예산이 초기화되었습니다.");
});

// 2) 언어 변경 기능
const languageValue = document.getElementById("languageValue");
const changeLanguageBtn = document.getElementById("changeLanguageBtn");

changeLanguageBtn.addEventListener("click", () => {
  // 실제 로직에 맞게 언어를 변경
  if (languageValue.textContent === "Korean") {
    languageValue.textContent = "English";
  } else {
    languageValue.textContent = "Korean";
  }
  alert(`언어가 ${languageValue.textContent}로 변경되었습니다.`);
});

// 3) 모드 변경 기능
const modeValue = document.getElementById("modeValue");
const changeModeBtn = document.getElementById("changeModeBtn");

changeModeBtn.addEventListener("click", () => {
  // 실제 로직에 맞게 모드를 변경
  if (modeValue.textContent === "○○모드") {
    modeValue.textContent = "▲▲모드";
  } else {
    modeValue.textContent = "○○모드";
  }
  alert(`모드가 ${modeValue.textContent}로 변경되었습니다.`);
});
