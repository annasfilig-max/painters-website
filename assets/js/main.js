/* ============================================================
   PAINTERS TEMPLATE — MAIN.JS
   Vanilla JS: mobile menu, FAQ, lightbox, forms,
   count-up, carousel, gallery filter, active nav
   ============================================================ */

(function () {
  'use strict';

  /* ── Helpers ────────────────────────────────────────────── */
  const qs  = (sel, ctx = document) => ctx.querySelector(sel);
  const qsa = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];
  const on  = (el, ev, fn, opts) => el && el.addEventListener(ev, fn, opts);

  /* ── Active nav ─────────────────────────────────────────── */
  function setActiveNav() {
    const path = window.location.pathname.split('/').pop() || 'index.html';
    qsa('[data-nav-link]').forEach(link => {
      const href = (link.getAttribute('href') || '').split('/').pop();
      if (href === path || (path === '' && href === 'index.html')) {
        link.setAttribute('aria-current', 'page');
      }
    });
  }

  /* ── Mobile menu ────────────────────────────────────────── */
  function initMobileMenu() {
    const btn  = qs('#hamburger');
    const menu = qs('#mobile-menu');
    if (!btn || !menu) return;

    function open() {
      btn.setAttribute('aria-expanded', 'true');
      menu.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    }
    function close() {
      btn.setAttribute('aria-expanded', 'false');
      menu.classList.remove('is-open');
      document.body.style.overflow = '';
    }

    on(btn, 'click', () => {
      btn.getAttribute('aria-expanded') === 'true' ? close() : open();
    });

    // Close on link tap
    qsa('a', menu).forEach(link => on(link, 'click', close));

    // Close on Esc
    on(document, 'keydown', e => { if (e.key === 'Escape') close(); });
  }

  /* ── FAQ accordion ──────────────────────────────────────── */
  function initFAQ() {
    const questions = qsa('.faq-question');
    if (!questions.length) return;

    questions.forEach(btn => {
      on(btn, 'click', () => {
        const expanded = btn.getAttribute('aria-expanded') === 'true';
        const answer   = qs(`#${btn.getAttribute('aria-controls')}`);

        // Close all
        questions.forEach(q => {
          q.setAttribute('aria-expanded', 'false');
          const a = qs(`#${q.getAttribute('aria-controls')}`);
          if (a) a.classList.remove('is-open');
        });

        // Toggle current
        if (!expanded) {
          btn.setAttribute('aria-expanded', 'true');
          if (answer) answer.classList.add('is-open');
        }
      });
    });
  }

  /* ── Gallery lightbox ───────────────────────────────────── */
  function initLightbox() {
    const lb     = qs('#lightbox');
    const lbImg  = qs('#lightbox-img');
    const lbPrev = qs('#lightbox-prev');
    const lbNext = qs('#lightbox-next');
    const lbClose= qs('#lightbox-close');
    const items  = qsa('.gallery-item');
    if (!lb || !items.length) return;

    let current = 0;
    const images = items.map(item => ({
      src: qs('img', item)?.src || '',
      alt: qs('img', item)?.alt || ''
    }));

    function show(index) {
      current = (index + images.length) % images.length;
      lbImg.src = images[current].src;
      lbImg.alt = images[current].alt;
    }

    function openLB(index) {
      show(index);
      lb.classList.add('is-open');
      lb.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      lbClose.focus();
    }

    function closeLB() {
      lb.classList.remove('is-open');
      lb.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      items[current]?.focus();
    }

    items.forEach((item, i) => {
      item.setAttribute('tabindex', '0');
      item.setAttribute('role', 'button');
      item.setAttribute('aria-label', `View full size: ${qs('img', item)?.alt || 'gallery image'}`);
      on(item, 'click', () => openLB(i));
      on(item, 'keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openLB(i); } });
    });

    on(lbClose, 'click', closeLB);
    on(lbPrev,  'click', () => show(current - 1));
    on(lbNext,  'click', () => show(current + 1));

    // Overlay click closes
    on(lb, 'click', e => { if (e.target === lb) closeLB(); });

    on(document, 'keydown', e => {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape')     closeLB();
      if (e.key === 'ArrowLeft')  show(current - 1);
      if (e.key === 'ArrowRight') show(current + 1);
    });
  }

  /* ── Gallery filter ─────────────────────────────────────── */
  function initGalleryFilter() {
    const btns = qsa('.filter-btn');
    if (!btns.length) return;

    btns.forEach(btn => {
      on(btn, 'click', () => {
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        // Visual-only in template — all items shown
      });
    });
  }

  /* ── Count-up animation ─────────────────────────────────── */
  function initCountUp() {
    const els = qsa('[data-countup]');
    if (!els.length) return;

    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el     = entry.target;
        const target = parseFloat(el.dataset.countup);
        const suffix = el.dataset.suffix || '';
        const prefix = el.dataset.prefix || '';
        const dec    = el.dataset.decimals ? parseInt(el.dataset.decimals) : 0;
        const dur    = 1800;

        if (prefersReduced) {
          el.textContent = prefix + target.toFixed(dec) + suffix;
          observer.unobserve(el);
          return;
        }

        let start  = null;
        const step = ts => {
          if (!start) start = ts;
          const prog = Math.min((ts - start) / dur, 1);
          // ease-out-cubic
          const ease = 1 - Math.pow(1 - prog, 3);
          el.textContent = prefix + (ease * target).toFixed(dec) + suffix;
          if (prog < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        observer.unobserve(el);
      });
    }, { threshold: 0.3 });

    els.forEach(el => observer.observe(el));
  }

  /* ── Testimonial carousel ───────────────────────────────── */
  function initCarousel() {
    const track  = qs('#testimonials-track');
    const btnPrev= qs('#carousel-prev');
    const btnNext= qs('#carousel-next');
    const dots   = qsa('.carousel-dot');
    if (!track) return;

    const cards    = qsa('.testimonial-card', track);
    let current    = 0;
    let perView    = 1;

    function getPerView() {
      if (window.innerWidth >= 1024) return 3;
      if (window.innerWidth >= 768)  return 2;
      return 1;
    }

    function update() {
      perView       = getPerView();
      const maxIdx  = Math.max(0, cards.length - perView);
      current       = Math.min(current, maxIdx);
      const pct     = current * (100 / cards.length);
      track.style.transform = `translateX(-${pct}%)`;
      dots.forEach((d, i) => d.classList.toggle('active', i === current));
    }

    on(btnPrev, 'click', () => { current = Math.max(0, current - 1); update(); });
    on(btnNext, 'click', () => {
      perView = getPerView();
      const maxIdx = Math.max(0, cards.length - perView);
      current = Math.min(current + 1, maxIdx);
      update();
    });

    dots.forEach((d, i) => on(d, 'click', () => { current = i; update(); }));

    window.addEventListener('resize', update, { passive: true });
    update();
  }

  /* ── Form validation ────────────────────────────────────── */
  function validateEmail(v) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim());
  }
  function validatePhone(v) {
    return /^[\d\s().+\-]{7,}$/.test(v.trim());
  }

  function showError(field, msg) {
    field.classList.add('error');
    let err = qs(`#${field.id}-error`);
    if (!err) {
      err = document.createElement('p');
      err.id = `${field.id}-error`;
      err.className = 'form-error';
      err.setAttribute('role', 'alert');
      field.parentNode.appendChild(err);
    }
    err.textContent = msg;
    err.classList.add('show');
    field.setAttribute('aria-describedby', err.id);
    field.setAttribute('aria-invalid', 'true');
  }

  function clearError(field) {
    field.classList.remove('error');
    const err = qs(`#${field.id}-error`);
    if (err) err.classList.remove('show');
    field.removeAttribute('aria-invalid');
  }

  function validateField(field) {
    const val  = field.value.trim();
    const type = field.type;
    const req  = field.hasAttribute('required');

    if (req && !val) {
      showError(field, `${field.dataset.label || 'This field'} is required.`);
      return false;
    }
    if (val && type === 'email' && !validateEmail(val)) {
      showError(field, 'Please enter a valid email address.');
      return false;
    }
    if (val && type === 'tel' && !validatePhone(val)) {
      showError(field, 'Please enter a valid phone number.');
      return false;
    }
    clearError(field);
    return true;
  }

  function showSuccess(form) {
    const wrapper = form.closest('[data-form-wrapper]') || form.parentNode;
    wrapper.innerHTML = `
      <div class="form-success" role="alert" aria-live="polite">
        <div class="success-icon">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
        </div>
        <h3>Message Sent!</h3>
        <p>Thanks — we'll be in touch within one business day.</p>
      </div>`;
  }

  function initForms() {
    qsa('[data-validate]').forEach(form => {
      const fields = qsa('input:not([type=hidden]):not([type=submit]), textarea, select', form);

      // Inline validation on blur
      fields.forEach(f => {
        on(f, 'blur', () => validateField(f));
        on(f, 'input', () => { if (f.classList.contains('error')) validateField(f); });
      });

      on(form, 'submit', async e => {
        e.preventDefault();

        // Honeypot check
        const honey = qs('[name="_gotcha"]', form);
        if (honey && honey.value) return;

        let valid = true;
        fields.forEach(f => { if (!validateField(f)) valid = false; });
        if (!valid) {
          const firstErr = qs('.error', form);
          if (firstErr) firstErr.focus();
          return;
        }

        const submitBtn = qs('[type=submit]', form);
        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.textContent = 'Sending…';
        }

        try {
          const action = form.action;
          const body   = new FormData(form);

          if (action && !action.includes('YOUR_FORM_ID')) {
            await fetch(action, { method: 'POST', body, headers: { Accept: 'application/json' } });
          }
          showSuccess(form);
        } catch {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = submitBtn.dataset.label || 'Send Message';
          }
          // Show a generic error notice
          let notice = qs('#form-send-error', form);
          if (!notice) {
            notice = document.createElement('p');
            notice.id = 'form-send-error';
            notice.style.cssText = 'color:var(--color-error);font-size:.875rem;margin-top:.75rem;';
            notice.setAttribute('role', 'alert');
            form.appendChild(notice);
          }
          notice.textContent = 'Something went wrong. Please call us or try again.';
        }
      });
    });
  }

  /* ── Newsletter form ────────────────────────────────────── */
  function initNewsletter() {
    qsa('[data-newsletter]').forEach(form => {
      on(form, 'submit', e => {
        e.preventDefault();
        const input = qs('input[type=email]', form);
        if (!input || !validateEmail(input.value)) {
          showError(input || form, 'Please enter a valid email.');
          return;
        }
        form.innerHTML = '<p style="color:var(--color-success);font-weight:600;">You\'re on the list. We\'ll be in touch!</p>';
      });
    });
  }

  /* ── Init ───────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', () => {
    setActiveNav();
    initMobileMenu();
    initFAQ();
    initLightbox();
    initGalleryFilter();
    initCountUp();
    initCarousel();
    initForms();
    initNewsletter();
  });

})();
