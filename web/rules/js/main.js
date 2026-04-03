/* ═══════════════════════════════════════════════════════════════
   THE AETHERIC CODEX — Interactive Systems
   Navigation, particles, scroll reveals, page transitions
   ═══════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ── Page Registry ──────────────────────────────────────────
  const PAGES = [
    { id: 'welcome',       file: 'index.html',          title: 'Welcome to the Age of Wonder', num: '01', theme: 'aether' },
    { id: 'creating',      file: 'creating.html',       title: 'Creating Your Adventurer',     num: '02', theme: 'neutral' },
    { id: 'rolling',       file: 'rolling.html',        title: 'Rolling the Dice',             num: '03', theme: 'neutral' },
    { id: 'getting-hurt',  file: 'getting-hurt.html',   title: 'Getting Hurt',                 num: '04', theme: 'galvanic' },
    { id: 'skills',        file: 'skills.html',         title: 'Skills',                       num: '05', theme: 'neutral' },
    { id: 'magic',         file: 'magic.html',          title: 'The Two Paths of Magic',       num: '06', theme: 'aether' },
    { id: 'grimoire',      file: 'grimoire.html',       title: 'The Grimoire',                 num: '07', theme: 'aether' },
    { id: 'world-between', file: 'world-between.html',  title: 'The World Between',            num: '08', theme: 'split' },
    { id: 'combat',        file: 'combat.html',         title: 'When Violence Finds You',      num: '09', theme: 'galvanic' },
    { id: 'equipment',     file: 'equipment.html',      title: 'Arms & Equipment',             num: '10', theme: 'galvanic' },
    { id: 'reference',     file: 'reference.html',      title: 'Quick Reference',              num: '11', theme: 'neutral' },
    { id: 'tables',        file: 'tables.html',         title: 'Table Index',                  num: '12', theme: 'neutral' },
  ];

  // ── Detect Current Page ────────────────────────────────────
  function getCurrentPage() {
    const path = window.location.pathname;
    const filename = path.split('/').pop() || 'index.html';
    return PAGES.find(p => p.file === filename) || PAGES[0];
  }

  // ── Sidebar TOC ────────────────────────────────────────────
  function buildSidebar() {
    const nav = document.querySelector('.sidebar-nav');
    if (!nav) return;

    const current = getCurrentPage();

    const html = PAGES.map(page => {
      const isActive = page.id === current.id;
      const sections = isActive ? getSections() : [];
      const expanded = isActive && sections.length > 0 ? ' expanded' : '';

      let sectionsHtml = '';
      if (sections.length > 0) {
        sectionsHtml = '<ul class="toc-sections">' +
          sections.map(s =>
            `<li><a href="#${s.id}" class="toc-section-link" data-section="${s.id}">${s.text}</a></li>`
          ).join('') +
          '</ul>';
      }

      return `<div class="toc-chapter${expanded}">
        <a href="${page.file}" class="toc-chapter-link${isActive ? ' active' : ''}" data-page="${page.id}">
          <span class="toc-number">${page.num}</span>${page.title}
        </a>
        ${sectionsHtml}
      </div>`;
    }).join('');

    nav.innerHTML = html;
  }

  function getSections() {
    const headings = document.querySelectorAll('.page-content h2[id], .page-content h3[id]');
    return Array.from(headings).map(h => ({
      id: h.id,
      text: h.textContent.trim(),
    }));
  }

  // ── Scroll Spy (active section tracking) ───────────────────
  function initScrollSpy() {
    const sectionLinks = document.querySelectorAll('.toc-section-link');
    if (sectionLinks.length === 0) return;

    const headings = document.querySelectorAll('.page-content h2[id], .page-content h3[id]');
    if (headings.length === 0) return;

    const headerOffset = 80;

    function updateActive() {
      let current = null;
      headings.forEach(heading => {
        const rect = heading.getBoundingClientRect();
        if (rect.top <= headerOffset + 20) {
          current = heading.id;
        }
      });

      sectionLinks.forEach(link => {
        link.classList.toggle('active', link.dataset.section === current);
      });
    }

    window.addEventListener('scroll', updateActive, { passive: true });
    updateActive();
  }

  // ── Mobile Sidebar Toggle ──────────────────────────────────
  function initSidebarToggle() {
    const toggle = document.querySelector('.header-toggle');
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.sidebar-overlay');

    if (!toggle || !sidebar) return;

    function open() {
      sidebar.classList.add('open');
      if (overlay) overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function close() {
      sidebar.classList.remove('open');
      if (overlay) overlay.classList.remove('active');
      document.body.style.overflow = '';
    }

    toggle.addEventListener('click', () => {
      sidebar.classList.contains('open') ? close() : open();
    });

    if (overlay) {
      overlay.addEventListener('click', close);
    }

    // Close on navigation
    sidebar.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 900) close();
      });
    });
  }

  // ── Page Transitions ───────────────────────────────────────
  function initPageTransitions() {
    const current = getCurrentPage();

    // Intercept internal navigation clicks
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href]');
      if (!link) return;

      const href = link.getAttribute('href');
      if (!href) return;

      // Only intercept local page links
      const target = PAGES.find(p => p.file === href);
      if (!target) return;
      if (target.id === current.id && !href.includes('#')) return;

      // If it's a same-page anchor, let it scroll naturally
      if (href.startsWith('#')) return;

      e.preventDefault();
      window.location.href = href;
    });
  }

  // ── Scroll Reveal ──────────────────────────────────────────
  function initScrollReveal() {
    const reveals = document.querySelectorAll('.reveal, .reveal-stagger');
    if (reveals.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px',
    });

    reveals.forEach(el => observer.observe(el));
  }

  // ── Particle System ────────────────────────────────────────
  function initParticles() {
    const canvas = document.getElementById('particle-canvas');
    if (!canvas) return;

    // Don't run on mobile
    if (window.innerWidth < 900) return;

    const ctx = canvas.getContext('2d');
    let w, h;
    let particles = [];
    let animFrame;

    const PARTICLE_COUNT = 40;
    const COLORS = [
      { r: 61, g: 200, b: 224 },   // aether
      { r: 232, g: 168, b: 37 },   // galvanic
    ];

    function resize() {
      w = canvas.width = window.innerWidth;
      h = canvas.height = window.innerHeight;
    }

    function createParticle() {
      const color = COLORS[Math.random() > 0.5 ? 1 : 0];
      return {
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.2 - 0.1,
        radius: Math.random() * 1.5 + 0.5,
        opacity: Math.random() * 0.3 + 0.05,
        color: color,
        pulse: Math.random() * Math.PI * 2,
        pulseSpeed: Math.random() * 0.01 + 0.005,
      };
    }

    function init() {
      resize();
      particles = [];
      for (let i = 0; i < PARTICLE_COUNT; i++) {
        particles.push(createParticle());
      }
    }

    function draw() {
      ctx.clearRect(0, 0, w, h);

      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.pulse += p.pulseSpeed;

        // Wrap around
        if (p.x < -10) p.x = w + 10;
        if (p.x > w + 10) p.x = -10;
        if (p.y < -10) p.y = h + 10;
        if (p.y > h + 10) p.y = -10;

        const opacity = p.opacity * (0.6 + 0.4 * Math.sin(p.pulse));
        const { r, g, b } = p.color;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${opacity})`;
        ctx.fill();

        // Subtle glow
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius * 3, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${r}, ${g}, ${b}, ${opacity * 0.15})`;
        ctx.fill();
      });

      animFrame = requestAnimationFrame(draw);
    }

    window.addEventListener('resize', resize);
    init();
    draw();

    // Pause when tab is hidden
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        cancelAnimationFrame(animFrame);
      } else {
        draw();
      }
    });
  }

  // ── Init ───────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', () => {
    buildSidebar();
    initScrollSpy();
    initSidebarToggle();
    initPageTransitions();
    initScrollReveal();
    initParticles();
    playEntranceAnimation();
  });
})();
