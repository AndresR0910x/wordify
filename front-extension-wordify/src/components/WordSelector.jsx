// WordSelector.jsx
import React from 'react'

const WordSelector = ({ onWordSelect }) => {  // Cambiado onWordSelector a onWordSelect
  
  const handleWordSelector = () => {
    const selection = window.getSelection().toString().trim();
    if (selection && /^[a-zA-Z]+$/.test(selection)) {
      onWordSelect(selection);  // Llama a la función pasada como prop correctamente
      console.log(selection);
    }  
  };

  return (
    <div>
      <button onClick={handleWordSelector}
              className='bg-blue-500 text-white py-2 px-4 rounded'>
        Seleccionar palabra
      </button>
      <div className='mt-4'>
        <p>
          Aquí tienes un texto de ejemplo. Puedes seleccionar una palabra como "hola", 
          "mundo" o cualquier otra palabra válida y agregarla a tu vocabulario.
        </p>
      </div>
    </div>
  );
}

export default WordSelector
