// DOM이 모두 로드된 뒤 실행
document.addEventListener("DOMContentLoaded", () => {
  // 탭 전환 기능
  const tabButtons = document.querySelectorAll(".tab-btn");
  const contentBoxes = document.querySelectorAll(".content-box");

  tabButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      contentBoxes.forEach((box) => box.classList.remove("active"));
      const target = document.getElementById(btn.dataset.target);
      if (target) target.classList.add("active");
    });
  });

  const loginBtn = document.getElementById("loginBtn");
  if (loginBtn) {
    loginBtn.addEventListener("click", () => {
      window.location.href = "login.html";
    });
  }

  const searchBtn = document.getElementById("searchBtn");
  if (searchBtn) {
    searchBtn.addEventListener("click", () => {
      const coinName = document.getElementById("coinSearch").value;
      alert(`'${coinName}'로 검색을 수행합니다(예시).`);
    });
  }

  // 예시 데이터 주석 처리
  /*
  document.getElementById("total-assets").textContent = "10,000,000";
  document.getElementById("available-balance").textContent = "2,000,000";
  document.getElementById("totalHoldings").textContent = "8,000,000";
  document.getElementById("krwBalance").textContent = "1,000,000";

  const sampleHistory = [
    { date: "2025-03-01", type: "매수", coin: "BTC", amount: 0.01 },
    { date: "2025-03-02", type: "매도", coin: "ETH", amount: 0.5 },
  ];
  const historyList = document.getElementById("historyList");
  sampleHistory.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.date} | ${item.type} | ${item.coin} ${item.amount}`;
    historyList.appendChild(li);
  });

  const sampleOpenOrders = [
    { date: "2025-03-03", type: "매수", coin: "XRP", amount: 100 },
  ];
  const openOrdersList = document.getElementById("openOrdersList");
  sampleOpenOrders.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.date} | ${item.type} | ${item.coin} ${item.amount}`;
    openOrdersList.appendChild(li);
  });

  const samplePending = [
    { date: "2025-03-04", action: "출금대기", coin: "KRW", amount: 500000 },
  ];
  const pendingDepositList = document.getElementById("pendingDepositList");
  samplePending.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.date} | ${item.action} | ${item.coin} ${item.amount}`;
    pendingDepositList.appendChild(li);
  });

  const sampleProfitLoss = [
    { coin: "BTC", profit: 300000 },
    { coin: "ETH", profit: -50000 },
  ];
  const profitLossList = document.getElementById("profitLossList");
  sampleProfitLoss.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.coin} | 손익: ${item.profit} KRW`;
    profitLossList.appendChild(li);
  });

  const sampleHoldings = [
    { coin: "BTC", amount: 0.05 },
    { coin: "ETH", amount: 1.2 },
    { coin: "XRP", amount: 500 },
  ];
  const coinHoldingsList = document.getElementById("coinHoldingsList");
  sampleHoldings.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.coin} : ${item.amount}`;
    coinHoldingsList.appendChild(li);
  });
  */
});

// 샘플 데이터 주석 처리
/*
const sampleData = [
  { time_close: "2025-01-01", open: 49500, high: 50800, low: 49300, close: 50000 },
  ...
];
const coinListData = [
  { name: "비트코인", price: 59823, change: 2.34, volume: 12456.78 },
  ...
];
*/

// 빈 배열로 대체 (초기 렌더링 방지)
const sampleData = [];
const coinListData = [];

// 차트 기본 옵션 (빈 데이터)
const options = {
  series: [{
    data: []
  }],
  chart: {
    type: 'candlestick',
    height: 500,
    toolbar: { tools: {} },
    background: 'transparent'
  },
  theme: { mode: "dark" },
  grid: { show: false },
  plotOptions: {
    candlestick: { wick: { useFillColor: true } }
  },
  xaxis: {
    labels: { show: false },
    type: 'datetime',
    categories: [],
    axisBorder: { show: false },
    axisTicks: { show: false }
  },
  yaxis: { show: false },
  tooltip: {
    y: {
      formatter: v => `$ ${v.toFixed(2)}`
    }
  }
};

const miniOptions = {
  series: [{
    name: "가격",
    data: []
  }],
  chart: {
    type: 'area',
    height: 150,
    toolbar: { show: false },
    background: 'transparent'
  },
  stroke: {
    curve: 'smooth',
    width: 2
  },
  fill: {
    type: 'gradient',
    gradient: {
      shadeIntensity: 1,
      opacityFrom: 0.7,
      opacityTo: 0.3,
      stops: [0, 100]
    }
  },
  grid: { show: false },
  xaxis: {
    type: 'datetime',
    categories: [],
    labels: { show: false },
    axisBorder: { show: false },
    axisTicks: { show: false }
  },
  yaxis: { show: false },
  tooltip: {
    y: {
      formatter: val => '$' + val.toFixed(2)
    },
    theme: 'dark'
  },
  colors: ['#007bff']
};

// 차트 생성
document.addEventListener('DOMContentLoaded', function () {
  const chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();

  const miniChart = new ApexCharts(document.querySelector("#mini-chart"), miniOptions);
  miniChart.render();

  // 테이블 초기화
  const coinListBody = document.getElementById('coin-list-body');
  if (coinListBody) coinListBody.innerHTML = '';

  // 거래창
  const priceInput = document.querySelector('.input-group input[placeholder="금액 입력"]');
  const quantityInput = document.querySelector('.input-group input[placeholder="직접 입력"]');
  const totalInput = document.querySelector('.input-group input[disabled]');

  function calculateTotal() {
    const price = parseFloat(priceInput.value) || 0;
    const quantity = parseFloat(quantityInput.value) || 0;
    totalInput.value = (price * quantity).toLocaleString() + ' 원';
  }

  priceInput.addEventListener('input', calculateTotal);
  quantityInput.addEventListener('input', calculateTotal);

  const buyBtn = document.querySelector('.buy-btn');
  const sellBtn = document.querySelector('.sell-btn');
  const tradeActionBtn = document.querySelector('.trade-action');

  buyBtn.addEventListener('click', function () {
    buyBtn.style.opacity = '1';
    sellBtn.style.opacity = '0.5';
    tradeActionBtn.textContent = '매수';
  });

  sellBtn.addEventListener('click', function () {
    sellBtn.style.opacity = '1';
    buyBtn.style.opacity = '0.5';
    tradeActionBtn.textContent = '매도';
  });

  buyBtn.style.opacity = '1';
  sellBtn.style.opacity = '0.5';
  tradeActionBtn.textContent = '매수';

  const percentButtons = document.querySelectorAll('.percentage-buttons button');
  percentButtons.forEach(btn => {
    btn.addEventListener('click', function () {
      const percent = parseInt(btn.textContent) / 100;
      const maxQuantity = 1.0; // 실제 로직에서 대체
      quantityInput.value = (maxQuantity * percent).toFixed(4);
      calculateTotal();
    });
  });

  const minusBtn = document.querySelector('.adjust-buttons button:first-child');
  const plusBtn = document.querySelector('.adjust-buttons button:last-child');

  minusBtn.addEventListener('click', function () {
    const currentPrice = parseFloat(priceInput.value) || 0;
    priceInput.value = Math.max(0, currentPrice - 100).toString();
    calculateTotal();
  });

  plusBtn.addEventListener('click', function () {
    const currentPrice = parseFloat(priceInput.value) || 0;
    priceInput.value = (currentPrice + 100).toString();
    calculateTotal();
  });

  calculateTotal();
});
