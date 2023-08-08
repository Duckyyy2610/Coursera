$(document).ready(function() {
    console.log($('#prev').attr('href'));
    const $slider = $('#slider-wrapper ul');
    const slideWidth = $('#slider-wrapper').width();
    let currentIndex = 0;
  
    function goToSlide(index) {
      $slider.css('transform', `translateX(-${index * slideWidth}px)`);
    }
  
    // Next slide function
    function nextSlide() {
      currentIndex = (currentIndex + 1) % $slider.children().length;
      goToSlide(currentIndex);
    }
  
    // Set an interval to auto-play the slider every 5 seconds (adjust as needed)
    const interval = setInterval(nextSlide, 5000);
  
    // Pause the auto-play when hovering over the slider
    $slider.hover(
      function() {
        clearInterval(interval);
      },
      function() {
        interval = setInterval(nextSlide, 5000);
      }
    );
  });
  