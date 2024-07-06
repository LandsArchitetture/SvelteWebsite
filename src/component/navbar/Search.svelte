<script>
	import { createEventDispatcher } from 'svelte';

	export let language;
	export let translations;

	const dispatch = createEventDispatcher();

	let filter = '';

	/**
	 * Filter all the images according to filter
	 * @param filter The filter to apply
	 */
	function transmit() {
		dispatch('filter', { text: filter });
	}

	let currentLanguage = language;

	$: if (currentLanguage !== language) {
		document.getElementById('search').placeholder = getTranslation('Search');
		currentLanguage = language;
	}

	function getTranslation(word) {
		if (translations && translations[word]) {
			return translations[word][language];
		}
		return 'Search';
	}
</script>

<input
	bind:value={filter}
	on:input={transmit}
	id="search"
	type="text"
	placeholder="Search"
	class="input input-bordered w-50 m-4 lg:m-0"
/>
