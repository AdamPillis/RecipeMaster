setTimeout(function() {
    // setting 3 second for user message to disappear in base.html
    let messages = document.getElementById("message");
    let alert= new bootstrap.Alert(messages);
    alert.close();
}, 3000);