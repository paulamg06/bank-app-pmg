// Conexión con las APIs de 'Cuentas' del backend
import { api } from './axios'

/* 
Endpoints de cuentas/:
urlpatterns = [
    path('', obtener_cuentas),
    path('', obtener_cuentas),
    path('crear/', crear_cuenta),
    path('eliminar/<int:id>/', eliminar_cuenta),
]
*/

export const obtenerCuentas = async () => {
    const response = await api.get(
        `cuentas/`
    )

    return response.data
}

export const obtenerCuentaPorId = async (cuentaId) => {
    const response = await api.get(
        `cuentas/?id=${cuentaId}`
    )
    .catch(error => console.log(error));

    return response.data
}

export const eliminarCuentaPorId = async (cuentaId) => {
    const response = await api.delete(
        `cuentas/eliminar/${cuentaId}`
    )

    return response.data
}

export const crearCuenta = async (crearCuentaRequest) => {
    const response = await api.post(
        `cuentas/crear/`,
        crearCuentaRequest
    )

    return response.data
}