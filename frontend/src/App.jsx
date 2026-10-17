import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { useEffect } from "react";
import api from "./api/axios"


import Login from './pages/login/Login'
import Register from './pages/register/Register'
import Dashboard from './pages/dashboard/Dashboard'
import Cuentas from './pages/cuentas/Cuentas'
import DetalleCuentas from './pages/cuentas/DetalleCuentas'
import NuevaCuenta from './pages/cuentas/nuevaCuenta'
import Movimientos from './pages/movimientos/Movimientos'
import NuevoMovimiento from './pages/movimientos/NuevoMovimiento'

function App() {
    useEffect(() => {
        api.get("/auth/csrf/");
    }, []);

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/mainPage" element={<Dashboard />} />
                <Route path="/cuentas" element={<Cuentas />} />
                <Route path="/cuentas/:id" element={<DetalleCuentas />} />
                <Route path="/cuentas/nueva" element={<NuevaCuenta />} />
                <Route path="/movimientos" element={<Movimientos />} />
                <Route path="/movimiento/nuevo" element={<NuevoMovimiento />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App