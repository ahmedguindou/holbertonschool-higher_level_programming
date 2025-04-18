document.addEventListener('DOMContentLoaded', () => {
    const characterElement = document.getElementById('character');
  
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        characterElement.textContent = data.name;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        characterElement.textContent = 'Error loading character';
      });
  });
