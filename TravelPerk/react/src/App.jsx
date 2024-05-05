import React, { useState } from 'react';
import './App.css';

function App() {
  const [dataForm, setDataForm] = useState({
    departureDate: '',
    returnDate: '',
    departureCity: '',
    arrivalCity: ''
  });
   //función para enviar al backend
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(dataForm);

    fetch('http://127.0.0.1:8000/api/v1/', { //dirección del backend
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(dataForm)
    })
      .then(response => {
        if (response.ok) {
          console.log('Data sent successfully');
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => {
        console.log(data["list_go"]);
        console.log(data["list_come_back"]);
        console.log(data["list_days"]);
        console.log(data["list_activities"]);

        setDataForm({
          departureDate: '',
          returnDate: '',
          departureCity: '',
          arrivalCity: ''
        });
      })
      .catch(error => {
        console.error('Error sending dates.', error);
      });
  };

  const handleFormInput = (e) => {
    const { name, value } = e.target;
    setDataForm({
      ...dataForm,
      [name]: value
    });
  };

  return (
    <div className='App'>
      <h1>AdventureCompass</h1>
      <form onSubmit={handleSubmit}>
        <input className='input'
          type="text"
          name="departureDate"
          value={dataForm.departureDate}
          onChange={handleFormInput}
          placeholder="Departure date:dd/mm/aaaa"
          required
        />
        <input  className='input'
          type="text"
          name="returnDate"
          value={dataForm.returnDate}
          onChange={handleFormInput}
          placeholder="Return date: dd/mm/aaaa"
          required
        />
        <input   className='input'
          type="text"
          name="departureCity"
          value={dataForm.departureCity}
          onChange={handleFormInput}
          placeholder="Departure city..."
          required
        />
        <input   className='input'
          type="text"
          name="arrivalCity"
          value={dataForm.arrivalCity}
          onChange={handleFormInput}
          placeholder="Arrival city..."
          required
        />
        <button type="submit">Send</button>
        <a href="../result.html">Results</a>
      </form>
    </div>
  );
}

export default App;