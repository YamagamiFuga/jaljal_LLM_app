document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    const videoList = document.getElementById('video-list');
    const descriptionDiv = document.getElementById('description');

    // フォーム送信時の処理
    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const category = searchInput.value.trim();
        if (category) {
            fetchVideos(category);
        }
    });

    // 動画を取得して表示
    async function fetchVideos(category) {
        const response = await fetch('http://127.0.0.1:8000/spi/jaljal', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify([{ role: "user", message: category, description: category }])

        });

        if (response.ok) {
            const data = await response.json();
            displayDescription(data.description);
            displayVideos(data.data);
        } else {
            descriptionDiv.textContent = "動画が見つかりませんでした。";
            videoList.innerHTML = "";
        }
    }

    // 説明文を表示
    function displayDescription(description) {
        descriptionDiv.textContent = description;
    }

    // 動画リストを表示
    function displayVideos(videos) {
        videoList.innerHTML = '';
        Object.keys(videos).forEach(title => {
            const url = videos[title];
            const videoElement = document.createElement('div');
            videoElement.className = 'video';
            videoElement.innerHTML = `
                <h3>${title}</h3>
                <a href="${url}" target="_blank">この動画にする！</a>
            `;
            videoList.appendChild(videoElement);
        });
    }
});
