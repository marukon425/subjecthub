// 一定時間で次の画像が表示されるようにする
class PhotoViewer {

    constructor(rootElm, images, interval = 3000) {
        this.rootElm = rootElm;
        this.images = images;
        this.interval = interval;
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
        }, this.interval);
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
    `https://placehold.jp/81daf5/ffffff/250x150.png`,
    `https://placehold.jp/f781f3/ffffff/250x150.png`,
    `https://placehold.jp/81f7d8/ffffff/250x150.png`,
];

new PhotoViewer(document.getElementById('photoViewer1'), images).init();
new PhotoViewer(document.getElementById('photoViewer2'), images, 1000).init();

function renderUsedImages(containerId, images) {
    const container = document.getElementById(containerId);
    container.innerHTML = images.map(src => `<a href="${src}">${src}</a><br>`).join('');
}

renderUsedImages('useimages1', images);
renderUsedImages('useimages2', images);

