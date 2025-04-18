document.addEventListener('DOMContentLoaded', () => {
    const helloElement = document.getElementById('hello');
  
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => {
        if (!response.ok) throw new Error('Network error');
        return response.json();
      })
      .then(data => {
        helloElement.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error:', error);
        helloElement.textContent = 'Error loading translation';
      });
  });