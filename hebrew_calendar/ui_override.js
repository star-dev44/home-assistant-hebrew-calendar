// Override Home Assistant's date display
async function overrideDates() {
    const response = await fetch("http://localhost:5000/convert");
    const data = await response.json();

    document.querySelectorAll(".datetime, .date, .calendar").forEach(el => {
        el.innerText = data.hebrew_date;
    });
}

// Wait for UI to load, then override
window.onload = () => {
    setTimeout(overrideDates, 2000);
};
