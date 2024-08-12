<script>
	import { createEventDispatcher } from 'svelte';
	import { navbarTranslations } from '$lib/stores/translations';

	const dispatch = createEventDispatcher();

	let filter = '';

	/**
	 * Filter all the images according to filter
	 * @param filter The filter to apply
	 */
	function transmit() {
		dispatch('filter', { text: filter });
	}
</script>

<input
	bind:value={filter}
	on:input={transmit}
	id="search"
	type="text"
	placeholder={$navbarTranslations['Search']}
	class="input input-bordered w-50 m-4 lg:m-0"
/>
