export function listaOgetti(dati)S{
    return Object.keys(dati).map(id=>({
        id,
        ...dati[id] 
    }))
} 