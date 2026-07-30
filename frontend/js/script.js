// ===========================================
// SyncReserve AI - Frontend Script
// ===========================================

// Backend API URL
const API_URL = "http://127.0.0.1:8000/api/book";

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
// Booking Form Submission
// ==========================

bookingForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const studentId = document.getElementById("studentId").value.trim();
    const resource = document.getElementById("resource").value;
    const bookingDate = document.getElementById("bookingDate").value;
    const timeSlot = document.getElementById("timeSlot").value;

    // Create start time
    const startTime = `${bookingDate}T${timeSlot}:00`;

    // Create end time (+1 hour)
    const hour = parseInt(timeSlot.split(":")[0]) + 1;
    const endHour = String(hour).padStart(2, "0");
    const endTime = `${bookingDate}T${endHour}:00:00`;

    const bookingData = {
        student_id: studentId,
        resource_id: resource,
        start_time: startTime,
        end_time: endTime
    };

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(bookingData)

        });

        const result = await response.json();

        if (response.ok && result.success) {

            alert(result.message);

            bookingForm.reset();

            closeModal();

        } else {

            alert(result.message || "Booking failed.");

        }

    } catch (error) {

        console.error(error);

        alert("Unable to connect to backend.");

    }

});