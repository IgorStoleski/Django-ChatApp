function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



async function sendMessage() {
    let fd = new FormData();
    let csrftoken = getCookie('csrftoken');
    fd.append("textmessage", messageField.value);
    fd.append("csrfmiddlewaretoken", csrftoken);
    try {
      await fetch('/chat/', {
        method: 'POST',
        body: fd,
      });
      location.reload();
    } catch (error) {
      console.error(error);
    }
    
}

document.addEventListener('DOMContentLoaded', function () {
    // Funktion, um zu überprüfen, ob alle erforderlichen Eingabefelder ausgefüllt sind
    function checkInputs() {
        const inputs = document.querySelectorAll('.required-input');
        let allFilled = true;
        inputs.forEach(function (input) {
            if (input.value.trim() === '') {
                allFilled = false;
            }
        });
        return allFilled;
    }

    // Funktion zum Aktivieren / Deaktivieren des Registrierungs-Buttons basierend auf den Eingaben
    function toggleButtonState() {
        const registerButton = document.getElementById('register-btn');
        registerButton.disabled = !checkInputs();
    }

    // Fügen Sie Event-Listener für Eingabefelder hinzu, um den Registrierungs-Button zu überprüfen
    const inputs = document.querySelectorAll('.required-input');
    inputs.forEach(function (input) {
        input.addEventListener('keyup', toggleButtonState);
    });
});

let messageContainers = document.querySelectorAll('#messageContainer .message-container');
if (messageContainers.length > 0) {
    let lastMessageContainer = messageContainers[messageContainers.length - 1];
    if (lastMessageContainer) {
        lastMessageContainer.classList.add('last-message');
    }
}

/* document.getElementById('messageField').addEventListener('input', function() {
    const messageField = document.getElementById('messageField');
    const sendButton = document.getElementById('sendButton');
    if(messageField.value.trim() !== '') {
        sendButton.disabled = false;
    } else {
        sendButton.disabled = true;
    }
}); */

const messageField = document.getElementById('messageField');

if (messageField) {
    messageField.addEventListener('input', function() {
        const sendButton = document.getElementById('sendButton');
        if (messageField.value.trim() !== '') {
            sendButton.disabled = false;
            
        }else {
            sendButton.disabled = true;
        }       
    });
}