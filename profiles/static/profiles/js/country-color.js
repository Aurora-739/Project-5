document.addEventListener('DOMContentLoaded', function () {
    const countryField = document.getElementById('id_default_country');

    function updateCountryColor() {
        if (!countryField.value) {
            countryField.style.color = "#6c757d";  // Placeholder grey
        } else {
            countryField.style.color = "#000";     // Black when selected
        }
    }

    // Run on page load
    updateCountryColor();

    // Run every time selection changes
    countryField.addEventListener('change', updateCountryColor);
});
