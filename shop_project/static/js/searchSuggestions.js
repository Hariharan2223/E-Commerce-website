document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const suggestionsBox = document.getElementById("suggestions");


    const socket = new WebSocket('ws://127.0.0.1:8000/ws/search-suggestions/');

    socket.onopen = () => {
        console.log("WebSocket connection established.");
    };

    searchInput.addEventListener("input", function() {
        const query = this.value;
        if (query.length > 0) {
            socket.send(JSON.stringify({ query: query }));
        } else {
            suggestionsBox.style.display = 'none';
        }
    });

    socket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        suggestionsBox.innerHTML = data.suggestions.map(product => `
            <div class="suggestion-item" data-value="${product.name}">
                <img src="${product.image}" alt="${product.name}" width="30">
                ${product.name}
            </div>
        `).join('');
        suggestionsBox.style.display = 'block';
    };

    socket.onerror = function(error) {
        console.error("WebSocket error:", error);
    };

    socket.onclose = function() {
        console.log("WebSocket connection closed.");
    };

    document.addEventListener("click", function(event) {
        if (!searchInput.contains(event.target) && !suggestionsBox.contains(event.target)) {
            suggestionsBox.style.display = 'none';
        }
    });
});
