// ① ページ読み込み時に JSON を読み込む
window.addEventListener("DOMContentLoaded", () => {
  fetch("songs.json")
    .then(res => res.json())
    .then(data => {
      console.log("JSONの読み込み成功:", data);
      displaySongs(data); // 初期表示
    });
});

// ② 検索ボタン
document.getElementById("searchBtn").addEventListener("click", () => {
  const keyword = document.getElementById("keyword").value;
  const url = `https://itunes.apple.com/search?term=${keyword}&entity=song&limit=20`;

  axios.get(url)
    .then(res => {
      const songs = res.data.results;
      displaySongs(songs);
    })
    .catch(err => console.error(err));
});

// ③ 表示するだけの関数
function displaySongs(songs) {
  const result = document.getElementById("result");
  result.innerHTML = "";

  songs.forEach(song => {
    const card = `
      <div class="card">
        <img src="${song.artworkUrl100 || song.image}">
        <h3>${song.trackName || song.title}</h3>
        <p>${song.artistName || song.artist}</p>
        <a href="${song.previewUrl || song.preview}" target="_blank">▶ 試聴</a>
      </div>
    `;
    result.innerHTML += card;
  });
}
