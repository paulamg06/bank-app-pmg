// Página principal que muestra todos los movimientos por orden cronológico.
import { useEffect, useState } from 'react'
import { obtenerMovimientos } from '../../api/movimientosApi'
import { navegar } from '../../hooks/navegar';
import { formatearFecha } from '../../hooks/fecha';
import BotonArriba from '../../components/botones/BotonArriba';
import BotonPrincipal from '../../components/botones/BotonPrincipal';
import '../../styles/Movimientos.css'

function Movimientos() {
    const { irAPaginaPrincipal, irANuevoMovimiento } = navegar()

    const [movimientos, setMovimientos] = useState([])

    useEffect(() => {
        obtenerMovimientos(1)
            .then(setMovimientos)
    }, [])

    return (
        <div>
            <h1>Movimientos</h1>

            <BotonPrincipal texto="Volver a la página principal" onClick={irAPaginaPrincipal} />
            <BotonPrincipal texto="Añadir movimiento" onClick={() => irANuevoMovimiento()} />

            {movimientos.map(fecha => (
                <div key={fecha.fecha}>
                    <header className="fecha_movimientos">
                        <h2>{formatearFecha(fecha.fecha)}</h2>
                        <p className={`${fecha.balance < 0 ? "gasto" : "ingreso"}`}>{fecha.balance} €</p>
                    </header>
                    {fecha.movimientos.map(movimiento => (
                        <div className={`movimientos ${movimiento.cantidad < 0 ? "gasto" : "ingreso"}`} key={movimiento.id}>
                            <h3>{movimiento.concepto}</h3>
                            <p>
                                {movimiento.cantidad} €, {movimiento.cuenta_nombre}
                            </p>
                        </div>
                    ))}
                </div>
            ))}

            <BotonArriba />

        </div>
    )
}

export default Movimientos