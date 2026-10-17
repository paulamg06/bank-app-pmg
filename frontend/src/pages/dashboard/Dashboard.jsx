// Página de inicio de la aplicación
import { useEffect, useState } from 'react'
import BotonPrincipal from '../../components/botones/BotonPrincipal';
import { actualUser, logoutUser } from '../../api/authApi';
import { navegar } from '../../hooks/navegar';

function Dashboard() {
    const { irAMovimientos, irACuentas, irANuevoMovimiento, irANuevaCuenta, irAInicioSesion } = navegar()
    
    const [user, setUser] = useState('')
    
    async function logout() {    
        try {
            await logoutUser();
            irAInicioSesion();
        } catch (error) {
            console.error(error);
        }
    }
    
    useEffect(() => {
            actualUser(1)
                .then(data => {
                    setUser(data)
                })
                .catch((error) => {
                    console.error(error)
                });
        }, [])

    return (
        <div>
            <h1>Gestor de cuentas bancarias</h1>
            <p>Bienvenida, {user.usuario}</p>

            <nav>
                <p>¿Qué deseas hacer?</p>

                <BotonPrincipal texto="Ver movimientos" onClick={irAMovimientos} />

                <BotonPrincipal texto="Ver cuentas" onClick={irACuentas} />

                <BotonPrincipal texto="Añadir movimiento" onClick={() => irANuevoMovimiento()} />

                <BotonPrincipal texto="Añadir nueva cuenta" onClick={irANuevaCuenta} />

                <BotonPrincipal texto="Cerrar sesión" onClick={logout} />
            </nav>
        </div>
    )
}

export default Dashboard