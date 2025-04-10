document.addEventListener("DOMContentLoaded", () => {
  // 페이지 로딩이 완료된 후 실행
  const priceInput = document.querySelector(
    '.input-group input[placeholder="금액 입력"]'
  );
  const quantityInput = document.querySelector(
    '.input-group input[placeholder="직접 입력"]'
  );
  const totalInput = document.querySelector(".input-group input[disabled]");
  const adjustButtons = document.querySelectorAll(".adjust-buttons button");
  const percentButtons = document.querySelectorAll(
    ".percentage-buttons button"
  );
  const tradeButtons = document.querySelectorAll(".trade-buttons button");
  const tradeActionButton = document.querySelector(".trade-action");

  // 보유 금액 가정 (예시)
  const userBalance = 1000000;

  // 총액 계산 함수
  function updateTotal() {
    const price = parseFloat(priceInput.value) || 0;
    const quantity = parseFloat(quantityInput.value) || 0;
    totalInput.value = (price * quantity).toLocaleString();
  }

  // 가격 조정 버튼
  adjustButtons[0].addEventListener("click", () => {
    priceInput.value = Math.max(0, (parseFloat(priceInput.value) || 0) - 1);
    updateTotal();
  });

  adjustButtons[1].addEventListener("click", () => {
    priceInput.value = (parseFloat(priceInput.value) || 0) + 1;
    updateTotal();
  });

  // 퍼센트 버튼 클릭 시 수량 자동 입력
  percentButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const percentage = parseFloat(button.textContent) / 100;
      const price = parseFloat(priceInput.value) || 0;
      if (price > 0) {
        const amount = Math.floor((userBalance * percentage) / price);
        quantityInput.value = amount;
        updateTotal();
      }
    });
  });

  // 입력값 변경 시 총액 업데이트
  priceInput.addEventListener("input", updateTotal);
  quantityInput.addEventListener("input", updateTotal);

  // 매수/매도 버튼 클릭 시 동작
  tradeActionButton.addEventListener("click", () => {
    const action = document
      .querySelector(".buy-btn")
      .classList.contains("active")
      ? "매수"
      : "매도";
    alert(`${action} 주문이 접수되었습니다.`);
  });

  // 매수/매도 버튼 토글
  tradeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      tradeButtons.forEach((btn) => btn.classList.remove("active"));
      button.classList.add("active");
      tradeActionButton.textContent = button.textContent;
    });
  });

  // 미니 그래프 초기 렌더링 (Chart.js 필요)
  const ctx = document.getElementById("mini-graph").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: Array.from({ length: 10 }, (_, i) => `${i + 1}분`),
      datasets: [
        {
          label: "가격 변동",
          data: Array.from(
            { length: 10 },
            () => Math.floor(Math.random() * 1000) + 500
          ),
          borderColor: "#007bff",
          fill: false,
          tension: 0.3,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
      },
      scales: {
        x: { display: false },
        y: { display: false },
      },
    },
  });
});
