<script>
	import { createEventDispatcher } from 'svelte';
	import AboutUs from './menu/AboutUs.svelte';
	import Contact from './menu/Contact.svelte';
	import Language from './menu/Language.svelte';

	export let language;
	export let translations;

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

	let currentLanguage = language;

	$: if (currentLanguage !== language) {
		document.getElementById('proj').innerHTML = getTranslation('Projects');
		document.getElementById('comp').innerHTML = getTranslation('Competitions');
		document.getElementById('buld').innerHTML = getTranslation('Buildings');
		document.getElementById('misc').innerHTML = getTranslation('Miscellaneous');
		document.getElementById('about').innerHTML = getTranslation('About us');
		currentLanguage = language;
	}

	function getTranslation(word) {
		if (translations && translations[word]) {
			return translations[word][language];
		}
		return '';
	}
</script>

<li>
	<details>
		<summary class="font-bold" id="about">About us</summary>
		<ul
			class="menu font-bold p-2 lg:bg-base-300 bg-base-200 rounded-t-none -z-5 lg:shadow-[5px_5px_2px_0_rgba(0,0,0,0.5)]"
		>
			<li><button id="proj" on:click={project}>Projects</button></li>
			<li><button id="comp" on:click={competitions}>Competitions</button></li>
			<li><button id="buld" on:click={buildings}>Buildings</button></li>
			<li><button id="misc" on:click={miscellaneous}>Miscellaneous</button></li>
			<div class="divider my-0 select-none"></div>
			<li><AboutUs {language} {translations} /></li>
		</ul>
	</details>
</li>
<li class="font-bold"><Contact {language} {translations} /></li>
<li><Language on:translate {language} {translations} /></li>
