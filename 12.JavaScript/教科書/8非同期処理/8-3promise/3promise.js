function displayMessage() {
    return fetch('./hello.json').then((response) => {
        return response.json();
    }).then((data) => {
        const messageElm = document.getElementById('message');
        messageElm.innerHTML = data.message
        console.log('終了');
    })
}