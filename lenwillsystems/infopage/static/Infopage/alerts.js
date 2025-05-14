document.addEventListener("DOMContentLoaded", function () {
    const messageBox = document.getElementById("django-message");

    if (messageBox) {
        const message = messageBox.dataset.message;
        if (message) {
            alert(message);
        }
    }
});
