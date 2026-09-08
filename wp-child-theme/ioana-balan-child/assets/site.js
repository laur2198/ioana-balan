/* ==========================================================================
   ioana-balan.ro - comportamente portate din prototip
   ========================================================================== */
(function () {
  'use strict';

  /* Video click-to-load ----------------------------------------------------
     Pana la click pagina nu contacteaza niciun server Google. La click,
     <button class="video-card"> e INLOCUIT in DOM cu un <div> care tine
     iframe-ul: un <iframe> interactiv intr-un <button> e HTML invalid si
     face controalele playerului nesigure. */
  function play(card) {
    var id = card.getAttribute('data-yt');
    if (!id) { return; }

    var frame = document.createElement('iframe');
    frame.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) +
      '?autoplay=1&rel=0&modestbranding=1&playsinline=1';
    var label = card.querySelector('.video-card__title');
    frame.title = label ? label.textContent.trim() : 'Clip video Ioana Balan';
    frame.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    frame.allowFullscreen = true;

    var holder = document.createElement('div');
    holder.className = card.className + ' is-playing';
    holder.tabIndex = -1;
    holder.appendChild(frame);

    card.replaceWith(holder);
    holder.focus();
  }

  document.addEventListener('click', function (e) {
    var card = e.target.closest('.video-card:not(.is-playing)');
    if (card) { play(card); }
  });

  /* FAQ: aria-expanded nu se actualizeaza singur pe <summary> ------------- */
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.faq-item details').forEach(function (d) {
      var s = d.querySelector('summary');
      if (s) { s.setAttribute('aria-expanded', String(d.open)); }
      d.addEventListener('toggle', function () {
        if (s) { s.setAttribute('aria-expanded', String(d.open)); }
      });
    });

    /* Cuprins: deschis de la 768px in sus (atributul open nu se poate
       comuta dintr-un media query) */
    var toc = document.querySelector('.toc');
    if (toc && window.matchMedia('(min-width: 768px)').matches) {
      toc.open = true;
    }
  });
})();
