/**
 * Wave Hero - Reusable Three.js background with automatic fallbacks
 *
 * Features:
 * - WebGL → CSS3D → CSS automatic fallback
 * - Retina/HiDPI support (crisp on iPhone)
 * - Auto-creates canvas/fallback elements
 * - Auto-initializes via data attributes
 * - Page-based preset detection
 * - Mouse/touch parallax
 *
 * Usage (pick one):
 *
 * 1. Auto-detect preset from URL path:
 *    <script src="/js/wave-hero.js" data-auto></script>
 *
 * 2. Explicit preset:
 *    <script src="/js/wave-hero.js" data-preset="quantum"></script>
 *
 * 3. Manual initialization:
 *    <script src="/js/wave-hero.js"></script>
 *    <script>WaveHero.init({ preset: 'waves' });</script>
 *
 * Presets: waves, particles, grid, nebula, quantum, governance
 */

(function(global) {
    'use strict';

    const WaveHero = {
        // Configuration presets for different hero styles
        presets: {
            waves: {
                separation: 80,
                amountX: 60,
                amountY: 40,
                color: 0x8b5cf6,        // Purple
                waveHeight: 30,
                waveSpeed: 0.05,
                cameraZ: 1200,
                cameraY: 400,
                particleSize: 200,
                opacity: 0.4
            },
            particles: {
                separation: 100,
                amountX: 50,
                amountY: 50,
                color: 0x06b6d4,        // Cyan
                waveHeight: 50,
                waveSpeed: 0.03,
                cameraZ: 1500,
                cameraY: 500,
                particleSize: 150,
                opacity: 0.3
            },
            grid: {
                separation: 60,
                amountX: 80,
                amountY: 50,
                color: 0xd4a543,        // Amber
                waveHeight: 20,
                waveSpeed: 0.08,
                cameraZ: 1000,
                cameraY: 300,
                particleSize: 180,
                opacity: 0.5
            },
            nebula: {
                separation: 120,
                amountX: 40,
                amountY: 30,
                color: 0xa855f7,        // Light purple
                color2: 0x22d3ee,       // Cyan accent
                waveHeight: 60,
                waveSpeed: 0.02,
                cameraZ: 1800,
                cameraY: 600,
                particleSize: 250,
                opacity: 0.35
            },
            quantum: {
                separation: 70,
                amountX: 70,
                amountY: 45,
                color: 0x22d3ee,        // Cyan
                color2: 0x8b5cf6,       // Purple accent
                waveHeight: 40,
                waveSpeed: 0.04,
                cameraZ: 1100,
                cameraY: 350,
                particleSize: 220,
                opacity: 0.45
            },
            governance: {
                separation: 90,
                amountX: 55,
                amountY: 35,
                color: 0xd4a543,        // Amber (ethics/governance)
                color2: 0x8b5cf6,       // Purple accent
                waveHeight: 25,
                waveSpeed: 0.03,
                cameraZ: 1300,
                cameraY: 450,
                particleSize: 190,
                opacity: 0.35
            },
            classical: {
                separation: 75,
                amountX: 65,
                amountY: 42,
                color: 0x8b5cf6,        // Purple (classical security)
                waveHeight: 35,
                waveSpeed: 0.045,
                cameraZ: 1150,
                cameraY: 380,
                particleSize: 210,
                opacity: 0.4
            }
        },

        // Map URL paths to presets
        pathPresets: {
            '/quantum': 'quantum',
            '/governance': 'governance',
            '/classical': 'classical',
            '/blog': 'nebula',
            '/about': 'particles',
            '/visualizations': 'grid',
            '/': 'waves'
        },

        config: null,
        renderer: null,
        scene: null,
        camera: null,
        particles: null,
        css3dRenderer: null,
        animationId: null,
        initialized: false,

        /**
         * Detect preset from current URL path
         */
        detectPreset: function() {
            const path = window.location.pathname;
            for (const [pattern, preset] of Object.entries(this.pathPresets)) {
                if (pattern !== '/' && path.startsWith(pattern)) {
                    return preset;
                }
            }
            return 'waves'; // default
        },

        /**
         * Create required DOM elements if they don't exist
         */
        createElements: function() {
            // Create canvas if missing
            if (!document.getElementById('wavehero-canvas')) {
                const canvas = document.createElement('canvas');
                canvas.id = 'wavehero-canvas';
                canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;';
                document.body.insertBefore(canvas, document.body.firstChild);
            }

            // Create CSS fallback if missing
            if (!document.getElementById('wavehero-fallback')) {
                const fallback = document.createElement('div');
                fallback.id = 'wavehero-fallback';
                fallback.className = 'wave-bg';
                fallback.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;background:linear-gradient(135deg, #050a14 0%, #0a1628 50%, #050a14 100%);';
                document.body.insertBefore(fallback, document.body.firstChild);
            }
        },

        /**
         * Initialize the wave hero background
         * @param {Object} options - Configuration options
         * @param {string} options.preset - Preset name ('waves', 'particles', 'grid', 'nebula', 'quantum', 'governance', 'classical')
         * @param {string} options.container - Container element ID (default: auto-created)
         * @param {string} options.fallbackId - CSS fallback element ID (default: auto-created)
         * @param {number} options.color - Override color (hex)
         * @param {Object} options.custom - Custom config to merge with preset
         */
        init: function(options = {}) {
            if (this.initialized) {
                console.log('WaveHero: Already initialized');
                return;
            }

            // Auto-detect preset if not specified
            const presetName = options.preset || this.detectPreset();
            const preset = this.presets[presetName] || this.presets.waves;
            this.config = { ...preset, ...options.custom };

            // Override color if provided
            if (options.color) this.config.color = options.color;

            // Create elements if needed
            this.createElements();

            // Set element references
            this.containerId = options.container || 'wavehero-canvas';
            this.fallbackEl = document.getElementById(options.fallbackId || 'wavehero-fallback');

            console.log('WaveHero: Initializing with preset "' + presetName + '"');
            this.initialized = true;
            this.loadThreeJS();
        },

        loadThreeJS: function() {
            if (window.THREE) {
                this.onThreeLoaded();
                return;
            }

            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js';
            script.onload = () => this.onThreeLoaded();
            script.onerror = () => this.showFallback('Three.js failed to load');
            document.head.appendChild(script);
        },

        onThreeLoaded: function() {
            if (this.webglSupported()) {
                this.initWebGL();
            } else {
                this.initCSS3D();
            }
        },

        webglSupported: function() {
            try {
                const canvas = document.createElement('canvas');
                return !!(window.WebGLRenderingContext &&
                    (canvas.getContext('webgl') || canvas.getContext('experimental-webgl')));
            } catch (e) {
                return false;
            }
        },

        /**
         * Get optimal pixel ratio for crisp rendering on all devices
         * Respects device capabilities while avoiding excessive GPU load
         */
        getPixelRatio: function() {
            const dpr = window.devicePixelRatio || 1;
            // Allow up to 3x for iPhone/iPad Retina, cap at 3 for performance
            return Math.min(dpr, 3);
        },

        initWebGL: function() {
            const cfg = this.config;
            let container = document.getElementById(this.containerId);

            if (!container) {
                console.warn('WaveHero: Canvas element not found, creating one');
                this.createElements();
                container = document.getElementById(this.containerId);
            }

            try {
                this.scene = new THREE.Scene();
                this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 10000);
                this.camera.position.set(0, cfg.cameraY, cfg.cameraZ);

                const numParticles = cfg.amountX * cfg.amountY;
                const positions = new Float32Array(numParticles * 3);
                const scales = new Float32Array(numParticles);

                let i = 0, j = 0;
                for (let ix = 0; ix < cfg.amountX; ix++) {
                    for (let iy = 0; iy < cfg.amountY; iy++) {
                        positions[i] = ix * cfg.separation - ((cfg.amountX * cfg.separation) / 2);
                        positions[i + 1] = 0;
                        positions[i + 2] = iy * cfg.separation - ((cfg.amountY * cfg.separation) / 2);
                        scales[j] = 1;
                        i += 3; j++;
                    }
                }

                const geometry = new THREE.BufferGeometry();
                geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
                geometry.setAttribute('scale', new THREE.BufferAttribute(scales, 1));

                // Shader with configurable color
                const colorHex = cfg.color;
                const material = new THREE.ShaderMaterial({
                    uniforms: {
                        color: { value: new THREE.Color(colorHex) },
                        particleSize: { value: cfg.particleSize },
                        opacity: { value: cfg.opacity }
                    },
                    vertexShader: `
                        attribute float scale;
                        uniform float particleSize;
                        void main() {
                            vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
                            gl_PointSize = scale * (particleSize / -mvPosition.z);
                            gl_Position = projectionMatrix * mvPosition;
                        }
                    `,
                    fragmentShader: `
                        uniform vec3 color;
                        uniform float opacity;
                        void main() {
                            float dist = length(gl_PointCoord - vec2(0.5));
                            if (dist > 0.5) discard;
                            float alpha = (1.0 - smoothstep(0.3, 0.5, dist)) * opacity;
                            gl_FragColor = vec4(color, alpha);
                        }
                    `,
                    transparent: true,
                    depthWrite: false
                });

                this.particles = new THREE.Points(geometry, material);
                this.scene.add(this.particles);

                this.renderer = new THREE.WebGLRenderer({
                    canvas: container,
                    antialias: true,
                    alpha: false
                });

                // CRITICAL: Set pixel ratio for crisp rendering on Retina/iPhone
                this.renderer.setPixelRatio(this.getPixelRatio());
                this.renderer.setSize(window.innerWidth, window.innerHeight);
                this.renderer.setClearColor(0x050a14, 1);

                // Show WebGL canvas, hide fallback
                container.style.display = 'block';
                if (this.fallbackEl) this.fallbackEl.classList.add('hidden');
                console.log('WaveHero: WebGL active (DPR: ' + this.getPixelRatio() + ')');

                this.setupInteraction();
                this.animate();

            } catch (e) {
                console.log('WaveHero: WebGL failed, trying CSS3D:', e.message);
                this.initCSS3D();
            }
        },

        initCSS3D: function() {
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/js/renderers/CSS3DRenderer.js';
            script.onload = () => this.startCSS3D();
            script.onerror = () => this.showFallback('CSS3D failed to load');
            document.head.appendChild(script);
        },

        startCSS3D: function() {
            const cfg = this.config;
            // Use fewer particles for CSS3D (DOM elements are heavier)
            const amountX = Math.min(cfg.amountX, 20);
            const amountY = Math.min(cfg.amountY, 15);
            const separation = cfg.separation * 1.5;

            try {
                this.scene = new THREE.Scene();
                this.camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 1, 5000);
                this.camera.position.set(0, cfg.cameraY * 0.75, cfg.cameraZ * 0.8);
                this.camera.lookAt(this.scene.position);

                const particles = [];
                const colorStr = '#' + cfg.color.toString(16).padStart(6, '0');

                for (let ix = 0; ix < amountX; ix++) {
                    for (let iy = 0; iy < amountY; iy++) {
                        const el = document.createElement('div');
                        el.style.cssText = `
                            width: 10px; height: 10px;
                            background: radial-gradient(circle, ${colorStr}99 0%, transparent 70%);
                            border-radius: 50%;
                        `;
                        const obj = new THREE.CSS3DObject(el);
                        obj.position.x = ix * separation - ((amountX * separation) / 2);
                        obj.position.z = iy * separation - ((amountY * separation) / 2);
                        obj.userData = { ix, iy };
                        this.scene.add(obj);
                        particles.push(obj);
                    }
                }

                this.css3dParticles = particles;
                this.css3dRenderer = new THREE.CSS3DRenderer();
                this.css3dRenderer.setSize(window.innerWidth, window.innerHeight);
                this.css3dRenderer.domElement.style.cssText =
                    'position:fixed;top:0;left:0;z-index:0;pointer-events:none;background:#050a14;';
                document.body.insertBefore(this.css3dRenderer.domElement, document.body.firstChild);

                if (this.fallbackEl) this.fallbackEl.classList.add('hidden');
                console.log('WaveHero: CSS3D active');

                this.setupInteraction();
                this.animateCSS3D();

            } catch (e) {
                this.showFallback('CSS3D failed: ' + e.message);
            }
        },

        setupInteraction: function() {
            this.mouseX = 0;
            this.mouseY = 0;
            this.windowHalfX = window.innerWidth / 2;
            this.windowHalfY = window.innerHeight / 2;
            this.count = 0;

            document.body.addEventListener('pointermove', (e) => {
                this.mouseX = e.clientX - this.windowHalfX;
                this.mouseY = e.clientY - this.windowHalfY;
            });

            window.addEventListener('resize', () => {
                this.windowHalfX = window.innerWidth / 2;
                this.windowHalfY = window.innerHeight / 2;
                this.camera.aspect = window.innerWidth / window.innerHeight;
                this.camera.updateProjectionMatrix();

                if (this.renderer) {
                    this.renderer.setSize(window.innerWidth, window.innerHeight);
                }
                if (this.css3dRenderer) {
                    this.css3dRenderer.setSize(window.innerWidth, window.innerHeight);
                }
            });
        },

        animate: function() {
            const cfg = this.config;
            const self = this;

            function loop() {
                self.animationId = requestAnimationFrame(loop);

                // Camera parallax
                self.camera.position.x += (self.mouseX * 0.3 - self.camera.position.x) * 0.02;
                self.camera.position.y += (-self.mouseY * 0.3 + cfg.cameraY - self.camera.position.y) * 0.02;
                self.camera.lookAt(self.scene.position);

                // Wave animation
                const pos = self.particles.geometry.attributes.position.array;
                const scl = self.particles.geometry.attributes.scale.array;
                let i = 0, j = 0;

                for (let ix = 0; ix < cfg.amountX; ix++) {
                    for (let iy = 0; iy < cfg.amountY; iy++) {
                        pos[i + 1] = Math.sin((ix + self.count) * 0.3) * cfg.waveHeight +
                                     Math.sin((iy + self.count) * 0.5) * cfg.waveHeight;
                        scl[j] = (Math.sin((ix + self.count) * 0.3) + 1) * 8 +
                                 (Math.sin((iy + self.count) * 0.5) + 1) * 8;
                        i += 3; j++;
                    }
                }

                self.particles.geometry.attributes.position.needsUpdate = true;
                self.particles.geometry.attributes.scale.needsUpdate = true;
                self.renderer.render(self.scene, self.camera);
                self.count += cfg.waveSpeed;
            }

            loop();
        },

        animateCSS3D: function() {
            const cfg = this.config;
            const self = this;

            function loop() {
                self.animationId = requestAnimationFrame(loop);

                self.css3dParticles.forEach(p => {
                    const { ix, iy } = p.userData;
                    p.position.y = Math.sin((ix + self.count) * 0.3) * cfg.waveHeight * 1.3 +
                                   Math.sin((iy + self.count) * 0.5) * cfg.waveHeight * 1.3;
                    const scale = (Math.sin((ix + self.count) * 0.3) + 1) * 0.5 +
                                  (Math.sin((iy + self.count) * 0.5) + 1) * 0.5 + 0.5;
                    p.element.style.opacity = scale * cfg.opacity * 2;
                });

                self.css3dRenderer.render(self.scene, self.camera);
                self.count += cfg.waveSpeed;
            }

            loop();
        },

        showFallback: function(reason) {
            console.log('WaveHero: ' + reason + ', using CSS fallback');
            // CSS fallback stays visible (no action needed)
        },

        /**
         * Cleanup and destroy the hero
         */
        destroy: function() {
            if (this.animationId) {
                cancelAnimationFrame(this.animationId);
            }
            if (this.renderer) {
                this.renderer.dispose();
            }
            if (this.css3dRenderer && this.css3dRenderer.domElement) {
                this.css3dRenderer.domElement.remove();
            }
            this.initialized = false;
        }
    };

    // Export
    global.WaveHero = WaveHero;

    // Auto-initialize from script data attributes
    function autoInit() {
        const scripts = document.querySelectorAll('script[src*="wave-hero.js"]');
        scripts.forEach(script => {
            // Check for data-auto (auto-detect preset from URL)
            if (script.hasAttribute('data-auto')) {
                WaveHero.init();
                return;
            }

            // Check for explicit data-preset
            const preset = script.getAttribute('data-preset');
            if (preset) {
                const color = script.getAttribute('data-color');
                WaveHero.init({
                    preset: preset,
                    color: color ? parseInt(color, 16) : undefined
                });
            }
        });
    }

    // Run auto-init when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', autoInit);
    } else {
        // DOM already loaded, run immediately
        autoInit();
    }

})(typeof window !== 'undefined' ? window : this);
