<template>
<div class="services-container">
  <div class="header-section text-center py-5">
    <div class="container">
      <h1 class="display-5 fw-bold text-white mb-3">
        Busca el tipo de web que necesitas
      </h1>
      <p class="lead text-white-50 mb-4">
        Explora nuestros servicios y encuentra la solución perfecta para tu proyecto.
      </p>
      <div class="service-filters d-flex flex-wrap justify-content-center gap-3">
        <button
          v-for="filter in filters"
          :key="filter.key"
          :class="['btn btn-lg service-filter-btn', { 'active': selectedFilter === filter.key }]"
          @click="selectedFilter = filter.key"
        >
          {{ filter.name }}
        </button>
      </div>
      <a href="/contact" class="btn btn-success-custom mt-4">
        ¿No encuentras lo que buscas? Contáctanos
      </a>
    </div>
  </div>
  <div class="container py-5">
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-4">
      <div v-for="service in filteredServices" :key="service.id" class="col d-flex">
        <div class="card h-100 service-card shadow-sm border-0">
          <img
            :src="service.image"
            class="card-img-top service-image"
            :alt="service.title"
            @error="handleImageError"
          >
          <div class="card-body d-flex flex-column">
            <h5 class="card-title fw-bold">{{ service.title }}</h5>
            <p class="card-text text-muted mb-auto">{{ service.description }}</p>
            <div class="mt-3">
              <span class="price-tag fw-bold">
                ${{ service.priceRange.min }} - ${{ service.priceRange.max }}
              </span>
            </div>
          </div>
        </div>
      </div>
      <div v-if="filteredServices.length === 0" class="col-12 text-center my-5">
        <p class="lead text-muted">No hay servicios disponibles en esta categoría.</p>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
import { ref, computed } from 'vue';

const servicesData = ref([
    {
        id: 1,
        title: "Blog o sitio dinamico", 
        description: "sitio web informativo que ofrece contenidos actualizados regularmente (entradas de blog) sobre un tema",
        category: "blog", 
        image: "/img/blogg.png",
        priceRange: { min: 300, max: 500 }
    },
    {
        id: 2,
        title: "Portafolio Profesional Web",
        description: "Creamos una vitrina digital única y responsiva para destacar tus proyectos, habilidades y CV. Tu mejor carta de presentación.",
        category: "portafolio",
        image: "/img/portafolio.png",
        priceRange: { min: 250, max: 500 }
    },
    {
        id: 3,
        title: "E-commerce Básico",
        description: "Tienda en línea lista para vender. Incluye carrito, gestión de hasta 50 productos y pasarela de pago inicial. Comienza a facturar online.",
        category: "ecommerce",
        image: "/img/ecommerce.avif",
        priceRange: { min: 300, max: 700 }
    },
    {
        id: 4,
        title: "Landing Page Simple",
        description: "Una página web de una sola sección diseñada para un objetivo único: promocionar un producto o captar datos rápidamente. Ideal para campañas sencillas.",
        category: "landing",
        image: "/img/langin.jpg",
        priceRange: { min: 150, max: 300 }
    },
    {
        id: 5,
        title: "Web Corporativa",
        description: "Web de 5-10 páginas para posicionamiento de marca y servicios.",
        category: "corporativa",
        image: "/img/job01.png",
        priceRange: { min: 300, max: 600 }
    },
]);


const selectedFilter = ref('all');
const filters = [
    { name: 'Todos', key: 'all' },
    { name: 'Landing Page', key: 'landing' },
    { name: 'Ecommerce', key: 'ecommerce' },
    { name: 'Web Corporativa', key: 'corporativa' },
    { name: 'Blog/Contenido', key: 'blog' },    
    { name: 'Portafolio', key: 'portafolio' },
];

const filteredServices = computed(() => {
    if (selectedFilter.value === 'all') {
        return servicesData.value;
    }
    return servicesData.value.filter(service => service.category === selectedFilter.value);
});


const handleImageError = (event) => {
    event.target.src = 'https://via.placeholder.com/400x300/f0f0f0/888888?text=CodeW3b';
};
</script>

<style scoped>

.header-section {

  background: 
    linear-gradient(
      135deg,
      #845ef7 0%,
      #a777e3 47%,
      #bc8dfc 100%
    ),
    linear-gradient(
      45deg,
      transparent,
      rgba(255, 255, 255, 0.1) 50%,
      transparent
    );
  background-size: 200% 200%;
  animation: gradientShift 15s ease infinite;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.service-filter-btn {
 
  background-color: transparent;
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.4);
  transition: all 0.3s ease;
  padding: 8px 15px;
  border-radius: 50px;
  font-weight: 500;
}

.service-filter-btn:hover {
  background-color: rgba(255, 255, 255, 0.1);
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.service-filter-btn.active {
  background-color: #6b46c1;
  border-color: #6b46c1;
  color: white;
  font-weight: bold;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(107, 70, 193, 0.3);
}

.btn-success-custom {
  
  background-color: #4CAF50;
  border-color: #4CAF50;
  color: white;
  font-weight: 600;
  transition: all 0.3s ease;
  padding: 12px 30px;
  border-radius: 50px;
  box-shadow: 0 4px 8px rgba(76, 175, 80, 0.3);
}

.btn-success-custom:hover {
  background-color: #45a049;
  border-color: #45a049;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(76, 175, 80, 0.4);
}


.service-card {
  border-radius: 15px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.service-image {
  height: 180px;
  object-fit: cover;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.price-tag {
  background-color: rgba(161, 148, 227, 0.9);
  color: #333;
  padding: 5px 12px;
  border-radius: 5px;
  font-size: 1rem;
  display: inline-block;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}


@media (max-width: 768px) {
  .service-card {
    margin-bottom: 20px;
  }
  
  .service-filter-btn {
    padding: 6px 12px;
    font-size: 0.9rem;
  }
  
  .btn-success-custom {
    padding: 10px 25px;
    font-size: 0.9rem;
  }
}
</style>