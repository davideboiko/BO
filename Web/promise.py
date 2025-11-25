const url="https";
const post="";

fetch(url).then(response=>response.json()).then(ris=>post=ris
    {
        console.log(ris)
        post=ris
    }
).catch(ee=>console.log(err))

async function getPost(){
    const response=await fetch(url);
    const ris=await response.json()
    console.log(ris)
} 

getPost().then(ris=>console.log(ris));
console.log(post)


"prendiamo un url con chiamata asincrona diamo un comando. il flusso importo una variabile. il risultato di una chiamata asincrona non può essere lavorata"