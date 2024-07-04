<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	function english() {
		dispatch('language', { text: 'en-US' });
	}

	function italian() {
		dispatch('language', { text: 'it-IT' });
	}
</script>

<details>
	<summary class="font-bold">Language</summary>
	<ul
		class="menu font-bold p-2 lg:bg-base-300 bg-base-200 rounded-t-none -z-5 lg:shadow-[5px_5px_2px_0_rgba(0,0,0,0.5)]"
	>
		<li><button on:click={english}>English</button></li>
		<li><button on:click={italian}>Italian</button></li>
	</ul>
</details>
