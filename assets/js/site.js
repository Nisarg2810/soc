(function () {
  var doc = document.documentElement;
  doc.classList.add('js');

  // Header: turn solid after the hero
  var header = document.querySelector('.site-header');
  function onScroll() {
    if (!header) return;
    header.classList.toggle('solid', window.scrollY > 40);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var menuBtn = document.querySelector('.menu-btn');
  if (menuBtn) {
    menuBtn.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.body.classList.contains('menu-open')) menuBtn.click();
    });
  }

  // Reveal on scroll
  var items = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && items.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Services: image follows the cursor
  var list = document.querySelector('.svc-list[data-preview]');
  if (list && window.matchMedia('(hover: hover) and (min-width: 900px)').matches) {
    var box = document.createElement('div');
    box.className = 'svc-preview';
    box.setAttribute('aria-hidden', 'true');
    var im = document.createElement('img');
    im.alt = '';
    box.appendChild(im);
    document.body.appendChild(box);
    list.querySelectorAll('a[data-img]').forEach(function (a) {
      a.addEventListener('mouseenter', function () { im.src = a.getAttribute('data-img'); box.classList.add('on'); });
      a.addEventListener('mouseleave', function () { box.classList.remove('on'); });
      a.addEventListener('mousemove', function (e) {
        box.style.left = (e.clientX + 32) + 'px';
        box.style.top = (e.clientY - 180) + 'px';
      });
    });
  }

  // Project filters
  var filters = document.querySelector('.filters');
  if (filters) {
    var cards = document.querySelectorAll('.pgrid .pcard[data-cat]');
    filters.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-filter]');
      if (!b) return;
      var f = b.getAttribute('data-filter');
      filters.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      cards.forEach(function (c) {
        c.hidden = !(f === 'all' || c.getAttribute('data-cat').split(' ').indexOf(f) > -1);
      });
    });
  }

  // Enquiry form: compose a WhatsApp message (static hosting has no server)
  var form = document.querySelector('#enquiry');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('.form-status');
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var d = new FormData(form);
      var lines = [
        'Hello Shree Ohm Creation, I would like to discuss a project.',
        'Name: ' + d.get('name'),
        'Phone: ' + d.get('phone'),
        'Area: ' + (d.get('area') || '-'),
        'Project: ' + d.get('type'),
        'Budget: ' + (d.get('budget') || '-'),
        'Details: ' + (d.get('message') || '-')
      ];
      var url = 'https://wa.me/' + form.getAttribute('data-wa') + '?text=' + encodeURIComponent(lines.join('\n'));
      window.open(url, '_blank', 'noopener');
      if (status) status.textContent = 'WhatsApp has opened with your details. Press send and we will reply within one working day.';
    });
  }

  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
