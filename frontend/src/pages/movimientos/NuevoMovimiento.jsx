// Página que permite añadir un nuevo movimiento a una cuenta bancaria.
import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom';
import { crearMovimiento } from '../../api/movimientosApi'
import { obtenerCuentas } from '../../api/cuentasApi'
import BotonPrincipal from '../../components/botones/BotonPrincipal';
import InputMinimalista from '../../components/inputs/InputMinimalista';
import { navegar } from '../../hooks/navegar';
import '../../styles/NuevoMovimiento.css'

function NuevoMovimiento() {
    const { irAPaginaPrincipal, irADetalleCuentas, irACuentas } = navegar()
    const location = useLocation();

    const { idCuenta, nombreCuenta } = location.state || {}; // Por si no tuviera valor

    const [cuentas, setCuentas] = useState([])
    const [cuenta, setCuenta] = useState(nombreCuenta ?? ""); // Si no hay nombreCuenta, se inicializa como cadena vacía
    const [fecha, setFecha] = useState(new Date().toISOString().split("T")[0]); // Fecha actual en formato YYYY-MM-DD
    const [concepto, setConcepto] = useState("");
    const [cantidad, setCantidad] = useState("");
    const [tipo, setTipo] = useState("gasto");

    useEffect(() => {
            if (idCuenta == null) {
                obtenerCuentas(1)
                    .then(data => {
                        setCuentas(data.cuentas)
                    })
                }
            }, [idCuenta]);

    const handleSubmit = (e) => {
        e.preventDefault();

        const movimiento = {
            cuenta: idCuenta == null ? cuentas.find(c => c.nombre === cuenta)?.id : idCuenta,
            concepto,
            cantidad: tipo === "ingreso" ? Number(cantidad) : -Number(cantidad),
            fecha
        };

        console.log(movimiento);

        crearMovimiento(movimiento)
            .then(() => {
                alert("Movimiento creado con éxito");
                // irADetalleCuentas(idCuenta);
            });
    };

    return (
        <div>
            <h1>Añadir nuevo movimiento</h1>

            <BotonPrincipal texto="Volver a la página principal" onClick={irAPaginaPrincipal} />
            
            {idCuenta != null ? (
                <BotonPrincipal texto="Volver a la cuenta" onClick={() => irADetalleCuentas(idCuenta)} />
            ) : (
                <BotonPrincipal texto="Volver a las cuentas" onClick={irACuentas} />
            )}           
        
            <form className="nuevo-movimiento" onSubmit={handleSubmit}>
                {idCuenta == null ? (
                    <InputMinimalista
                        className="cuenta" 
                        type="select"
                        label="Cuenta" 
                        value={cuenta}
                        onChange={(e) => setCuenta(e.target.value)}                    
                    >
                        {cuentas.map(c => (
                            <option key={c.id}
                             className={c.id} value={c.nombre}>{c.nombre}</option>
                        ))}
                    </InputMinimalista>
                ) : (
                    <InputMinimalista
                        className="cuenta" 
                        type="text" 
                        label="Cuenta" 
                        value={nombreCuenta ?? ""}
                        onChange={(e) => setCuenta(e.target.value)}
                        disabled={true}
                    />
                )}


                <InputMinimalista
                    className="fecha" 
                    type="date" 
                    label="Fecha" 
                    value={fecha}
                    onChange={(e) => setFecha(e.target.value)}
                />

                <InputMinimalista
                    className="concepto" 
                    type="text" 
                    label="Concepto" 
                    value={concepto}
                    onChange={(e) => setConcepto(e.target.value)}
                />

                <InputMinimalista
                    className={tipo === "ingreso" ? "cantidad-ingreso": "cantidad-gasto"} 
                    type="text" 
                    label="Cantidad" 
                    value={cantidad}
                    onChange={(e) => setCantidad(e.target.value)}
                />

                <InputMinimalista
                    type="select" 
                    label="Tipo" 
                    value={tipo}
                    onChange={(e) => setTipo(e.target.value)}
                    className={tipo === "ingreso" ? "select-ingreso" : "select-gasto"}
                >
                    <option className="gasto" value="gasto">Gasto</option>
                    <option className="ingreso" value="ingreso">Ingreso</option>
                </InputMinimalista>

                <BotonPrincipal texto="Añadir movimiento" type="submit" />
            </form>
        </div>
    )
}

export default NuevoMovimiento