function socialLoginPopup(provider) {
  const redirectUrl = '/main_page/';
  const loginUrl = `/accounts/${provider}/login/?next=${redirectUrl}`;

  const width = 500;
  const height = 600;
  const left = (screen.width / 2) - (width / 2);
  const top = (screen.height / 2) - (height / 2);

  const popup = window.open(
    loginUrl,
    `${provider}_login`,
    `width=${width},height=${height},top=${top},left=${left},resizable=yes,scrollbars=yes`
  );

  // ✅ 메시지 수신 처리
  window.addEventListener("message", function(event) {
    if (event.data === "social-login-success") {
      if (popup && !popup.closed) {
        popup.close();
      }
      window.location.href = redirectUrl;
    }
  });
}
