window.onscroll = function() {myFunction()};
var navbar = document.querySelector(".navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}




document.querySelector('.testimonial').addEventListener('mouseover',function(){
    const counters = document.querySelectorAll(".counter_number");
    counters.forEach(counter => {
        const updatecount = function () {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerHTML;
            if (count < target) {
                counter.innerHTML = count + 1;
                setTimeout(updatecount, 20);
            }
            else {
                count.innerHTML = target;
            }
        }
        updatecount();
    })
})


AOS.init({
    duration:2000
});