// v1
// (function() {
//     $(document).ready(function() {
//         const slider = $('#slider ul');
//         const sliderItems = slider.find('li');
//         const totalSlides = sliderItems.length;
//         const slideWidth = sliderItems.first().outerWidth();
//         let currentSlide = 1;

//         const moveSlider = function(direction) {
//             if (direction === 'next') {
//                 currentSlide = (currentSlide % totalSlides) + 1;
//             } else if (direction === 'previous') {
//                 currentSlide = (currentSlide - 2 + totalSlides) % totalSlides +1 ;
//             }

//             const newPosition = -(currentSlide - 1) * slideWidth;
//             console.log(newPosition);
//             slider.css('margin-left', newPosition);
//         };

//         // Event handlers for previous and next buttons
//         $('#previous').on('click', function(e) {
//             e.preventDefault();
//             moveSlider('previous');
//         });

//         $('#next').on('click', function(e) {
//             e.preventDefault();
//             moveSlider('next');
//         });
//     });
// })();


// v2
(function() {
    // script.js
console.log($('#previous').attr('href'));
$(document).ready(function () {
    // Set the current slide index and the slide width
    let currentSlide = 0;
    const slideWidth = $('#slider').width();
  
    // Function to move the slider to the specified slide index
    function moveSlider(slideIndex) {
      const displacement = slideWidth * slideIndex;
      $('#slider ul').animate({ left: -displacement }, 500, 'easeInOutExpo');
    }
  
    // Function to move to the next slide
    function nextSlide() {
      currentSlide++;
      if (currentSlide >= $('#slider li').length) {
        // If at the rightmost image, create a new ul, and delete the old one
        currentSlide = 0;
        const $oldUl = $('#slider ul');
        const $newUl = $oldUl.clone();
        $newUl.css('left', 0);
        $oldUl.remove();
        $('#slider').append($newUl);
      }
      moveSlider(currentSlide);
    }
  
    // Function to move to the previous slide
    function previousSlide() {
      currentSlide--;
      if (currentSlide < 0) {
        // If at the leftmost image, create a new ul, and delete the old one
        currentSlide = $('#slider li').length - 1;
        const $oldUl = $('#slider ul');
        const $newUl = $oldUl.clone();
        const lastSlidePosition = -slideWidth * currentSlide;
        $newUl.css('left', -lastSlidePosition);
        $oldUl.remove();
        $('#slider').prepend($newUl);
      }
      moveSlider(currentSlide);
    }
  
    // Attach click event handlers to the previous and next links
    $('#previous').click(function (e) {
      e.preventDefault();
      previousSlide();
    });
  
    $('#next').click(function (e) {
      e.preventDefault();
      nextSlide();
    });
  });  
})();


