class PhotoViewer {
    constructor(rootElm, images) {
        this.rootElm = rootElm;
        this.images = images;
        this.currentIndex = 0;
    }

    init() {
    // const rootElm = document.getElementById('photoViewer');
    // const frameElm = rootElm.querySelector('.frame');
    // const image = 'https://fakeimg.pl/250x150/81DAF5';
    const frameElm = this.rootElm.querySelector('.frame')
    const image = this.images[this.currentIndex];
    frameElm.innerHTML = `
        <div class="currentImage">
        <img src="${image}" />
        </div>
    `;
    }
}
new PhotoViewer().init();
