document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const suggestionsBox = document.getElementById("suggestions");

    searchInput.addEventListener("input", function() {
        const query = this.value;
        if (query.length > 0) {
            fetch(`/search-suggestions/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsBox.innerHTML = data.suggestions.map(product => `
                        <div class="suggestion-item" data-value="${product.name}">
                            <img src="${product.image}" alt="${product.name}" width="30">
                            ${product.name}
                        </div>
                    `).join('');
                    suggestionsBox.style.display = 'block';
                })
                .catch(error => {
                    console.error('Error fetching suggestions:', error);
                });
        } else {
            suggestionsBox.style.display = 'none';
        }
    });

    suggestionsBox.addEventListener("click", function(event) {
        if (event.target.classList.contains("suggestion-item")) {
            searchInput.value = event.target.getAttribute("data-value");
            suggestionsBox.style.display = 'none';
        }
    });

    // Hide suggestions when clicking outside
    document.addEventListener("click", function(event) {
        if (!searchInput.contains(event.target) && !suggestionsBox.contains(event.target)) {
            suggestionsBox.style.display = 'none';
        }
    });
});






