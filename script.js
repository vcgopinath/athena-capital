// ========================================
// Athena Capital Partners LLC — Website Scripts
// ========================================

document.addEventListener('DOMContentLoaded', () => {

  // --- Navbar scroll effect ---
  const navbar = document.getElementById('navbar');
  const onScroll = () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // --- Mobile nav toggle ---
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    navToggle.classList.toggle('active');
  });

  // Close mobile nav on link click
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navToggle.classList.remove('active');
    });
  });

  // --- Active nav link on scroll ---
  const sections = document.querySelectorAll('section[id]');
  const navItems = document.querySelectorAll('.nav-links a');

  const updateActiveNav = () => {
    const scrollPos = window.scrollY + 120;
    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');
      if (scrollPos >= top && scrollPos < top + height) {
        navItems.forEach(a => {
          a.classList.toggle('active', a.getAttribute('href') === `#${id}`);
        });
      }
    });
  };
  window.addEventListener('scroll', updateActiveNav, { passive: true });

  // --- Fade-in on scroll ---
  const fadeElements = document.querySelectorAll(
    '.service-card, .team-card, .insight-card, .value-card, .stat, .about-lead'
  );

  fadeElements.forEach(el => el.classList.add('fade-in'));

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  fadeElements.forEach(el => observer.observe(el));

  // --- Contact form ---
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', () => {
      const btn = form.querySelector('button[type="submit"]');
      btn.textContent = 'Sending...';
      btn.style.background = '#2d6a4f';
      btn.style.color = '#fff';
      btn.disabled = true;
    });
  }

  // --- Smooth scroll for all anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (href === '#') return;
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // --- Cookie Consent Banner ---
  const cookieBanner = document.getElementById('cookieBanner');
  const cookieAccept = document.getElementById('cookieAccept');
  const cookieDecline = document.getElementById('cookieDecline');
  const footerCookieSettings = document.getElementById('footerCookieSettings');

  function showBanner() {
    if (cookieBanner) {
      setTimeout(() => cookieBanner.classList.add('visible'), 500);
    }
  }

  function hideBanner() {
    if (cookieBanner) {
      cookieBanner.classList.remove('visible');
    }
  }

  function enableAnalytics() {
    localStorage.setItem('analytics-consent', 'accepted');
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=G-REN5THJRFM';
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-REN5THJRFM');
  }

  // Show banner if no consent decision has been made
  if (!localStorage.getItem('analytics-consent')) {
    showBanner();
  }

  if (cookieAccept) {
    cookieAccept.addEventListener('click', () => {
      enableAnalytics();
      hideBanner();
    });
  }

  if (cookieDecline) {
    cookieDecline.addEventListener('click', () => {
      localStorage.setItem('analytics-consent', 'declined');
      hideBanner();
    });
  }

  // Footer "Cookie Settings" link — reopen the banner
  if (footerCookieSettings) {
    footerCookieSettings.addEventListener('click', (e) => {
      e.preventDefault();
      localStorage.removeItem('analytics-consent');
      showBanner();
    });
  }

});
