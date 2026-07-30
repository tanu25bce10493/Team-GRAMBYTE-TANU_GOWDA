const toast = document.getElementById("toast");
const toastMessage = document.getElementById("toast-message");

function showToast(message) {

    toastMessage.textContent = message;

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 2500);

}

const approveButtons = document.querySelectorAll(".approve-btn");
const rejectButtons = document.querySelectorAll(".reject-btn");

approveButtons.forEach(button => {

    button.addEventListener("click", () => {

        showToast("Booking Approved Successfully");

    });

});

rejectButtons.forEach(button => {

    button.addEventListener("click", () => {

        showToast("Booking Rejected");

    });

});

console.log("Toast notification system loaded.");