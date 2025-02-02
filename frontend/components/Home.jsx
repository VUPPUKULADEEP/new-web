import React from 'react'
import './About.css'
import axios from 'axios';
const Home = () => {
  const call = async () => {
    try {
      const response = await axios.get( 'http://127.0.0.1:8000/project');
      console.log('Data:', response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className='container'>
      <p>hello home</p>
      <button onClick={call}>call</button>
    </div>
  )
}

export default Home
