import styled from 'styled-components';
import { navegar } from '../../hooks/navegar';
import { Plus, Search, Trash } from 'lucide-react';

function eliminarCuenta(idCuenta) {
      <dialog>
          <h2>¿Estás seguro de que deseas eliminar esta cuenta?</h2>
          <p>Esta acción no se puede deshacer.</p>
          <button >Sí, eliminar</button>
          <button >Cancelar</button>
      </dialog>
}

const BotonSeleccion = ({ idCuenta, nombreCuenta }) => {
  const { irADetalleCuentas, irANuevoMovimiento } = navegar();

  return (
    <StyledWrapper>
      <div className="button-container">
        <button className="button" data-tooltip="Nuevo movimiento" onClick={() => irANuevoMovimiento(idCuenta, nombreCuenta)}>
          <Plus className="icon" size={20} />
        </button>
        <button className="button" data-tooltip="Detalles" onClick={() => irADetalleCuentas(idCuenta)}>
          <Search className="icon" size={18} />
        </button>
        <button className="button" data-tooltip="Eliminar" onClick={() => eliminarCuenta(idCuenta)}>
          <Trash className="icon" size={18} />
        </button>
      </div>
    </StyledWrapper>
  );
}

const StyledWrapper = styled.div`
  .button-container {
    display: flex;
    background-color: #4B94E2;
    width: 200px;
    height: 40px;
    align-items: center;
    justify-content: space-around;
    border-radius: 10px;
    box-shadow: #00000059 0px 5px 15px,
          #103965 5px 10px 15px;
  }

  .button {
    outline: 0 !important;
    border: 0 !important;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    transition: all ease-in-out 0.3s;
    cursor: pointer;
  }

  .button:hover {
    transform: translateY(-3px);
  }

  .button::after {
    content: attr(data-tooltip);
    position: absolute;
    bottom: 45px;

    background-color: #4B94E2;
    color: white;
    padding: 5px 8px;
    border-radius: 5px;

    font-size: 12px;
    white-space: nowrap;

    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s;
  }

  .button:hover::after {
      opacity: 1;
  }
`;

export default BotonSeleccion;
