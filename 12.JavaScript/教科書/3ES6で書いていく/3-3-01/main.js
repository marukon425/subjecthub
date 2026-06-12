// 一定時間で次の画像が表示されるようにする
class PhotoViewer {

    constructor(rootElm, images) {
        this.rootElm = rootElm;
        this.images = images;
        this.currentIndex = 0;
    }

    init() {
        const nextButtonElm = this.rootElm.querySelector('.nextButton');
        const prevButtonElm = this.rootElm.querySelector('.prevButton');
        nextButtonElm.addEventListener('click', () => {
            this.next();
        });

        prevButtonElm.addEventListener('click', () => {
            this.prev();
        });

        this.updatePhoto();
    }

    updatePhoto() {
        const frameElm = this.rootElm.querySelector('.frame');
        const imageIndex = this.currentIndex + 1;
        const image = this.images[this.currentIndex];
        frameElm.innerHTML = `
<div class="currentImage">
<p>${imageIndex}枚目</p>
<img src="${image}" />
</div>
        `;
        this.startTimer();
    }
    startTimer() {
        if (this.timerKey){
            clearTimeout(this.timerKey);
        }

        this.timerKey = setTimeout(() => {
            this.next();
        }, 3000);
    }

    next() {
        const lastIndex = this.images.length -1;
        if (lastIndex === this.currentIndex) {
            this.currentIndex = 0;
        }else{
            this.currentIndex ++;
        }
        this.updatePhoto();
    }

    prev() {
        const lastIndex = this.images.length -1;
        if (this,this.currentIndex === 0){
            this.currentIndex = lastIndex;
        }else{
            currentIndex --;
        this.updatePhoto();
        }
    }
}

const images = [
    `https://placehold.jp/81daf5/ffffff/250x250.png`,
    `https://placehold.jp/f781f3/ffffff/250x250.png`,
    `https://placehold.jp/81F7D8/ffffff/250x250.png`,
    `../IMG_7138.PNG`
];

new PhotoViewer(document.getElementById('photoViewer'), images).init();
