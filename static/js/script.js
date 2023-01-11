setTimeout(function() {
    // setting 3 second for user message to disappear in base.html
    let messages = document.getElementById("message");
    let alert= new bootstrap.Alert(messages);
    alert.close();
}, 3000);

const trigger_search = document.querySelector('.trigger_search');
const submit_button = document.querySelector('.submit_button');
const input = document.querySelector('.input');

trigger_search.addEventListener('click', () =>{
    if (input.style.display = 'none') {
        input.style.display = 'unset';
        trigger_search.classList.add('input');
        submit_button.classList.remove('input');
    }
})
