// Página principal que muestra todas las cuentas bancarias.
import { useEffect, useState } from 'react'
import { obtenerCuentas } from '../../api/cuentasApi'
import BotonPrincipal from '../../components/botones/BotonPrincipal';
import BotonArriba from '../../components/botones/BotonArriba';
import BotonSeleccion from '../../components/botones/BotonSeleccion';
import { navegar } from '../../hooks/navegar';
import '../../styles/Cuentas.css'


function Cuentas() {
    const { irAPaginaPrincipal, irANuevaCuenta } = navegar()

    const [cuentas, setCuentas] = useState([])
    const [saldoTotal, setSaldoTotal] = useState(0)

    useEffect(() => {
        obtenerCuentas(1)
            .then(data => {
                setCuentas(data.cuentas)
                setSaldoTotal(data.saldo_total)
            })
            .catch((error) => {
                console.error(error);
            });
    }, [])

    return (
        <div>
            <h1>Cuentas</h1>
                        
            <BotonPrincipal texto="Volver a la página principal" onClick={irAPaginaPrincipal} />
            
            <BotonPrincipal texto="Añadir nueva cuenta" onClick={irANuevaCuenta} />

            <h2>Saldo total: {saldoTotal} €</h2>

            <table className="tabla-cuentas">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Saldo</th>
                    </tr>
                </thead>
                    
                <tbody>
                    {cuentas.map(cuenta => (
                        <tr key={cuenta.id}>
                            <td>{cuenta.nombre}</td>
                            <td>{cuenta.saldo} €</td>
                            <td><BotonSeleccion idCuenta={cuenta.id} nombreCuenta={cuenta.nombre} /></td>
                        </tr>
                    ))}
                </tbody>

            </table>

            <BotonArriba />

        </div>
    )
}

export default Cuentas