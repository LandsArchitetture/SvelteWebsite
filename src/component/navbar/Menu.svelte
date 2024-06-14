<script>
	import { createEventDispatcher } from 'svelte';
	import AboutUs from './menu/AboutUs.svelte';
	import Contact from './menu/Contact.svelte';
	import Language from './menu/Language.svelte';

	const dispatch = createEventDispatcher();

	function project() {
		dispatch('filter', { text: 'progetto' });
	}

	function competitions() {
		dispatch('filter', { text: 'concorso' });
	}

	function buildings() {
		dispatch('filter', { text: 'edificio' });
	}

	function miscellaneous() {
		dispatch('filter', { text: 'varie' });
	}
</script>

<li>
	<details>
		<summary class="font-bold">About us</summary>
		<ul
			class="menu font-bold p-2 lg:bg-base-300 bg-base-200 rounded-t-none -z-5 lg:shadow-[5px_5px_2px_0_rgba(0,0,0,0.5)]"
		>
			<li><button id="proj" on:click={project}>Projects</button></li>
			<li><button id="comp" on:click={competitions}>Competitions</button></li>
			<li><button id="buld" on:click={buildings}>Buildings</button></li>
			<li><button id="misc" on:click={miscellaneous}>Miscellaneous</button></li>
			<div class="divider my-0 select-none"></div>
			<li><AboutUs /></li>
		</ul>
	</details>
</li>
<li class="font-bold"><Contact /></li>
<li><Language /></li>
