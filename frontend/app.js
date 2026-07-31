// Mobile Navigation
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");

hamburger.addEventListener("click", () => {
    navLinks.classList.toggle("show");
});

// Navbar Shadow
window.addEventListener("scroll", () => {
    document
        .querySelector(".navbar")
        .classList.toggle("scrolled", window.scrollY > 20);
});

// Temporary Booking Button Demo
document.querySelectorAll(".book-resource-btn:not(:disabled)")
.forEach(button => {

    button.addEventListener("click", () => {

        alert("Booking form will be implemented in the next commit.");

    });

});