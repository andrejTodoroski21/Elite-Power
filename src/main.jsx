import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
// import Home from './components/Home.jsx'
import Workouts from './Components/Workouts.jsx'

import './index.css'

import { createBrowserRouter, RouterProvider } from 'react-router-dom'


//ROUTES
const routes = [
  {
    path: "/",
    element: <App />,
    children: [
      // {
      //   index: true,
      //   element: <Home />
      // },
      {
        path: "workouts",
        element: <Workouts />
      },
    ]
  }
]

const router = createBrowserRouter(routes)

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
