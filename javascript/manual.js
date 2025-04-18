document.addEventListener("DOMContentLoaded", () => {
  const priceInput = document.querySelector('input[placeholder="금액"]');
  const quantityInput = document.querySelector(
    '.percent-buttons input[type="text"]'
  );
  const totalInput = document.querySelectorAll('input[type="text"]')[2];
  const minusBtn = document.querySelectorAll(".form-group button")[0];
  const plusBtn = document.querySelectorAll(".form-group button")[1];
  const percentBtns = document.querySelectorAll(".percent-buttons button");
  const buyBtn = document.querySelectorAll(".action-btn")[0];
  const sellBtn = document.querySelectorAll(".action-btn")[1];

  const holdingAmount = 1000000;

  minusBtn.addEventListener("click", () => {
    const current = parseFloat(priceInput.value) || 0;
    priceInput.value = Math.max(current - 100, 0).toFixed(0);
    updateTotal();
  });

  plusBtn.addEventListener("click", () => {
    let price = parseFloat(priceInput.value) || 0;
    price += 100;
    priceInput.value = price.toFixed(0);
    updateTotal();
  });

  percentBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const percent = parseFloat(btn.textContent) / 100;
      const price = parseFloat(priceInput.value);
      if (!price || price <= 0) return alert("가격을 먼저 입력하세요.");
      const quantity = (holdingAmount * percent) / price;
      quantityInput.value = quantity.toFixed(4);
      updateTotal();
    });
  });

  priceInput.addEventListener("input", updateTotal);
  quantityInput.addEventListener("input", updateTotal);

  function updateTotal() {
    const price = parseFloat(priceInput.value) || 0;
    const quantity = parseFloat(quantityInput.value) || 0;
    const total = price * quantity;
    totalInput.value = total.toFixed(2);
  }

  buyBtn.addEventListener("click", () => {
    const price = priceInput.value;
    const quantity = quantityInput.value;
    const total = totalInput.value;
    alert(`매수 주문:\n가격: ${price}, 수량: ${quantity}, 총액 ${total}`);
  });

  sellBtn.addEventListener("click", () => {
    const price = priceInput.value;
    const quantity = quantityInput.value;
    const total = totalInput.value;
    alert(`매도 주문:\n가격: ${price}, 수량: ${quantity}, 총액 ${total}`);
  });
});
