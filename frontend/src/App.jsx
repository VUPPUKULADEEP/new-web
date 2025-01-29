
import viteLogo from '/vite.svg'
import './App.css'
import About from '../components/About'
import Create from '../components/Create'
import Home from '../components/Home'
import { Routes, Route } from 'react-router-dom';
import ResponsiveDrawer from '../components/Materialdrawer'

function App() {

  return (
    <>
    <div className='App'>
      <Routes>
        <Route path='' element={<ResponsiveDrawer/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/create' element={<Create/>}/>
      </Routes>
    </div>
    </>
  )
}

export default App
