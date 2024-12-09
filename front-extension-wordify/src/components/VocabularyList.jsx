import React from 'react'

const VocabularyList = ( {vocabulary} ) => {
  return (
    <div className='mt-4'>
        <h2> Vocabulario Guardado: </h2>
        <ul>
            {
                vocabulary.map((word, index) => (
                    <li key={index}>{word}</li>
                ))
            }
        </ul>
    </div>
  )
}

export default VocabularyList
