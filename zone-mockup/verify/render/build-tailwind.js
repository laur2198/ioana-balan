#!/usr/bin/env node
/*
 * Construiește un CSS Tailwind local din configurarea REALĂ a prototipului,
 * assets/tailwind.config.js.
 *
 * De ce: paginile încarcă Tailwind de pe cdn.tailwindcss.com, care e blocat de
 * proxy-ul de egress din sandbox. Fără build local, browserul randează paginile
 * cu ZERO clase aplicate, iar orice măsurătoare de layout e falsă — vezi README.
 *
 * Configurarea nu se copiază și nu se rescrie: fișierul din assets/ se execută
 * cu un obiect `tailwind` fals, exact cum ar face-o scriptul CDN. Dacă tokenii
 * se schimbă în assets/, build-ul îi ia automat.
 */
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const AICI = __dirname;
const RADACINA = path.resolve(AICI, '../../..');
const CONFIG = path.join(RADACINA, 'assets/tailwind.config.js');
const BUILD = path.join(AICI, 'build');

// --content: implicit ambele familii de pagini; suprascriere prin argv
const content = process.argv.slice(2).length
  ? process.argv.slice(2)
  : [path.join(RADACINA, 'zone-mockup/*.html'), path.join(RADACINA, '*.html')];

if (!fs.existsSync(CONFIG)) {
  console.error('Nu găsesc ' + CONFIG);
  process.exit(1);
}

// Execută config-ul din assets/ cu un `tailwind` fals, ca scriptul CDN.
const fals = {};
new Function('tailwind', fs.readFileSync(CONFIG, 'utf8'))(fals);
const cfg = fals.config;
if (!cfg) {
  console.error('assets/tailwind.config.js nu a setat tailwind.config');
  process.exit(1);
}
cfg.content = content;

fs.mkdirSync(BUILD, { recursive: true });

// Plugin-urile nu supraviețuiesc serializării JSON; se re-atașează ca require().
const corp = JSON.stringify(cfg, null, 1);
fs.writeFileSync(
  path.join(BUILD, 'tailwind.generat.cjs'),
  'module.exports = ' + corp + ';\n' +
  'module.exports.plugins = [\n' +
  "  require('@tailwindcss/forms'),\n" +
  "  require('@tailwindcss/container-queries'),\n" +
  '];\n'
);
fs.writeFileSync(path.join(BUILD, 'intrare.css'),
  '@tailwind base;\n@tailwind components;\n@tailwind utilities;\n');

execFileSync(path.join(AICI, 'node_modules/.bin/tailwindcss'), [
  '-c', path.join(BUILD, 'tailwind.generat.cjs'),
  '-i', path.join(BUILD, 'intrare.css'),
  '-o', path.join(BUILD, 'tailwind.css'),
  '--minify',
], { stdio: 'inherit' });

const dim = fs.statSync(path.join(BUILD, 'tailwind.css')).size;
console.log('build/tailwind.css — ' + dim + ' B, din ' + content.length + ' tipar(e) de conținut');
