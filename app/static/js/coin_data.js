let interval = null;

function fetch_coin_data() {
    console.log("running fetch_coin_data")
    function fetch_data() {
      fetch('/coin_value')
      .then(response => response.json())
      .then(data=> {
        document.getElementById('value').innerText = data.value;})
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    }
    if (!interval) {
      interval = setInterval(fetch_data, 5000);
    }
}

function coin_trade_request(){
  const amount = document.getElementById('amount')
  const price = document.getElementById('price')
  const coin_name = document.getElementById("coin-name")
  let trade_type = document.getElementById("trade-action")

  if (type.value == "매수"){
    trade_type = "buy";
  } else if (type.value == "매도"){
    trade_type = "sell";
  }

  fetch("trade_request", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      coin_name: coin_name.value,
      coin_price: price.value,
      coin_amount: amount.value,
      trade_type : trade_type
    })
  })
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Network response was not ok');
    }
  })
}



/*function persentage_amount() {
    const amount = document.getElementById('amount').value;
    const value = document.getElementById('value').innerText;
    const total = parseFloat(amount) * parseFloat(value);
    document.getElementById('total').innerText = total.toFixed(2);
}*/