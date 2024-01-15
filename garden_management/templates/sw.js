// Cache name
const CACHE_NAME = 'pwa-k-editor-caches-v1';
// Cache targets
const urlsToCache = [
    '/static/css/sanitize.css',
    '/static/css/bulma.css',
    '/static/css/style.css',
    '/static/css/login.css',
    '/static/js/scripts.js',
    '/static/img/garden.jpg',
    '/static/fa/css/all.min.css',
    '/static/fa/webfonts/fa-brands-400.eot',
    '/static/fa/webfonts/fa-brands-400.svg',
    '/static/fa/webfonts/fa-brands-400.ttf',
    '/static/fa/webfonts/fa-brands-400.woff',
    '/static/fa/webfonts/fa-brands-400.woff2',
    '/static/fa/webfonts/fa-regular-400.eot',
    '/static/fa/webfonts/fa-regular-400.svg',
    '/static/fa/webfonts/fa-regular-400.ttf',
    '/static/fa/webfonts/fa-regular-400.woff',
    '/static/fa/webfonts/fa-regular-400.woff2',
    '/static/fa/webfonts/fa-solid-900.eot',
    '/static/fa/webfonts/fa-solid-900.svg',
    '/static/fa/webfonts/fa-solid-900.ttf',
    '/static/fa/webfonts/fa-solid-900.woff',
    '/static/fa/webfonts/fa-solid-900.woff2',
];
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches
            .open(CACHE_NAME)
            .then((cache) => {
                return cache.addAll(urlsToCache);
            })
    );
});
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches
            .match(event.request)
            .then((response) => {
                return response ? response : fetch(event.request);
            })
    );
});