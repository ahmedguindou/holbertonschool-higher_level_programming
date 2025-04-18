document.addEventListener('DOMContentLoaded', () => {
    const redHeader = document.getElementById('red_header');
    
    redHeader.addEventListener('click', () => {
      // Add .red class to the header
      document.querySelector('header').classList.add('red');
    });
  });
  