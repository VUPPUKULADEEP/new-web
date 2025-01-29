
import viteLogo from '/vite.svg'
import './App.css'
import About from '../components/About'
import Create from '../components/Create'
import Home from '../components/Home'
import { Routes, Route } from 'react-router-dom';
import ResponsiveDrawer from '../components/Materialdrawer'

function App() {
  const mywidth = 240;
  return (
    <>
    <div className='App'>
    <ResponsiveDrawer drawerWidth={mywidth}
    content = {
      <Routes>
        <Route path='' element={<Home/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/create' element={<Create/>}/>
      </Routes>
      }/>
    </div>
    </>
  )
}

export default App
