import React from 'react';

const Component1 = () => {
  return (
    <>
      <div className='App'>
      <h1>AdventureCompass</h1>
      <form onSubmit={handleSubmit}>
      <label id="date" for="departureDate">Departure Date</label>
        <input className='input'
          type="text"
          name="departureDate"
          value={dataForm.departureDate}
          onChange={handleFormInput}
          placeholder="dd/mm/aaaa"
          required
        />
        <label id="date" for="returnDate">Return Date</label>
        <input  className='input'
          type="text"
          name="returnDate"
          value={dataForm.returnDate}
          onChange={handleFormInput}
          placeholder="dd/mm/aaaa"
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
        <input     className='input'
          type="text"
          name="arrivalCity"
          value={dataForm.arrivalCity}
          onChange={handleFormInput}
          placeholder="Arrival city..."
          required
        />
        <button type="submit">Send</button>
      </form>
    </div>
    </>
  );
};

export default Component1;
