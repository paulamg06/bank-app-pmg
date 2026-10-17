// Página que muestra el detalle de una cuenta bancaria.
import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { obtenerCuentaPorId } from '../../api/cuentasApi'
import { obtenerMovimientosPorCuenta } from '../../api/movimientosApi'
import { navegar } from '../../hooks/navegar';
import { formatearFecha, transformarFechaIso } from '../../hooks/fecha';
import BotonPrincipal from '../../components/botones/BotonPrincipal';
import BotonArriba from '../../components/botones/BotonArriba';

function DetalleCuentas() {
    const { irAPaginaPrincipal, irACuentas, irANuevoMovimiento } = navegar()

    const { id } = useParams()

    /* Detalle cuenta */
    const [cuenta, setCuenta] = useState(null)

    useEffect(() => {
        obtenerCuentaPorId(id)
            .then(data => {
                setCuenta(data)
            })
            .catch((error) => {
                console.error(error);
            });
    }, [])

    /* Movimientos de la cuenta */
    const [movimientos, setMovimientos] = useState([])

    useEffect(() => {
        obtenerMovimientosPorCuenta(id)
            .then(data => {
                setMovimientos(data)
            })
    }, [])

    return (
        <div>
            <h1>{cuenta?.nombre}</h1>

            <nav>
                <BotonPrincipal texto="Volver a la página principal" onClick={irAPaginaPrincipal} />
                <BotonPrincipal texto="Volver a las cuentas" onClick={irACuentas} />
                <BotonPrincipal texto="Añadir movimiento" onClick={() => irANuevoMovimiento(id, cuenta?.nombre)} />
            </nav>

            <h2>{cuenta?.saldo} €</h2>

            <p>Creado el {transformarFechaIso(cuenta?.fecha_creacion)}</p>
            <p>Modificado por última vez el {transformarFechaIso(cuenta?.fecha_actualizacion)}</p>

            <h2>Movimientos</h2>
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

export default DetalleCuentas