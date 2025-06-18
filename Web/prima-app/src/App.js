import logo from './logo.svg';
import './App.css';
import "bootstrap/dist/css/bootstrap.css"
import { Componente1 } from './Componente1';
import { Clock } from './Clock';
/*function getDate(date) {
  return  date.toLocaleDateString()+" "+ date.toLocaleDateString()
}*/
function App() {
  let name = "Pasha";
  return (
    <div className="App">
      
      <h1>Pisdun {name} </h1>
      <h2>
        {
          new Date().toLocaleDateString()+" "+new Date().toLocaleDateString()
        }
      </h2>
      
        <Clock timezone="1" country="ITALY"></Clock>
        <Clock timezone="4" country="USA"></Clock>
        <Clock timezone="8" country="JAPAN"></Clock>
      
        <Componente1></Componente1>
    </div>
  );
}

export default App;
