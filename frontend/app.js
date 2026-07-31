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

        const modal = document.getElementById("bookingModal");

const closeBtn = document.querySelector(".close-btn");

document
.querySelectorAll(".book-resource-btn:not(:disabled)")
.forEach(button=>{

button.addEventListener("click",()=>{

modal.classList.add("show");

});

});

closeBtn.onclick=()=>{

modal.classList.remove("show");

};

window.onclick=(e)=>{

if(e.target===modal){

modal.classList.remove("show");

}

};

document
.getElementById("bookingForm")
.addEventListener("submit",(e)=>{

e.preventDefault();

alert("Booking request prepared successfully!");

modal.classList.remove("show");

});

    });

});