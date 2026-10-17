// Página de inicio de sesión de la aplicación
import { useState, useEffect } from 'react';
import { loginUser, actualUser } from '../../api/authApi';
import BotonPrincipal from '../../components/botones/BotonPrincipal';
import InputMinimalista from '../../components/inputs/InputMinimalista';
import { navegar } from '../../hooks/navegar';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const { irAPaginaPrincipal, irARegistroUsuario } = navegar()

    useEffect(() => {
        actualUser()
            .then(data => {
                if (data.autenticado){
                    irAPaginaPrincipal();
                }
            })
            .catch((error) => {
                console.error(error)
            });
    }, [])

    const handleSubmit = async (e) => {
            e.preventDefault();
    
            const user = {
                username,
                password,
            };
    
            try {
                await loginUser(user);

                alert("Inicio de sesión exitoso");
                irAPaginaPrincipal();
            } catch (error) {
                console.error(error);
            }
        };

    return (
        <div>
            <h1>Iniciar sesión</h1>

            <form className="login-form" onSubmit={handleSubmit}>
                <InputMinimalista
                    className="username" 
                    type="username" 
                    label="Nombre de usuario" 
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <InputMinimalista
                    className="password" 
                    type="password" 
                    label="Contraseña" 
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <BotonPrincipal texto="Iniciar sesión" type="submit" />
            </form>


            <p>¿No tienes una cuenta?</p>
            <BotonPrincipal texto="Regístrate ahora" onClick={irARegistroUsuario} />
        </div>
    )
}

export default Login