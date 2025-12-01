<script setup>
import { ref } from 'vue';

// 1. Declaración de variables reactivas para el formulario
const form = ref({
    nombre: '',
    email: '',
    idea_proyecto: ''
});

const statusMessage = ref('');
const isSubmitting = ref(false);

// 2. Función que maneja el envío de datos a Django
const submitForm = async () => {
    isSubmitting.value = true;
    statusMessage.value = 'Enviando...';

    // Validación básica de Vue (opcional, pero buena práctica)
    if (!form.value.nombre || !form.value.email || !form.value.idea_proyecto) {
        statusMessage.value = '❌ Por favor, completa todos los campos obligatorios.';
        isSubmitting.value = false;
        return;
    }

    try {
        // *** PUNTO CRÍTICO: Petición POST al endpoint de Django ***
        const response = await fetch('https://codew3b-api.onrender.com/api/contacto/', { 
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(form.value) // Convierte los datos de Vue a JSON
        });

        const data = await response.json();

        if (response.ok) {
            statusMessage.value = '✅ ¡Propuesta enviada con éxito! Te contactaremos pronto.';
            // Limpiar formulario después del envío exitoso
            form.value.nombre = ''; 
            form.value.email = '';
            form.value.idea_proyecto = '';
        } else {
            // Muestra el error devuelto por la vista de Django
            statusMessage.value = `❌ Error: ${data.message || 'No se pudo enviar la propuesta.'}`;
        }
    } catch (error) {
        console.error('Error de red/conexión:', error);
        statusMessage.value = '❌ Error de conexión. Asegúrate que el servidor Django esté corriendo en http://localhost:8000.';
    } finally {
        isSubmitting.value = false;
    }
};
</script>

<template>
  <section id="contacto" class="container py-5">
    <div class="row text-center mb-5">
      <div class="col-12">
        <h1 class="display-4 fw-bold text-primary-custom">Tu Puente con CodeW3b</h1>
        <p class="lead text-muted">Estamos listos para hacer que tu proyecto **destaque**. Cuéntanos sobre tu idea y empecemos a construir la presencia digital que necesitas.</p>
        <h2 class="my-4 fw-light">¡Hablemos de tu visión!</h2>
      </div>
    </div>
    
    <div class="row justify-content-center">
      
      <div class="col-lg-8 mb-4">
        <div class="card p-4 p-md-5 shadow-lg h-100 form-card">
            <h3 class="fw-bold mb-3 text-center">💡 Describe tu Proyecto</h3>
            <p class="text-center text-muted mb-4">
                Usa este espacio para detallar tus ideas, objetivos y presupuesto. Te contactaremos con una propuesta específica en menos de 24 horas.
            </p>
            
            <form @submit.prevent="submitForm">
                
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label for="nombre" class="form-label fw-bold">Nombre Completo</label>
                        <input type="text" class="form-control" id="nombre" name="nombre" v-model="form.nombre" required>
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="email" class="form-label fw-bold">Correo Electrónico</label>
                        <input type="email" class="form-control" id="email" name="email" v-model="form.email" required>
                    </div>
                </div>
                
                <div class="mb-4">
                    <label for="idea" class="form-label fw-bold">Ideas del Proyecto (Objetivos, Referencias, Presupuesto)</label>
                    <textarea class="form-control" id="idea" name="idea_proyecto" rows="7" v-model="form.idea_proyecto" required placeholder="Ej: Necesito un E-commerce para vender mis diseños. Debe tener un diseño moderno y mi presupuesto es de $XXX."></textarea>
                    <div class="form-text">Mencionar tu presupuesto y referencias nos ayuda a ser más precisos.</div>
                </div>

                <div v-if="statusMessage" class="mb-3 p-3 rounded" 
                    :class="{'bg-success-subtle text-success': statusMessage.includes('✅'), 'bg-danger-subtle text-danger': statusMessage.includes('❌')}">
                    {{ statusMessage }}
                </div>
                
                <button type="submit" class="btn btn-primary-custom btn-lg w-100 fw-bold" :disabled="isSubmitting">
                    {{ isSubmitting ? 'Enviando...' : 'Enviar Propuesta' }}
                </button>
            </form>
        </div>
      </div>
      
      <div class="col-lg-4">
        <div class="row">
            <div class="col-md-12 mb-4">
                <div class="card shadow-lg h-100 hover-card text-center">
                    <div class="card-body">
                        <h5 class="card-title fw-bold">Alternativa Rápida</h5>
                        <p class="card-text text-muted">Envíanos un email para empezar a discutir tu proyecto o cotización.</p>
                        <a href="mailto:codew3b25@gmail.com" class="btn btn-lg btn-primary-custom-light mt-3">
                            📧 codew3b25@gmail.com
                        </a>
                    </div>
                </div>
            </div>
            
            <div class="col-md-12 mb-4">
                <div class="card shadow-lg h-100 hover-card text-center">
                    <div class="card-body">
                        <h5 class="card-title fw-bold">Redes Sociales</h5>
                        <p class="card-text text-muted">Síguenos para ver nuestros últimos proyectos y tips de desarrollo.</p>
                        <div class="mt-3">
                            <a href="https://www.instagram.com/codew3b/" target="_blank" class="btn btn-outline-secondary me-2 hover-btn">
                                📸 Instagram
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
      
    </div>
  </section>
</template>

<style scoped>
/* (Mantener tus estilos CSS originales abajo) */
/* Color principal de la marca (Morado fuerte) */
:root {
 --primary-color: #6A00FF;
 --primary-light: #8a6d9e; /* Color más claro para botones secundarios */
}

.text-primary-custom {
 color: #6A00FF; 
}

/* Estilos de la tarjeta lateral (Contacto/Redes) */
.hover-card {
 transition: all 0.3s ease;
 border: none;
 background-color: #ffffff;
}

.hover-card:hover {
 transform: translateY(-5px);
 box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

/* Estilos de la tarjeta del formulario */
.form-card {
 border-top: 5px solid #6A00FF; /* Borde de color de marca para destacar */
 border-radius: 12px;
 background-color: #ffffff;
}

/* Botón Principal del Formulario */
.btn-primary-custom {
background-color: #6A00FF;
border-color: #6A00FF;
transition: background-color 0.3s ease;
}

.btn-primary-custom:hover {
background-color: #5100cc;
border-color: #5100cc;
}

/* Botón de Contacto Directo (Email) */
.btn-primary-custom-light {
background-color: #8a6d9e; 
border-color: #8a6d9e;
color: white;
}

.btn-primary-custom-light:hover {
 background-color: #6A00FF;
 border-color: #6A00FF;
}

/* Estilos para campos de formulario y botones de redes */
.form-control:focus {
 border-color: #6A00FF;
box-shadow: 0 0 0 0.25rem rgba(106, 0, 255, 0.25);
}

.hover-btn {
transition: all 0.3s ease;
border-color: #8a6d9e; /* Usar color de marca en el borde */
color: #8a6d9e;
}

.hover-btn:hover {
transform: scale(1.05);
background-color: #6A00FF;
color: white;
 border-color: #6A00FF;
}

@media (max-width: 768px) {
/* ... (Mantenemos tus estilos responsivos originales) ... */
.hover-card:hover, .hover-btn:hover {
 transform: none;
}
}
</style>