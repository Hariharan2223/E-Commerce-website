
  let socket = null;  // Initialize socket variable

  const searchInput = document.getElementById('searchInput');
  const suggestionsContainer = document.getElementById('suggestions');

  // Event listener for typing in the search input
  searchInput.addEventListener('input', function(event) {
    const query = event.target.value;

    // Trigger WebSocket connection once the user starts typing
    if (query.length > 2) {  // Trigger WebSocket after typing at least 3 characters
      if (!socket || socket.readyState !== WebSocket.OPEN) {
        // Establish a new WebSocket connection if one is not open
        socket = new WebSocket("ws://localhost:8000/ws/search/");

        // WebSocket connection opened
        socket.onopen = function() {
          console.log("WebSocket connection established.");
        };

        // WebSocket connection closed
        socket.onclose = function() {
          console.log("WebSocket connection closed.");
        };

        // Handle WebSocket errors
        socket.onerror = function(error) {
          console.error("WebSocket error:", error);
        };

        // Handle messages received from WebSocket (search suggestions)
        socket.onmessage = function(event) {
          const data = JSON.parse(event.data);
          
          if (data.suggestions) {
            displaySuggestions(data.suggestions);
          } else if (data.error) {
            suggestionsContainer.innerHTML = 'Error: ' + data.error;
          }
        };
      }

      // Send the search query to the WebSocket backend
      socket.send(JSON.stringify({ query: query }));
    } else {
      // If query is too short, clear suggestions
      suggestionsContainer.innerHTML = '';
    }
  });

  // Function to display suggestions below the search bar
  function displaySuggestions(suggestions) {
    suggestionsContainer.innerHTML = '';  // Clear any previous suggestions

    if (suggestions.length === 0) {
      suggestionsContainer.innerHTML = '<p>No suggestions found.</p>';
    } else {
      suggestions.forEach(function(suggestion) {
        const suggestionItem = document.createElement('div');
        suggestionItem.classList.add('suggestion-item');
        suggestionItem.innerHTML = `
          <img src="${suggestion.image}" alt="${suggestion.name}" class="suggestion-image">
          <span>${suggestion.name}</span>
        `;
        suggestionsContainer.appendChild(suggestionItem);
      });
    }
  }

  // Handle form submission (optional)
  document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const query = searchInput.value;
    if (query.length > 0) {
      window.location.href = `/search/?query=${query}`;  // Redirect to search results page
    }
  });

