// selectors
const key = document.querySelector('#key');
const value = document.querySelector('#value');
const btnSubmit = document.querySelector('#submit');
// addeventListener
btnSubmit.addEventListener('click',(e)=>{
// prevent browser refreshing when  used form submit
e.preventDefault();
// get the data from input element
const dataKey = key.value;
const dataValue = value.value;
// check first if there is a data value then add in to storage.
if(dataKey && dataValue){
    localStorage.setItem(dataKey,dataValue);
}
// display the data in DOM first check if the storage has a data. 
if(localStorage.getItem(dataKey)){
// and get the data and save in to variable.
    const dataJSON = localStorage.getItem(dataKey);
    // create element
    const para = document.createElement('p');
    // insert innerText paragraph the data value.
    para.innerText = dataJSON;
    // insert in the dom
    document.body.appendChild(para)

}
})

// another solution to display data in DOM first check if localstorage has data length
if(localStorage.length > 0){
    // loop all the data
    for(let i = 0; i < localStorage.length; i++){
        // get all the key in localstorage
        const keyMe = localStorage.key([i])
        // get all the data value by providing key in getItem method
        const valueMe = localStorage.getItem(keyMe)
        // createElement
        const p = document.createElement('p');
        //insert innerText the value from localstorage
        p.innerText = valueMe;
        //add id using setAttribute
        p.setAttribute('id','myvalue');
        // append the element with value in body tag 
        document.body.appendChild(p)
    }
}
