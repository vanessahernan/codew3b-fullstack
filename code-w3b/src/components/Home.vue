<template>
    <div>
        <div class="presentacion-home d-flex flex-column align-items-center justify-content-center text-center vh-100 text-white">
            
            <h1 class="display-1 fw-bold mb-3">CodeW3b</h1>
            
            <h2 class="lead fs-3 fw-light mt-4 px-5 mx-auto" style="max-width: 800px;">
                Damos vida a tus ideas digitales. Tu proyecto web, visible y funcional desde hoy.
            </h2>
            
            <router-link to="/contact" class="btn btn-warning btn-lg fw-bold mt-5 px-5 py-3 shadow-lg pulse-button">
                Empieza tu Proyecto Hoy
            </router-link>
            
        </div>

        <div class="guide-section py-5">
            <div class="container">
                <h2 class="text-center display-5 fw-bold mb-4">
                    🚀 Nuestro Proceso de Trabajo
                </h2>
                <p class="lead text-center text-muted mb-5">
                    4 pasos sencillos para transformar tu idea en una web profesional.
                </p>

                <div class="row g-4">
                    <div class="col-lg-3 col-md-6">
                        <div class="card p-4 h-100 step-card">
                            <span class="step-number">1</span>
                            <h4 class="fw-bold mt-2">Definición de Meta</h4>
                            <p class="text-muted">Establecemos el objetivo principal: ¿Vender, captar leads, o generar autoridad?</p>
                        </div>
                    </div>
                    
                    <div class="col-lg-3 col-md-6">
                        <div class="card p-4 h-100 step-card">
                            <span class="step-number">2</span>
                            <h4 class="fw-bold mt-2">Mapeo y Estructura</h4>
                            <p class="text-muted">Diseñamos el mapa del sitio y las secciones clave para guiar al usuario.</p>
                        </div>
                    </div>

                    <div class="col-lg-3 col-md-6">
                        <div class="card p-4 h-100 step-card">
                            <span class="step-number">3</span>
                            <h4 class="fw-bold mt-2">Contenido y Diseño</h4>
                            <p class="text-muted">Recopilamos tus textos, imágenes y marca, y comenzamos el diseño visual.</p>
                        </div>
                    </div>

                    <div class="col-lg-3 col-md-6">
                        <div class="card p-4 h-100 step-card">
                            <span class="step-number">4</span>
                            <h4 class="fw-bold mt-2">Desarrollo y Entrega</h4>
                            <p class="text-muted">Codificación final, pruebas exhaustivas y lanzamiento de tu web al público.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeView'
}
</script>

<style scoped>

.presentacion-home {
    background: linear-gradient(135deg, #1A72FF 0%, #6A00FF 100%); 
    height: 100vh;
    width: 100%;
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.4); 
}

.presentacion-home h1 {
    font-size: 5rem;
    transition: transform 0.3s ease;
}

.presentacion-home h1:hover {
    transform: scale(1.05);
}


.pulse-button {
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 193, 7, 0.7); }
    70% { transform: scale(1.05); box-shadow: 0 0 0 15px rgba(255, 193, 7, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 193, 7, 0); }
}


.guide-section {
    background-color: #f8f9fa;
}

.step-card {
    background-color: white;
    border: none;
    border-radius: 12px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-align: center;
}

.step-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.step-number {
   
    display: inline-flex;
    justify-content: center;
    align-items: center;
    width: 60px;
    height: 60px;
    font-size: 2rem;
    font-weight: 700;
    color: white;
    background-color: #6A00FF;
    border-radius: 50%;
    margin-bottom: 1rem;
    box-shadow: 0 4px 10px rgba(106, 0, 255, 0.3);
}

@media (max-width: 768px) {
    .presentacion-home h1 {
        font-size: 3rem; 
    }
    .presentacion-home h2 {
        font-size: 1.5rem;
        padding: 0 15px; 
    }
    .presentacion-home .btn-lg {
        font-size: 1.1rem;
        padding: 10px 25px;
    }
    .step-card {
        text-align: left; 
    }
}
</style>