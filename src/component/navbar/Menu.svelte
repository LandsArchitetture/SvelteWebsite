<script>
	import { createEventDispatcher } from 'svelte';
	import AboutUs from './menu/AboutUs.svelte';
	import Contact from './menu/Contact.svelte';
	import Language from './menu/Language.svelte';
	import { navbarTranslations } from '$lib/stores/translations';

	const dispatch = createEventDispatcher();

	/**
	 * Filter the projects
	 */
	function project() {
		dispatch('filter', { text: 'progetto' });
	}

	/**
	 * Filter the competitions
	 */
	function competitions() {
		dispatch('filter', { text: 'concorso' });
	}

	/**
	 * Filter the buildings
	 */
	function buildings() {
		dispatch('filter', { text: 'edificio' });
	}

	/**
	 * Filter the miscellaneous
	 */
	function miscellaneous() {
		dispatch('filter', { text: 'varie' });
	}
</script>

<li>
	<details>
		<summary class="font-bold" id="about">{$navbarTranslations['About us']}</summary>
		<ul
			class="menu font-bold p-2 lg:bg-base-300 bg-base-200 rounded-t-none -z-5 lg:shadow-[5px_5px_2px_0_rgba(0,0,0,0.5)]"
		>
			<li><button id="proj" on:click={project}>{$navbarTranslations['Projects']}</button></li>
			<li>
				<button id="comp" on:click={competitions}>{$navbarTranslations['Competitions']}</button>
			</li>
			<li><button id="buld" on:click={buildings}>{$navbarTranslations['Buildings']}</button></li>
			<li>
				<button id="misc" on:click={miscellaneous}>{$navbarTranslations['Miscellaneous']}</button>
			</li>
			<div class="divider my-0 select-none"></div>
			<li><AboutUs /></li>
		</ul>
	</details>
</li>
<li class="font-bold"><Contact /></li>
<li><Language on:translate /></li>
