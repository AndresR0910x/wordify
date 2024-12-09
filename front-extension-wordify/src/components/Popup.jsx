import React from 'react'
import { Dialog, DialogTitle, DialogContent, DialogActions, Button, Typography } from '@mui/material';


const  Popup = ( { isOpen, word, onSave, onCancel } ) => {
  
  return (
      <Dialog open={isOpen} onClose={onCancel} className="flex justify-center items-center">
        <DialogTitle>¿Guardar palabra?</DialogTitle>
        <DialogContent>
          <Typography variant="body1">
            ¿Quieres agregar la palabra "<strong>{word}</strong>" a tu vocabulario?
          </Typography>
        </DialogContent>
        <DialogActions>
          <Button onClick={onSave} color="primary" variant="contained">
            Guardar
          </Button>
          <Button onClick={onCancel} color="secondary" variant="contained">
            Cancelar
          </Button>
        </DialogActions>
      </Dialog>
  );

}

export default Popup
