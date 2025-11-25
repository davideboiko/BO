import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css';
import SelezioneAuto from "./eserciziobma/Bmwmaudi.jsx";

export default function App() {
  return <Bmwmaudi />;
}



{/*
export default App;

  function App() {
  
  const [visibile, funVisibilita] = useState(true);

  
  const pulsante = () => {
    funVisibilita(!visibile);
  };

  return (
    <div>
      <button onClick={pulsante}>
        {visibile ? "Nascondi" : "Mostra"}
      </button>
      {visibile && <p>Ciao come stai? Io molto bene!</p>}
    </div>
     );
}
*/} 
