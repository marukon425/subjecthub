// 画像を無限に「次へ」「前へ」にする

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
        const image = this.images[this.currentIndex];
        frameElm.innerHTML = `
<div class="currentImage">
<img src="${image}" />
</div>
        `;
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
