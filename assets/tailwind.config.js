/* ==========================================================================
   ioana-balan.ro — configurare Tailwind partajată (prototip)
   Sursă unică pentru tokenii de design. Se încarcă DUPĂ scriptul Tailwind Play
   CDN (cdn.tailwindcss.com), înlocuind config-ul inline duplicat pe fiecare pagină.
   Vezi CLAUDE.md §5 pentru semantica tokenilor (accent bordo #800020 = singurul accent).
   ========================================================================== */
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      "colors": {
        "accent": "#800020",
        "accent-hover": "#600018",
        "secondary": "#c6c6c6",
        "secondary-fixed": "#e3e2e2",
        "primary-fixed-dim": "#c8c6c5",
        "secondary-container": "#484949",
        "surface-tint": "#c8c6c5",
        "tertiary": "#ffb3b1",
        "on-surface": "#e5e2e1",
        "primary-container": "#121212",
        "tertiary-fixed-dim": "#ffb3b1",
        "surface-container-low": "#1c1b1b",
        "error-container": "#93000a",
        "outline": "#8e9192",
        "background": "#131313",
        "surface-container-lowest": "#0e0e0e",
        "on-primary-container": "#7e7d7d",
        "error": "#ffb4ab",
        "surface-dim": "#131313",
        "on-secondary-fixed-variant": "#464747",
        "on-primary": "#313030",
        "on-primary-fixed-variant": "#474646",
        "surface-container-highest": "#353535",
        "tertiary-container": "#2f0004",
        "on-surface-variant": "#c4c7c7",
        "on-tertiary": "#630d16",
        "on-secondary": "#2f3131",
        "surface": "#131313",
        "surface-bright": "#393939",
        "on-tertiary-fixed-variant": "#82252a",
        "inverse-primary": "#5f5e5e",
        "outline-variant": "#444748",
        "secondary-fixed-dim": "#c6c6c6",
        "surface-container": "#20201f",
        "on-primary-fixed": "#1c1b1b",
        "surface-variant": "#353535",
        "primary-fixed": "#e5e2e1",
        "on-error-container": "#ffdad6",
        "tertiary-fixed": "#ffdad8",
        "on-secondary-container": "#b8b8b8",
        "primary": "#c8c6c5",
        "inverse-surface": "#e5e2e1",
        "on-secondary-fixed": "#1a1c1c",
        "surface-container-high": "#2a2a2a",
        "inverse-on-surface": "#313030",
        "on-background": "#e5e2e1"
      },
      "borderRadius": {
        "DEFAULT": "0.25rem",
        "lg": "0.5rem",
        "xl": "0.75rem",
        "full": "9999px"
      },
      "spacing": {
        "margin-desktop": "64px",
        "max-width": "1200px",
        "unit": "8px",
        "margin-mobile": "16px",
        "gutter": "24px"
      },
      "fontFamily": {
        "label-md": ["Inter"],
        "body-lg": ["Inter"],
        "headline-lg": ["EB Garamond"],
        "headline-md": ["EB Garamond"],
        "body-md": ["Inter"],
        "headline-lg-mobile": ["EB Garamond"],
        "display-lg": ["EB Garamond"]
      },
      "fontSize": {
        "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "600"}],
        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
        "headline-lg": ["32px", {"lineHeight": "40px", "fontWeight": "500"}],
        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "500"}],
        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
        "headline-lg-mobile": ["28px", {"lineHeight": "36px", "fontWeight": "500"}],
        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "500"}]
      }
    }
  }
}
