// Página que permite añadir un nuevo movimiento a una cuenta bancaria.
import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom';
import { crearCuenta } from '../../api/cuentasApi'
import BotonPrincipal from '../../components/botones/BotonPrincipal';
import InputMinimalista from '../../components/inputs/InputMinimalista';
import { navegar } from '../../hooks/navegar';

function NuevaCuenta() {
    const { irAPaginaPrincipal, irACuentas } = navegar()
    const location = useLocation();

    const [nombre, setNombre] = useState("");
    const [saldo, setSaldo] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        const cuenta = {
            nombre,
            saldo
        };

        console.log(cuenta);

        crearCuenta(cuenta)
            .then(() => {
                alert("Cuenta creada con éxito");
                irACuentas();
            })
            .catch((error) => {
                console.error(error);
            });
    };

    return (
        <div>
            <h1>Añadir nueva cuenta</h1>

            <BotonPrincipal texto="Volver a la página principal" onClick={irAPaginaPrincipal} />

            <BotonPrincipal texto="Volver a las cuentas" onClick={irACuentas} />    
        
            <form className="nueva-cuenta" onSubmit={handleSubmit}>
                <InputMinimalista
                    className="nombre" 
                    type="text" 
                    label="Nombre de la cuenta" 
                    value={nombre}
                    onChange={(e) => setNombre(e.target.value)}
                />

                <InputMinimalista
                    className="saldo" 
                    type="text" 
                    label="Saldo inicial" 
                    value={saldo}
                    onChange={(e) => setSaldo(e.target.value)}
                />

                <BotonPrincipal texto="Añadir cuenta" type="submit" />
            </form>
        </div>
    )
}

export default NuevaCuenta