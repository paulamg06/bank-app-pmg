import { useNavigate } from 'react-router-dom'

export const navegar = () => {
    const navigate = useNavigate()

    const irAInicioSesion = () => {
        navigate(`/`)
    }

    const irARegistroUsuario = () => {
        navigate(`/register`)
    }

    const irAPaginaPrincipal = () => {
        navigate('/mainPage')
    }

    const irAMovimientos = () => {
        navigate('/movimientos')
    }

    const irACuentas = () => {
        navigate('/cuentas')
    }

    const irANuevaCuenta = () => {
        navigate('/cuentas/nueva')
    }

    const irADetalleCuentas = (idCuenta) => {
        navigate(`/cuentas/${idCuenta}`)
    }

    const irANuevoMovimiento = (idCuenta = null, nombreCuenta = "") => {
        navigate(`/movimiento/nuevo`, {
        state: {
            idCuenta,
            nombreCuenta
        }
    })
    }

    return {
        irAInicioSesion,
        irARegistroUsuario,
        irAPaginaPrincipal,
        irAMovimientos,
        irACuentas,
        irANuevaCuenta,
        irADetalleCuentas,
        irANuevoMovimiento
    }
}