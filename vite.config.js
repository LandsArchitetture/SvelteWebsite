import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	build: {
		sourcemap: true,  // Enable source maps for production builds
		minify: false     // Disable minification if you're debugging
	}
});