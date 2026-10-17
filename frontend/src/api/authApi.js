// Conexión con las APIs de 'Cuentas' del backend
import { api } from './axios'

/* 
Endpoints de auth/:
    path('register/', register_user),
    path('login/', login_user),
    path('me/', actual_user),
    path('logout/', logout_user),
*/

export const registerUser = async (registerUserRequest) => {
    const response = await api.post(
        `auth/register/`,
        registerUserRequest
    )

    return response.data
}

export const loginUser = async (loginUserRequest) => {
    const response = await api.post(
        `auth/login/`,
        loginUserRequest
    );

    return response.data
}

export const actualUser = async () => {
    const response = await api.get("auth/me/");

    return response.data
}

export const logoutUser = async () => {
    const response = await api.post("auth/logout/");

    return response.data
}
