## First
 npx create-react-app marvel_frontend

 ## change app.js
 import React, { useState, useEffect } from 'react'

const App = () => {
  return (
    <>
      <h1>App</h1>
    </>
  )
}

export default App

## START APP
 npm start

 ## add axios
 npm i axios

 import axios from 'axios'

 const getPeople = () => {
 axios
   .get('http://localhost:8000/api/contacts')
   .then(
     (response) => setPeople(response.data),
     (err) => console.error(err)
   )
   .catch((error) => console.error(error))
}

useEffect(() => {
 getPeople()
}, [])

## map over results
 return (

  <div className="people">

    {people.map((person) => {
      return (
        <div className="person" key={person.id}>
          <h4>Name: {person.name}</h4>
          <h5>Age: {person.age}</h5>
        </div>
      )
  })}
</div>
  )
}