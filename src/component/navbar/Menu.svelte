<script>
	import { createEventDispatcher } from 'svelte';

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
			class="menu font-bold p-2 bg-base-300 rounded-t-none -z-5 lg:shadow-[5px_5px_2px_0_rgba(0,0,0,0.5)]"
		>
			<li><button id="proj" on:click={project}>Projects</button></li>
			<li><button id="comp" on:click={competitions}>Competitions</button></li>
			<li><button id="buld" on:click={buildings}>Buildings</button></li>
			<div class="divider"></div>
			<li><button id="misc" on:click={miscellaneous}>Miscellaneous</button></li>
		</ul>
	</details>
</li>
<li class="font-bold"><div>Contact</div></li>
<li>
	<details>
		<summary class="font-bold">Language</summary>
		<ul
			class="menu font-bold p-2 bg-base-300 rounded-t-none -z-5 lg:shadow-[5px_5px_2px_0_rgba(0,0,0,0.5)]"
		>
			<li><div>English</div></li>
			<li class="disabled"><div>Italian</div></li>
		</ul>
	</details>
</li>
