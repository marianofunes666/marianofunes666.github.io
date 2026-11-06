(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  var form = document.getElementById('wa-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var nombre = form.nombre.value.trim();
      var area = form.area.value;
      var msg = form.mensaje.value.trim();
      var texto = 'Hola Dr. Funes, mi nombre es ' + nombre + '. Quisiera hacer una consulta sobre ' + area + '.';
      if (msg) texto += ' ' + msg;
      window.open('https://wa.me/' + form.getAttribute('data-wa') + '?text=' + encodeURIComponent(texto), '_blank', 'noopener');
    });
  }

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
