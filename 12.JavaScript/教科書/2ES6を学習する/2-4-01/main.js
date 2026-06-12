// クラスを適用する

class StopWatch {
    constructor(options = {}){
        this.options = options;
        this.timer = null;
    }

    init(){
        let {color, backgroundColor} = this.options;

        color = color || 'lightblue';
        backgroundColor = backgroundColor || 'black';

        this.display = document.getElementsByClassName('display')[0];
        this.display.style.color = color;
        this.display.style.backgroundColor = backgroundColor;

        this.logElm = document.querySelector('.log');

        const startButton = document.getElementsByClassName('startButton')[0];
        startButton.addEventListener('click', () => {
            if (this.timer === null){
                let seconds = 0;
                this.display.innerText = seconds;

                this.timer = setInterval(() => {
                    seconds++;
                    this.display.innerText = seconds;
                }, 1000);

                this.addMessage('開始');
            }
        });

        const stopButton = document.getElementsByClassName('stopButton')[0];
        stopButton.addEventListener('click', () => {
            if (this.timer !== null){
                clearInterval(this.timer);
                this.timer = null;

                this.addMessage('終了');
            }
        });
    }

    addMessage(message) {
        const messageElm = document.createElement('div');
        const now = new Date();
        messageElm.innerText =
            `${now.getHours()}時${now.getMinutes()}分${now.getSeconds()}秒 ${message}`;
        messageElm.classList.add('message');
        this.logElm.appendChild(messageElm);
    }
}

const options = {
    color: 'lightgreen',
    backgroundColor: '#333'
};

const sw = new StopWatch(options);
sw.init();
