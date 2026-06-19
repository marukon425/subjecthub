/**
 * 寿司打タイピングゲーム
 * AJAXでdata.jsonから単語を取得し、ローマ字タイピングゲームを実現する
 */

// ============================================================
// Gameクラス：ゲームの状態と処理を管理する
// ============================================================
class Game {
  constructor() {
    this.allWords = [];      // 全単語データ
    this.gameWords = [];     // 今回使用する単語リスト
    this.currentIndex = 0;  // 現在の単語インデックス
    this.typedCount = 0;    // 現在の単語の入力済み文字数
    this.score = 0;         // 合計スコア
    this.correctCount = 0;  // 正解した単語数
    this.timeLeft = 60;     // 残り時間（秒）
    this.totalTime = 60;    // 制限時間
    this.timerInterval = null;
    this.isRunning = false;
    this.selectedCourse = 'easy';
  }

  // ----------------------------------------------------------
  // AJAXでdata.jsonを非同期取得する（例外処理あり）
  // ----------------------------------------------------------
  async loadWords() {
    try {
      const response = await fetch('./data.json');
      if (!response.ok) {
        throw new Error(`HTTP エラー: ${response.status}`);
      }
      this.allWords = await response.json();
    } catch (e) {
      // 読み込み失敗時は上位に例外を伝播させる
      throw new Error('単語データの読み込みに失敗しました。\n' + e.message);
    }
  }

