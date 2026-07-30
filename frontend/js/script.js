// ===========================================
// SyncReserve AI - Frontend Script
// ===========================================

// Modal Elements
const modal = document.getElementById("bookingModal");
const closeBtn = document.querySelector(".close");

// Buttons
const heroBookBtn = document.querySelector(".hero-book-btn");
const bookButtons = document.querySelectorAll(".book-btn");

// Booking Form
const bookingForm = document.getElementById("bookingForm");

// ==========================
// Open Modal
// ==========================

function openModal() {
    modal.style.display = "flex";
}

// ==========================
// Close Modal
// ==========================

function closeModal() {
    modal.style.display = "none";
}

// ==========================
// Hero Button
// ==========================

heroBookBtn.addEventListener("click", openModal);

// ==========================
// Resource Card Buttons
// ==========================

bookButtons.forEach(button => {

    if (!button.disabled) {

        button.addEventListener("click", openModal);

    }

});

// ==========================
// Close Button
// ==========================

closeBtn.addEventListener("click", closeModal);

// ==========================
// Close when clicking outside
// ==========================

window.addEventListener("click", function (event) {

    if (event.target === modal) {

        closeModal();

    }

});

// ==========================
// Booking Form
// ==========================

bookingForm.addEventListener("submit", function (event) {

    event.preventDefault();

    alert("Booking request submitted successfully!");

    bookingForm.reset();

    closeModal();

});