<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	let filter = '';

	function transmit() {
		dispatch('filter', { text: filter });
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
