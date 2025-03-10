// DOM이 모두 로드된 뒤 실행
document.addEventListener("DOMContentLoaded", () => {
    // 탭 전환 기능
    const tabButtons = document.querySelectorAll(".tab-btn");
    const contentBoxes = document.querySelectorAll(".content-box");
  
    tabButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        // 모든 content-box에서 active 제거
        contentBoxes.forEach((box) => box.classList.remove("active"));
        // 클릭한 버튼에 해당하는 content-box만 active 추가
        const target = document.getElementById(btn.dataset.target);
        if (target) {
          target.classList.add("active");
        }
      });
    });
  
    // 예시: 로그인 버튼 클릭 시 login.html로 이동
    const loginBtn = document.getElementById("loginBtn");
    if (loginBtn) {
      loginBtn.addEventListener("click", () => {
        window.location.href = "login.html";
      });
    }
  
    // 검색 버튼 클릭 시 예시 기능
    const searchBtn = document.getElementById("searchBtn");
    if (searchBtn) {
      searchBtn.addEventListener("click", () => {
        const coinName = document.getElementById("coinSearch").value;
        alert(`'${coinName}'로 검색을 수행합니다(예시).`);
        // 실제로는 서버나 DB에서 검색 결과를 받아 아래 목록에 반영하는 로직 필요
      });
    }
  
    // 샘플 데이터 표시(실제론 서버나 DB에서 받아와서 표시)
    document.getElementById("total-assets").textContent = "10,000,000"; // 총 투자자산 예시
    document.getElementById("available-balance").textContent = "2,000,000"; // 예수금 예시
    document.getElementById("totalHoldings").textContent = "8,000,000"; // 총 보유자산 예시
    document.getElementById("krwBalance").textContent = "1,000,000"; // 보유 KRW 예시
  
    // 예시 거래내역
    const historyList = document.getElementById("historyList");
    if (historyList) {
      const sampleHistory = [
        { date: "2025-03-01", type: "매수", coin: "BTC", amount: 0.01 },
        { date: "2025-03-02", type: "매도", coin: "ETH", amount: 0.5 },
      ];
      sampleHistory.forEach((item) => {
        const li = document.createElement("li");
        li.textContent = `${item.date} | ${item.type} | ${item.coin} ${item.amount}`;
        historyList.appendChild(li);
      });
    }
  
    // 예시 미체결
    const openOrdersList = document.getElementById("openOrdersList");
    if (openOrdersList) {
      const sampleOpenOrders = [
        { date: "2025-03-03", type: "매수", coin: "XRP", amount: 100 },
      ];
      sampleOpenOrders.forEach((item) => {
        const li = document.createElement("li");
        li.textContent = `${item.date} | ${item.type} | ${item.coin} ${item.amount}`;
        openOrdersList.appendChild(li);
      });
    }
  
    // 예시 입출금대기
    const pendingDepositList = document.getElementById("pendingDepositList");
    if (pendingDepositList) {
      const samplePending = [
        { date: "2025-03-04", action: "출금대기", coin: "KRW", amount: 500000 },
      ];
      samplePending.forEach((item) => {
        const li = document.createElement("li");
        li.textContent = `${item.date} | ${item.action} | ${item.coin} ${item.amount}`;
        pendingDepositList.appendChild(li);
      });
    }
  
    // 예시 투자손익
    const profitLossList = document.getElementById("profitLossList");
    if (profitLossList) {
      const sampleProfitLoss = [
        { coin: "BTC", profit: 300000 },
        { coin: "ETH", profit: -50000 },
      ];
      sampleProfitLoss.forEach((item) => {
        const li = document.createElement("li");
        li.textContent = `${item.coin} | 손익: ${item.profit} KRW`;
        profitLossList.appendChild(li);
      });
    }
  
    // 예시 보유 코인 목록
    const coinHoldingsList = document.getElementById("coinHoldingsList");
    if (coinHoldingsList) {
      const sampleHoldings = [
        { coin: "BTC", amount: 0.05 },
        { coin: "ETH", amount: 1.2 },
        { coin: "XRP", amount: 500 },
      ];
      sampleHoldings.forEach((item) => {
        const li = document.createElement("li");
        li.textContent = `${item.coin} : ${item.amount}`;
        coinHoldingsList.appendChild(li);
      });
    }
  });
  