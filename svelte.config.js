import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const config = {
	kit: {
		adapter: adapter()
		// No `vite` configuration here, it's moved to `vite.config.js`
	},
	preprocess: vitePreprocess()
};

export default config;
