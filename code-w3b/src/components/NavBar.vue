<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">CodeW3b</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/" active-class="active">Inicio</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/servicios" active-class="active">Servicios</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/contact" active-class="active">Contacto</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.navbar:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.nav-link {
  transition: all 0.3s ease;
  padding: 0.5rem 1rem;
}

.nav-link:hover {
  color: #fff !important;
  transform: translateY(-2px);
}

.nav-link.active {
  color: #fff;
  border-bottom: 2px solid rgba(255, 255, 255, 0.5);
}

@media (max-width: 768px) {
  .nav-link {
    padding: 0.5rem;
  }
  
  .nav-link:hover {
    transform: none;
  }
}
</style>