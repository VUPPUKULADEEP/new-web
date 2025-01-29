
import viteLogo from '/vite.svg'

import About from '../components/About'
import Create from '../components/Create'
import Home from '../components/Home'
import { Routes, Route } from 'react-router-dom';
import ResponsiveDrawer from '../components/Materialdrawer'

function App() {

  return (
    <>
    <div className='App'>
    <ResponsiveDrawer/>
      <Routes>
        <Route path='' element={<Home/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/create' element={<Create/>}/>
      </Routes>
    </div>
    </>
  )
}

export default App
