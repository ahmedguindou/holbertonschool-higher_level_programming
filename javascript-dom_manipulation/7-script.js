document.addEventListener('DOMContentLoaded', () => {
    const listMovies = document.getElementById('list_movies');
  
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        data.results.forEach(movie => {
          const li = document.createElement('li');
          li.textContent = movie.title;
          listMovies.appendChild(li);
        });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        listMovies.textContent = 'Error loading movies';
      });
  });
