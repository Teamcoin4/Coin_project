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


  // 샘플 데이터 - 캔들스틱 차트용
const sampleData = [
  { time_close: "2025-01-01", open: 49500, high: 50800, low: 49300, close: 50000 },
  { time_close: "2025-01-02", open: 50100, high: 51500, low: 50000, close: 51200 },
  { time_close: "2025-01-03", open: 51300, high: 52700, low: 51000, close: 52500 },
  { time_close: "2025-01-04", open: 52600, high: 53500, low: 52200, close: 53000 },
  { time_close: "2025-01-05", open: 53100, high: 53200, low: 51500, close: 51800 },
  { time_close: "2025-01-06", open: 51900, high: 53000, low: 51700, close: 52700 },
  { time_close: "2025-01-07", open: 52800, high: 54500, low: 52600, close: 54200 },
  { time_close: "2025-01-08", open: 54300, high: 55300, low: 53900, close: 55100 },
  { time_close: "2025-01-09", open: 55200, high: 55400, low: 54000, close: 54500 },
  { time_close: "2025-01-10", open: 54600, high: 56300, low: 54400, close: 56000 },
  { time_close: "2025-01-11", open: 56100, high: 57500, low: 55800, close: 57200 },
  { time_close: "2025-01-12", open: 57300, high: 58600, low: 57100, close: 58400 },
  { time_close: "2025-01-13", open: 58500, high: 58700, low: 57400, close: 57800 },
  { time_close: "2025-01-14", open: 57900, high: 59400, low: 57700, close: 59100 },
  { time_close: "2025-01-15", open: 59200, high: 60100, low: 59000, close: 59800 },
];

// 코인 목록 데이터
const coinListData = [
  { name: "비트코인", price: 59823, change: 2.34, volume: 12456.78 },
  { name: "이더리움", price: 3256, change: 1.25, volume: 8549.32 },
  { name: "리플", price: 0.52, change: -0.75, volume: 4852.16 },
  { name: "라이트코인", price: 189.45, change: 0.88, volume: 2154.96 },
  { name: "도지코인", price: 0.08, change: 5.23, volume: 9621.45 },
  { name: "카르다노", price: 0.46, change: -1.32, volume: 3256.78 },
  { name: "폴카닷", price: 5.87, change: 0.54, volume: 1895.34 },
  { name: "솔라나", price: 119.45, change: 3.67, volume: 5632.12 }
];

// 메인 차트 설정 (캔들스틱 차트로 변경)
const options = {
  series: [{
    data: sampleData.map(price => ({
      x: price.time_close,
      y: [price.open, price.high, price.low, price.close],
    }))
  }],
  chart: {
    type: 'candlestick',
    height: 500,
    toolbar: {
      tools: {}
    },
    background: 'transparent'
  },
  theme: {
    mode: "dark"
  },
  grid: {
    show: false
  },
  plotOptions: {
    candlestick: {
      wick: {
        useFillColor: true
      }
    }
  },
  xaxis: {
    labels: {
      show: false,
      datetimeFormatter: {
        month: "mmm 'yy"
      }
    },
    type: 'datetime',
    categories: sampleData.map(date => date.time_close),
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false
    }
  },
  yaxis: {
    show: false
  },
  tooltip: {
    y: {
      formatter: v => `$ ${v.toFixed(2)}`
    }
  }
};

// 미니 차트 설정 (간단한 영역 차트 유지)
const miniOptions = {
  series: [{
    name: "가격",
    data: sampleData.slice(-7).map(price => Number(price.close))
  }],
  chart: {
    type: 'area',
    height: 150,
    toolbar: {
      show: false
    },
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
  grid: {
    show: false
  },
  xaxis: {
    type: 'datetime',
    categories: sampleData.slice(-7).map(date => date.time_close),
    labels: {
      show: false
    },
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false
    }
  },
  yaxis: {
    show: false
  },
  tooltip: {
    y: {
      formatter: function(val) {
        return '$' + val.toFixed(2);
      }
    },
    theme: 'dark'
  },
  colors: ['#007bff']
};

// 차트 생성 및 이벤트 처리
document.addEventListener('DOMContentLoaded', function() {
  const chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();
  
  const miniChart = new ApexCharts(document.querySelector("#mini-chart"), miniOptions);
  miniChart.render();
  
  // 코인 목록 채우기
  const coinListBody = document.getElementById('coin-list-body');
  
  coinListData.forEach(coin => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${coin.name}</td>
      <td>$${coin.price.toLocaleString()}</td>
      <td class="${coin.change >= 0 ? 'positive-change' : 'negative-change'}">${coin.change >= 0 ? '+' : ''}${coin.change}%</td>
      <td>${coin.volume.toLocaleString()}</td>
    `;
    coinListBody.appendChild(row);
    
    // 행 클릭 이벤트 추가
    row.style.cursor = 'pointer';
    row.addEventListener('click', function() {
      document.querySelector('.coin-graph h1').textContent = `${coin.name} 차트`;
    });
  });
  
  // 가격 및 수량 입력에 따른 총액 계산
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
  
  // 버튼 클릭 이벤트
  const buyBtn = document.querySelector('.buy-btn');
  const sellBtn = document.querySelector('.sell-btn');
  const tradeActionBtn = document.querySelector('.trade-action');
  
  buyBtn.addEventListener('click', function() {
    buyBtn.style.opacity = '1';
    sellBtn.style.opacity = '0.5';
    tradeActionBtn.textContent = '매수';
  });
  
  sellBtn.addEventListener('click', function() {
    sellBtn.style.opacity = '1';
    buyBtn.style.opacity = '0.5';
    tradeActionBtn.textContent = '매도';
  });
  
  // 기본값 설정
  buyBtn.style.opacity = '1';
  sellBtn.style.opacity = '0.5';
  tradeActionBtn.textContent = '매수';
  
  // 퍼센트 버튼 이벤트
  const percentButtons = document.querySelectorAll('.percentage-buttons button');
  percentButtons.forEach(btn => {
    btn.addEventListener('click', function() {
      const percent = parseInt(btn.textContent) / 100;
      // 실제 구현에서는 보유 자산 정보를 기반으로 계산
      const maxQuantity = 1.0; // 예시: 최대 구매 가능 코인 수량
      quantityInput.value = (maxQuantity * percent).toFixed(4);
      calculateTotal();
    });
  });
  
  // +/- 버튼 이벤트
  const minusBtn = document.querySelector('.adjust-buttons button:first-child');
  const plusBtn = document.querySelector('.adjust-buttons button:last-child');
  
  minusBtn.addEventListener('click', function() {
    const currentPrice = parseFloat(priceInput.value) || 0;
    priceInput.value = Math.max(0, currentPrice - 100).toString();
    calculateTotal();
  });
  
  plusBtn.addEventListener('click', function() {
    const currentPrice = parseFloat(priceInput.value) || 0;
    priceInput.value = (currentPrice + 100).toString();
    calculateTotal();
  });
  
  // 초기 총액 계산
  calculateTotal();
});