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
  
//Calling the form element to collect player name and use within handleSubmit function
let form = document.getElementById('quantity-form');
form.elements.quantity.focus(); // focusing on text box
/**
 * adds Enter event listener to form box by pressing 'Enter' or clicking 'Submit'
 */
form.addEventListener('keydown', function(event) {

    if (event.key === 'Enter') {
        handleSubmit(event);
    }
});
form.addEventListener('submit', handleSubmit);


/**Function to collect playerName from form section in #start-screen.
 * Hides start-screen and opens menu-screens.
 * PlayerName added to welcome message. 
 */
function handleSubmit(event) {

    event.preventDefault();

    let quantity = form.elements.quantity;
    let ingredientScreen = document.getElementById('ingredient-screen');
    let quantityScreen = document.getElementById('quantity-screen');
    let elements = ingredientScreen.getElementsByClassName('quantity-amount');

        for (let i = 0; i < elements.length; i++) {
            elements[i].innerHTML = Math.floor(elements[i].innerHTML) * quantity.value
        }

     quantityScreen.style.display = 'none';
     ingredientScreen.style.display = 'unset';
}


function displayIngredients() {
    let ingredientScreen = document.getElementById('ingredient-screen');
    let showButton = document.getElementById('ingredient-display');
    let hideButton = document.getElementById('hide-display');
    

    ingredientScreen.style.display = 'unset';
    showButton.style.display = 'none';
    hideButton.style.display = 'unset';

    return ingredientScreen;

}


function hideIngredients() {
    let ingredientScreen = document.getElementById('ingredient-screen');
    let showButton = document.getElementById('ingredient-display');
    let hideButton = document.getElementById('hide-display');
    

    ingredientScreen.style.display = 'none';
    showButton.style.display = 'unset';
    hideButton.style.display = 'none';
}

