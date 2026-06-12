class PhotoViewer {
    init() {
    const rootElm = document.getElementById('photoViewer');
    const frameElm = rootElm.querySelector('.frame');
    const image = `https://placehold.co/250x250/#81DAF5`;

    frameElm.innerHTML = `
        <div class="currentImage">
        <img src="${image}" />
        </div>
    `;
    }
}
new PhotoViewer().init();
