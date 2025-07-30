Telegram.WebApp.ready();

function sendOrder(drink) {
  const order = { drink };
  Telegram.WebApp.sendData(JSON.stringify(order));
}
