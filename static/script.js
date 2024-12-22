// Fetch mission data from the backend
async function fetchMissions() {
    try {
        const response = await fetch('/missions');
        const data = await response.json();
        displayMissions(data);
    } catch (error) {
        console.error('Error fetching mission data:', error);
    }
}

// Display missions in the mission list
function displayMissions(missions) {
    const missionList = document.getElementById('mission-list');
    missionList.innerHTML = ''; // Clear existing missions

    Object.keys(missions).forEach(mission => {
        const missionData = missions[mission];
        const missionElement = document.createElement('div');
        missionElement.className = 'mission-item';
        missionElement.innerHTML = `
            <h3>${mission}</h3>
            <p>Status: ${missionData.status}</p>
        `;
        missionElement.addEventListener('click', () => showMissionDetails(mission, missionData));
        missionList.appendChild(missionElement);
    });
}

// Show detailed information for a selected mission
function showMissionDetails(missionName, missionData) {
    const missionDetails = document.getElementById('mission-details');
    missionDetails.innerHTML = `
        <h2>${missionName}</h2>
        <p><strong>Launch Date:</strong> ${missionData.launch_date}</p>
        <p><strong>Status:</strong> ${missionData.status}</p>
        <p><strong>Objectives:</strong> ${missionData.objectives}</p>
        <p><strong>Current Location:</strong> ${missionData.current_location}</p>
    `;
    missionDetails.classList.remove('hidden');
}

// Filter missions based on the search input
function searchMissions() {
    const searchTerm = document.getElementById('search').value.toLowerCase();
    const missionItems = document.querySelectorAll('.mission-item');
    const missionList = document.getElementById('mission-list');

    // Show or hide mission items based on the search term
    let hasResults = false;
    missionItems.forEach(item => {
        const missionName = item.querySelector('h3').innerText.toLowerCase();
        const matches = missionName.includes(searchTerm);
        item.style.display = matches ? 'block' : 'none';
        if (matches) hasResults = true;
    });

    // Toggle visibility of the mission list
    if (hasResults || searchTerm.trim() === '') {
        missionList.classList.remove('hidden');
    } else {
        missionList.classList.add('hidden');
    }
}

// Initialize the page by fetching missions and binding events
document.addEventListener('DOMContentLoaded', () => {
    fetchMissions();
    document.getElementById('search').addEventListener('input', searchMissions);
});
