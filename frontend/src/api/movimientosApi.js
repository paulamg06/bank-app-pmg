// Conexión con las APIs de 'Movimientos' del backend
import { api } from './axios'

/* 
Endpoints de movimientos/:
urlpatterns = [
    path('', obtener_todos_movimientos),
    path('cuenta/', obtener_movimientos_por_cuenta),
    path('movimiento/', obtener_movimiento_por_id),
    path('fecha/', obtener_movimientos_por_fechas),
    path('crear/', crear_movimiento),
    path('<int:id>/', eliminar_movimiento)
]
*/

export const obtenerMovimientos = async () => {
    const response = await api.get(
        `movimientos/`
    )

    return response.data
}

export const obtenerMovimientosPorCuenta = async (cuentaId) => {
    const response = await api.get(
        `movimientos/cuenta/?cuenta=${cuentaId}`
    )

    return response.data
}

export const obtenerMovimientoPorId = async (movimientoId) => {
    const response = await api.get(
        `movimientos/movimiento/?id=${movimientoId}`
    )

    return response.data
}

export const obtenerMovimientoPorFechas = async (fechaDesde, fechaHasta) => {
    const response = await api.get(
        `movimientos/fecha/?fecha_desde=${fechaDesde}&fecha_hasta=${fechaHasta}`
    )

    return response.data
}

export const crearMovimiento = async (crearMovimientoRequest) => {
    // Falta body
    const response = await api.post(
        `movimientos/crear/`,
        crearMovimientoRequest
    )

    return response.data
}

export const eliminarMovimientoId = async (movimientoId) => {
    const response = await api.delete(
        `movimientos/eliminar/${movimientoId}/`
    )

    return response.data
}