
        let socket = null; // Initialize socket variable
        let isSocketConnecting = false; // Track whether the socket is being established
      
        const searchInput = document.getElementById('searchInput');
        const suggestionsContainer = document.getElementById('suggestions');
      
        // Event listener for typing in the search input
        searchInput.addEventListener('input', function (event) {
            const query = event.target.value;
      
            if (query.length > 2) { // Trigger WebSocket after typing at least 3 characters
                if (!socket || socket.readyState !== WebSocket.OPEN) {
                    if (!isSocketConnecting) {
                        // Establish a new WebSocket connection if one is not open
                        isSocketConnecting = true;
                        socket = new WebSocket("ws://localhost:8000/ws/search/");
      
                        // WebSocket connection opened
                        socket.onopen = function () {
                            console.log("WebSocket connection established.");
                            isSocketConnecting = false;
                            sendQuery(query); // Send the query after connection is established
                        };
      
                        // WebSocket connection closed
                        socket.onclose = function () {
                            console.log("WebSocket connection closed.");
                            isSocketConnecting = false;
                            socket = null;
                        };
      
                        // Handle WebSocket errors
                        socket.onerror = function (error) {
                            console.error("WebSocket error:", error);
                            isSocketConnecting = false;
                            socket = null;
                        };
      
                        // Handle messages received from WebSocket (search suggestions)
                        socket.onmessage = function (event) {
                            const data = JSON.parse(event.data);
                            if (data.suggestions) {
                                displaySuggestions(data.suggestions);
                            } else if (data.error) {
                                suggestionsContainer.innerHTML = 'Error: ' + data.error;
                            }
                        };
                    }
                } else {
                    // If WebSocket is already open, send the query
                    sendQuery(query);
                }
            } else {
                // If query is too short, clear suggestions
                suggestionsContainer.innerHTML = '';
            }
        });
      
        // Function to send a query via WebSocket
        function sendQuery(query) {
            if (socket && socket.readyState === WebSocket.OPEN) {
                socket.send(JSON.stringify({ query: query }));
            }
        }
      
        // Function to display suggestions below the search bar
        function displaySuggestions(suggestions) {
            suggestionsContainer.innerHTML = ''; // Clear any previous suggestions
      
            if (suggestions.length === 0) {
                suggestionsContainer.innerHTML = '<p>No suggestions found.</p>';
            } else {
                suggestions.forEach(function (suggestion) {
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
