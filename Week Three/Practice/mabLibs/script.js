// selectors
let nounsInput = document.querySelector('#noun');
let adjectiveInput = document.querySelector('#adjective');
let personNameInput = document.querySelector('#person');
let libButton = document.querySelector('#lib-button');
let storyDisplay = document.querySelector('#story');


//  function 
const makeMadLib = ({ noun, adjective, person } = libs) => {
    // i have 3 parameter... 
    // noun,adjective,person using object destructuring technic.
    // using template literals this ---> `` to structure the sentence.
    storyDisplay.innerText = `${person} ${adjective} ${noun}.`

}

//AddEventListener

libButton.addEventListener('click', () => {
    // i am experiencing what i can do with object
    const libs = {
        noun: nounsInput.value,
        adjective: adjectiveInput.value,
        person: personNameInput.value,
    }
    // this method makeMadLib to retrieve the object libs...
    // to send in my scope block function makeMadLib
    makeMadLib(libs)
})