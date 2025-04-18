document.addEventListener('DOMContentLoaded', () => {
    // Get the red_header div
    const redHeader = document.getElementById('red_header');
    
    // Add click event listener
    redHeader.addEventListener('click', () => {
      // Change header color to red
      document.querySelector('header').style.color = '#FF0000';
    });
  });
