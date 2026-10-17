import axios from 'axios';
import Cookies from "js-cookie";

// URL donde se exponen las APIs del backend
export const api = axios.create({
    baseURL: "http://localhost:8000/",
    withCredentials: true,
})

api.interceptors.request.use((config) => {
    const csrfToken = Cookies.get("csrftoken");

    if (csrfToken) {
        config.headers["X-CSRFToken"] = csrfToken;
    }

    return config;
});

export default api;