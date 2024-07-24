// selector
const divContainer = document.querySelector('#container')



// fetch the data from external link

const getData = async () =>{
const response =  await fetch('https://api.tvmaze.com/search/shows?q=actions');
return response.json();
}


document.addEventListener('DOMContentLoaded', async () =>{
    let tvShow = [];
    try {
         tvShow = await getData();
        
    } catch (error) {
        console.log(error);
    }
    
    // const {image,language,averageRuntime,summary} = show;
         tvShow.map(tv =>{
            const {image,averageRuntime,language,summary} = tv.show;
            let html = `<div class="container">
            <img src="${image.medium}" alt="">
            <h1 class="mname">${name}</h1>
            <div class="spa">
        
                <span>averageRuntime: ${averageRuntime} Min. </span>
                <span>language: ${language}</span>
                <span>${summary}</span>
            </div>
        </div>`
        document.body.innerHTML += html;
         })
  

    
})