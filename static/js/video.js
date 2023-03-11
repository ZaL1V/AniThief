
const episodesBySeason = {{ episodes_by_season|json }};

// Добавляем прослушиватель событий к элементу Seasons <select>
const seasonsSelect = document.getElementById('seasons-select');
const episodesSelect = document.getElementById('episodes-select');

seasonsSelect.addEventListener('change', (event) => {
    const seasonValue = event.target.value;
    const episodes = episodesBySeason[seasonValue];

// Удаляем все существующие опции
    while (episodesSelect.firstChild) {
        episodesSelect.removeChild(episodesSelect.firstChild);
    }

    // Добавляем новые опции для выбранного сезона
    for (const episode of episodes) {
        const option = document.createElement('option');
        option.value = episode.toLowerCase().replace(' ', '-');
        option.text = episode;
        episodesSelect.appendChild(option);
    }
});

