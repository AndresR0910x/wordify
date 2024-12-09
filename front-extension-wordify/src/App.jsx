// App.jsx
import { useState } from 'react'
import './App.css'
import WordSelector from './components/WordSelector'
import VocabularyList from './components/VocabularyList'

const App = () => {
  const [selectedWord, setSelectedWord] = useState(null);
  const [vocabulary, setVocabulary] = useState([]);

  // Función para manejar el pop-up
  const handleSaveWord = (word) => {
    setSelectedWord(word);
    setVocabulary([...vocabulary, word]);  // Cambiado setSelectedWord a word
  }

  return (
    <div className="container mx-auto p-4">
      <WordSelector onWordSelect={handleSaveWord} /> 
      <VocabularyList vocabulary={vocabulary} />
    </div>
  );
}

export default App
