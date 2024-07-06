<script>
	import { createEventDispatcher } from 'svelte';
	import { get } from 'svelte/store';

	export let language;
	export let translations;

	const dispatch = createEventDispatcher();

	function english() {
		dispatch('translate', { text: 'en-US' });
	}

	function italian() {
		dispatch('translate', { text: 'it-IT' });
	}

	let currentLanguage = language;

	$: if (currentLanguage !== language) {
		document.getElementById('lang').innerHTML = getTranslation('Language');
		currentLanguage = language;
	}

	function getTranslation(word) {
		if (translations && translations[word]) {
			return translations[word][language];
		}
		return '';
	}
</script>

<details>
	<summary class="font-bold" id="lang">{getTranslation('Language')}</summary>
	<ul
		class="menu font-bold p-2 lg:bg-base-300 bg-base-200 rounded-t-none -z-5 lg:shadow-[5px_5px_2px_0_rgba(0,0,0,0.5)]"
	>
		<li><button on:click={english}>English</button></li>
		<li><button on:click={italian}>Italiano</button></li>
	</ul>
</details>