  // ----------------------------------------------------------
  // 配列をシャッフルして返す（Fisher-Yates法）
  // ----------------------------------------------------------
  shuffle(arr) {
    const result = [...arr];
    for (let i = result.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
  }

  // ----------------------------------------------------------
  // ゲームを開始する
  // ----------------------------------------------------------
  start(course) {
    this.selectedCourse = course;
    this.score = 0;
    this.correctCount = 0;
    this.timeLeft = this.totalTime;
    this.currentIndex = 0;
    this.typedCount = 0;
    this.isRunning = false;

    // 選択コースの単語だけ抽出してシャッフル
    const filtered = this.allWords.filter(w => w.course.includes(course));
    this.gameWords = this.shuffle(filtered);

    showScreen('game');
    this.updateHUD();
    this.updateTimerBar();
    this.loadCurrentWord();
    this.startTimer();
    this.isRunning = true;
  }

  // ----------------------------------------------------------
  // 現在のインデックスの単語を画面に表示する
  // ----------------------------------------------------------
  loadCurrentWord() {
    // 全単語を打ち終えたら再シャッフルして最初から
    if (this.currentIndex >= this.gameWords.length) {
      this.currentIndex = 0;
      this.gameWords = this.shuffle(this.gameWords);
    }

    this.typedCount = 0;
    const word = this.gameWords[this.currentIndex];

    document.getElementById('word-name').textContent = word.name;
    document.getElementById('word-reading').textContent = word.reading;
    document.getElementById('word-price').textContent = '¥' + word.price;
    this.updateRomanDisplay();
  }

  // ----------------------------------------------------------
  // ローマ字の「入力済み／次の文字／残り」を更新する
  // ----------------------------------------------------------
  updateRomanDisplay() {
    const roman = this.gameWords[this.currentIndex].roman;
    document.getElementById('roman-done').textContent    = roman.slice(0, this.typedCount);
    document.getElementById('roman-current').textContent = roman[this.typedCount] ?? '';
    document.getElementById('roman-rest').textContent    = roman.slice(this.typedCount + 1);
  }

  // ----------------------------------------------------------
  // キー入力を処理する（無名関数から呼び出される）
  // ----------------------------------------------------------
  handleKey(key) {
    if (!this.isRunning || key.length !== 1) return;

    // Caps Lock対策：大文字を小文字に変換
    const typedChar = key.toLowerCase();
    const roman = this.gameWords[this.currentIndex].roman;
    const expected = roman[this.typedCount];

    if (typedChar === expected) {
      // 正しいキー
      this.typedCount++;
      this.updateRomanDisplay();

      if (this.typedCount >= roman.length) {
        // 単語完成
        this.onWordComplete();
      }
    } else {
      // ミスタイプ
      this.onMistake();
    }
  }

  // ----------------------------------------------------------
  // 単語を正解したときの処理
  // ----------------------------------------------------------
  onWordComplete() {
    const word = this.gameWords[this.currentIndex];
    this.score += word.price;
    this.correctCount++;
    this.currentIndex++;
    this.updateHUD();

    // 正解エフェクト（緑フラッシュ）
    const area = document.getElementById('word-area');
    area.classList.add('correct');
    setTimeout(() => {
      area.classList.remove('correct');
      this.loadCurrentWord();
    }, 140);
  }

  // ----------------------------------------------------------
  // ミスタイプしたときの処理
  // ----------------------------------------------------------
  onMistake() {
    const area = document.getElementById('word-area');
    area.classList.add('wrong');
    setTimeout(() => area.classList.remove('wrong'), 140);
  }

  // ----------------------------------------------------------
  // タイマーを開始する
  // ----------------------------------------------------------
  startTimer() {
    clearInterval(this.timerInterval);
    this.timerInterval = setInterval(() => {
      this.timeLeft--;
      this.updateHUD();
      this.updateTimerBar();

      if (this.timeLeft <= 0) {
        this.endGame();
      }
    }, 1000);
  }

  // ----------------------------------------------------------
  // HUD（残り時間・スコア・正解数）を更新する
  // ----------------------------------------------------------
  updateHUD() {
    document.getElementById('timer').textContent = this.timeLeft;
    document.getElementById('score').textContent = '¥' + this.score.toLocaleString();
    document.getElementById('count').textContent = this.correctCount;
  }

  // ----------------------------------------------------------
  // タイマーバーの幅と色を更新する
  // ----------------------------------------------------------
  updateTimerBar() {
    const bar = document.getElementById('timer-bar');
    const pct = (this.timeLeft / this.totalTime) * 100;
    bar.style.width = pct + '%';

    // 残り時間に応じて色を変える
    bar.className = 'timer-bar';
    if (pct <= 25) {
      bar.classList.add('danger');
    } else if (pct <= 50) {
      bar.classList.add('warning');
    }
  }

  // ----------------------------------------------------------
  // ゲームを終了してリザルト画面を表示する
  // ----------------------------------------------------------
  endGame() {
    clearInterval(this.timerInterval);
    this.isRunning = false;

    document.getElementById('result-score').textContent = '¥' + this.score.toLocaleString();
    document.getElementById('result-count').textContent = this.correctCount + '問';
    document.getElementById('result-message').textContent = this.getResultMessage();

    showScreen('result');
  }

  // ----------------------------------------------------------
  // 正解数に応じた結果メッセージを返す
  // ----------------------------------------------------------
  getResultMessage() {
    const c = this.correctCount;
    if (c >= 30) return '🏆 プロの腕前！素晴らしい！';
    if (c >= 20) return '🎉 とても上手！さすがです！';
    if (c >= 10) return '👍 なかなかいい感じ！';
    if (c >= 5)  return '💪 もう少し！練習あるのみ！';
    return '🍣 ゆっくり確実に打とう！';
  }
}

// ============================================================
// 画面切り替え（無名関数として定義）
// ============================================================
const showScreen = (name) => {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-' + name).classList.add('active');
};

// ============================================================
// 初期化処理
// ============================================================
const game = new Game();

// AJAXでdata.jsonを取得してからタイトル画面を表示する（即時実行の無名関数）
(async () => {
  try {
    await game.loadWords();
    showScreen('title');
  } catch (e) {
    // 読み込み失敗時はエラーメッセージを表示
    document.body.innerHTML =
      `<div style="color:#e74c3c;padding:3rem;text-align:center;font-size:1.2rem">${e.message}</div>`;
  }
})();

// ============================================================
// イベントリスナー
// ============================================================

// コース選択ボタン
document.querySelectorAll('.btn-course').forEach(btn => {
  btn.addEventListener('click', () => {
    game.start(btn.dataset.course);
  });
});

// キーボード入力（無名関数）
document.addEventListener('keydown', (e) => {
  game.handleKey(e.key);
});

// リザルト画面：もう一度ボタン
document.getElementById('btn-retry').addEventListener('click', () => {
  game.start(game.selectedCourse);
});

// リザルト画面：タイトルへボタン
document.getElementById('btn-title').addEventListener('click', () => {
  showScreen('title');
});
