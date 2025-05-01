<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Robo dos Criativos</title>
<style>
  body {
    background: #101820FF;
    color: #FEE715FF;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    flex-direction: column;
    height: 100vh;
    margin: 0;
  }
  header {
    background: #FEE715FF;
    color: #101820FF;
    padding: 1rem;
    text-align: center;
    font-size: 1.8rem;
    font-weight: bold;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  }
  #chat-container {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
    background: #1F2833FF;
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
    border-radius: 8px;
    margin: 1rem;
  }
  .message {
    padding: 0.6rem 1rem;
    border-radius: 20px;
    max-width: 60%;
    line-height: 1.3;
    word-wrap: break-word;
    font-size: 1rem;
  }
  .user-message {
    background-color: #45A29EFF;
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 2px;
  }
  .bot-message {
    background-color: #66FCF1FF;
    color: #0B0C10FF;
    align-self: flex-start;
    border-bottom-left-radius: 2px;
  }
  footer {
    display: flex;
    padding: 1rem;
    background: #0B0C10FF;
    gap: 0.5rem;
  }
  input[type="text"] {
    flex: 1;
    padding: 0.7rem 1rem;
    border-radius: 9999px;
    border: none;
    font-size: 1rem;
    outline: none;
  }
  button {
    background: #FEE715FF;
    color: #101820FF;
    border: none;
    padding: 0 1.5rem;
    border-radius: 9999px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }
  button:hover {
    background-color: #FFD633FF;
  }
</style>
</head>
<body>
  <header>Robo dos Criativos</header>
  <div id="chat-container" aria-live="polite" aria-label="Área de conversa"></div>
  <footer>
    <input type="text" id="user-input" placeholder="Digite sua mensagem..." aria-label="Digite sua mensagem" />
    <button id="send-button" disabled>Enviar</button>
  </footer>
<script>
  const chatContainer = document.getElementById('chat-container');
  const userInput = document.getElementById('user-input');
  const sendButton = document.getElementById('send-button');

  userInput.addEventListener('input', () => {
    sendButton.disabled = userInput.value.trim() === '';
  });

  function appendMessage(text, className) {
    const msgDiv = document.createElement('div');
    msgDiv.textContent = text;
    msgDiv.className = 'message ' + className;
    chatContainer.appendChild(msgDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }

  async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;
    appendMessage(text, 'user-message');
    userInput.value = '';
    sendButton.disabled = true;
    try {
      const response = await fetch('/api/message', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: text}),
      });
      const data = await response.json();
      appendMessage(data.response, 'bot-message');
    } catch (e) {
      appendMessage('Erro na comunicação com o servidor.', 'bot-message');
    }
  }

  sendButton.addEventListener('click', sendMessage);
  userInput.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !sendButton.disabled) {
      sendMessage();
    }
  });

  appendMessage('Olá! Eu sou o Robo dos Criativos. Como posso te ajudar?', 'bot-message');
</script>
</body>
</html>