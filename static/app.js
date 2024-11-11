class Chatbox {
  constructor() {
    this.args = {
      openButton: document.querySelector('.chatbox__button'),
      chatBox: document.querySelector('.chatbox__support'),
      sendButton: document.querySelector('.send__button'),
    }

    this.state = false;
    this.messages = [];
    this.socket = null;
  }

  display() {

    const {openButton, chatBox, sendButton} = this.args;

    openButton.addEventListener('click', () => this.toggleState(chatBox))

    sendButton.addEventListener('click', () => this.onSendButton(chatBox))

    const node = chatBox.querySelector('input');

    node.addEventListener("keyup", ({key}) => {
      if (key === "Enter") {
        this.onSendButton(chatBox)
      }
    })

    // Connect websocket. Comment below code out when using HTTP
    this.connectWebSocket();

  }

  // Using WebScockets
  connectWebSocket() {
    this.socket = new WebSocket(`${websocketUrl}/ws/query`);

    console.log(`Websocket url: ${websocketUrl}/ws/query`)
    this.socket.onopen = () => {
      console.log("WebSocket client connection established.");
    };

    this.socket.onmessage = (event) => {
      try {
        const response = JSON.parse(event.data).response;
        const msg2 = { name: "Rolando", message: response };
        this.messages.push(msg2);
        this.updateChatText(this.args.chatBox);
      } catch (error) {
        console.error("Error processing incoming message:", error);
      }
    };

    this.socket.onclose = () => {
      console.warn("WebSocket connection closed.");
      setTimeout(() => this.connectWebSocket(), 5000); // Reconnect after a delay
    };

    this.socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };
  }



  toggleState(chatBox) {
    this.state = !this.state;

    // show or hides the bot
    if (this.state) {
      chatBox.classList.add('chatbox--active')
    } else {
      chatBox.classList.remove('chatbox--active')
    }
  }

  // // Using HTTP
  // onSendButton(chatBox) {
  //   var textField = chatBox.querySelector('input');
  //   let text1 = textField.value
  //   if (text1 == "") {
  //     return;
  //   }

  //   let msg1 = {name: "User", message: text1}
  //   this.messages.push(msg1);

  //   console.log('Scriptroot: ', $SCRIPT_ROOT)

  //   // Using HTTP
  //   fetch('http://127.0.0.1:8000' + '/query', {
  //     method: 'POST',
  //     body: JSON.stringify({query: text1}),
  //     mode: 'cors',
  //     headers: {
  //       'Content-Type': 'application/json'
  //     },
  //   })
  //   .then(r => r.json())
  //   .then(r => {
  //     let msg2 = { name: "Rolando", message: r.response };
  //     this.messages.push(msg2);
  //     this.updateChatText(chatBox)
  //     textField.value = ''
  //   }).catch((error) => {
  //     console.error('Error:', error);
  //     this.updateChatText(chatBox)
  //     textField.value = ''
  //   });

  // }

  // Using Websockets
  onSendButton(chatBox) {
    const textField = chatBox.querySelector('input');
    const text = textField.value;
    if (!text) return;

    const msg1 = { name: "User", message: text };
    this.messages.push(msg1);
    this.updateChatText(chatBox);
    textField.value = '';

    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      try {
        this.socket.send(text);
      } catch (error) {
        console.error("Error sending message:", error);
        alert("Failed to send message. Please try again.");
      }
    } else {
      console.error("WebSocket connection is not open.");
      alert("Connection lost. Attempting to reconnect...");
    }
  }


  updateChatText(chatBox) {
    var html = '';
    this.messages.slice().reverse().forEach(function(item ) {
      if (item.name == "Rolando") {
        html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
      } else {
        html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
      }
    });

    const chatmessage = chatBox.querySelector('.chatbox__messages');
    chatmessage.innerHTML = html;
  }
}

const chatbox = new Chatbox();
chatbox.display();
