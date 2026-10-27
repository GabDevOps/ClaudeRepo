// Talks to the backend: sends the search, shows the results.

const API_URL = "http://127.0.0.1:8000"; // where the backend runs

const form = document.getElementById("search-form");
const statusLine = document.getElementById("status");
const resultsList = document.getElementById("results");

form.addEventListener("submit", async (event) => {
  event.preventDefault(); // stop the browser from reloading the page

  // 1. Read what the user typed and build the request URL
  const params = new URLSearchParams({ city: document.getElementById("city").value });
  const maxPrice = document.getElementById("max-price").value;
  const minRooms = document.getElementById("min-rooms").value;
  if (maxPrice) params.set("max_price", maxPrice);
  if (minRooms) params.set("min_rooms", minRooms);

  statusLine.textContent = "Searching...";
  resultsList.innerHTML = "";

  // 2. Ask the backend
  try {
    const response = await fetch(`${API_URL}/search?${params}`);
    const data = await response.json();

    // 3. Show the results
    statusLine.textContent = `${data.count} house(s) found`;
    for (const house of data.results) {
      const item = document.createElement("li");
      item.innerHTML = `
        <strong>${house.title}</strong><br>
        ${house.city} · ${house.rooms} rooms · ${house.size_m2} m²<br>
        <span class="price">€${house.price.toLocaleString()}</span>`;
      resultsList.appendChild(item);
    }
  } catch (error) {
    statusLine.textContent = "Could not reach the backend. Is it running?";
  }
});
