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
        this.currentIndex++;
        if (this.currentIndex >= this.images.length) {
            this.currentIndex = 0;
        }

        this.updatePhoto();
    }

    prev() {
        this.currentIndex--;
        if (this.currentIndex < 0) {
            this.currentIndex = this.images.length - 1;
        }

        this.updatePhoto();
    }
}

const images = [
    `https://placehold.jp/81daf5/ffffff/250x250.png`,
    `https://placehold.jp/f781f3/ffffff/250x250.png`,
    `https://placehold.jp/81F7D8/ffffff/250x250.png`];

new PhotoViewer(document.getElementById('photoViewer'), images).init();
