<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	/**
	 * Remove all filters when called
	 */
	function filter() {
		dispatch('filter', { text: '' });
	}
</script>

<a id="logo" on:click={filter} class="btn btn-ghost text-xl p-0 w-fit" href="/">
	<svg
		xmlns="http://www.w3.org/2000/svg"
		class="Navbar_svg__rHY25"
		width="45mm"
		height="9mm"
		xml:space="preserve"
		style="shape-rendering:geometricPrecision;text-rendering:geometricPrecision;image-rendering:optimizeQuality;fill-rule:evenodd;clip-rule:evenodd"
		viewBox="0 0 644 132"
		><defs
			><style>
				.LANDS_logo_mini_svg__str0 {
					stroke: #2b2a29;
					stroke-width: 2.13862;
				}
				.LANDS_logo_mini_svg__fil0,
				.LANDS_logo_mini_svg__fil1 {
					fill: none;
					fill-rule: nonzero;
				}
				.LANDS_logo_mini_svg__fil0 {
					fill: #2b2a29;
				}
			</style></defs
		><g id="LANDS_logo_mini_svg__Livello_x0020_1"
			><path
				class="LANDS_logo_mini_svg__fil0"
				d="M10 118h15l-7-17-8 17zm-9 13 15-32h4l15 32h-4l-4-10H9l-5 10H1z"
			></path><path
				id="LANDS_logo_mini_svg__1"
				class="LANDS_logo_mini_svg__fil0"
				d="M79 102H67v12h12c3 0 5 0 7-1 1-1 2-3 2-5s-1-4-2-5c-2-1-4-1-7-1zm-15 29V99h15c4 0 7 0 9 2 2 1 3 3 3 6 0 2 0 4-1 6-1 1-3 2-5 2 2 1 3 1 4 2s1 2 1 5c0 0 1 2 1 3 0 3 0 5 1 6h-4c0-1-1-3-1-5v-4c0-2-1-3-2-4s-2-1-4-1H67v14h-3z"
			></path><path
				id="LANDS_logo_mini_svg__2"
				class="LANDS_logo_mini_svg__fil0"
				d="M150 109c-1-2-2-5-4-6s-5-2-8-2c-4 0-7 1-10 4-2 2-4 5-4 10 0 4 2 7 4 10s6 4 10 4c3 0 6-1 8-3s4-4 4-7h4c-1 4-3 7-6 10-2 2-6 3-10 3-5 0-9-2-12-5s-5-7-5-12 2-10 5-13 7-4 12-4c4 0 8 1 11 3 2 2 4 5 4 8h-3z"
			></path><path
				id="LANDS_logo_mini_svg__3"
				class="LANDS_logo_mini_svg__fil0"
				d="M184 131V99h3v13h22V99h3v32h-3v-16h-22v16z"
			></path><path
				id="LANDS_logo_mini_svg__4"
				class="LANDS_logo_mini_svg__fil0"
				d="M245 131V99h3v32z"
			></path><path
				id="LANDS_logo_mini_svg__5"
				class="LANDS_logo_mini_svg__fil0"
				d="M289 131v-30h-12v-2h28v2h-12v30z"
			></path><path
				id="LANDS_logo_mini_svg__6"
				class="LANDS_logo_mini_svg__fil0"
				d="M334 131V99h25v3h-22v11h20v3h-20v12h22v3z"
			></path><path
				id="LANDS_logo_mini_svg__7"
				class="LANDS_logo_mini_svg__fil0"
				d="M399 131v-30h-13v-2h29v2h-13v30z"
			></path><path
				id="LANDS_logo_mini_svg__8"
				class="LANDS_logo_mini_svg__fil0"
				d="M452 131v-30h-13v-2h29v2h-13v30z"
			></path><path
				id="LANDS_logo_mini_svg__9"
				class="LANDS_logo_mini_svg__fil0"
				d="M497 99h3v20c0 3 1 6 3 7 1 2 4 3 8 3s6-1 8-3c2-1 3-4 3-7V99h3v20c0 4-1 8-4 10-2 2-6 3-10 3-5 0-8-1-11-3-2-2-3-6-3-10V99z"
			></path><path
				id="LANDS_logo_mini_svg__10"
				class="LANDS_logo_mini_svg__fil0"
				d="M572 102h-11v12h12c3 0 5 0 7-1 1-1 2-3 2-5s-1-4-2-5c-2-1-4-1-8-1zm-14 29V99h15c4 0 7 0 9 2 2 1 3 3 3 6 0 2 0 4-1 6-1 1-3 2-5 2 2 1 3 1 4 2s1 2 1 5c0 0 1 2 1 3 0 3 0 5 1 6h-4c0-1-1-3-1-5v-4c0-2-1-3-2-4s-2-1-4-1h-14v14h-3z"
			></path><path
				id="LANDS_logo_mini_svg__11"
				class="LANDS_logo_mini_svg__fil0"
				d="M617 131V99h25v3h-22v11h20v3h-20v12h22v3z"
			></path><path
				class="LANDS_logo_mini_svg__fil0"
				d="M1 68V3h7v59h41v6zM149 42h30L164 8l-15 34zm-19 26 30-65h8l30 65h-7l-9-20h-36l-9 20h-7zM285 68V3h8l46 58V3h6v65h-9l-45-58v58zM463 3c7 0 13 0 16 1 4 1 8 3 11 5 3 3 6 6 7 10 2 5 3 10 3 16 0 7-1 12-3 17-1 4-4 8-8 10-2 2-6 4-10 5-3 1-9 1-16 1h-24V3h24zm-2 6h-16v53h18c5 0 10 0 13-1s6-2 8-3c3-2 5-5 7-9 1-4 2-8 2-14 0-5-1-10-2-14-2-3-4-6-7-8-2-2-5-3-8-3-3-1-8-1-15-1zM588 47h7c0 5 1 9 5 12s9 4 15 4c7 0 11-1 15-3 4-3 6-6 6-10 0-3-1-5-4-7-2-2-6-3-13-4l-14-3c-5-1-9-2-11-5-3-3-4-6-4-11 0-6 2-10 7-14 4-3 10-5 18-5s14 2 18 5c5 4 7 9 7 15h-6c0-4-2-8-6-10-3-3-7-4-13-4s-10 1-14 3c-3 3-4 6-4 10 0 3 1 5 3 7 2 1 7 3 13 4l12 2c6 1 11 3 13 6 3 2 4 6 4 11 0 6-2 11-7 15-4 3-11 5-19 5-9 0-16-2-21-6s-7-10-7-16v-1z"
			></path><path
				class="LANDS_logo_mini_svg__fil1 LANDS_logo_mini_svg__str0"
				d="M1 68V3h7v59h41v6zM149 42h30L164 8l-15 34zm-19 26 30-65h8l30 65h-7l-9-20h-36l-9 20h-7zM285 68V3h8l46 58V3h6v65h-9l-45-58v58zM463 3c7 0 13 0 16 1 4 1 8 3 11 5 3 3 6 6 7 10 2 5 3 10 3 16 0 7-1 12-3 17-1 4-4 8-8 10-2 2-6 4-10 5-3 1-9 1-16 1h-24V3h24zm-2 6h-16v53h18c5 0 10 0 13-1s6-2 8-3c3-2 5-5 7-9 1-4 2-8 2-14 0-5-1-10-2-14-2-3-4-6-7-8-2-2-5-3-8-3-3-1-8-1-15-1zM588 47h7c0 5 1 9 5 12s9 4 15 4c7 0 11-1 15-3 4-3 6-6 6-10 0-3-1-5-4-7-2-2-6-3-13-4l-14-3c-5-1-9-2-11-5-3-3-4-6-4-11 0-6 2-10 7-14 4-3 10-5 18-5s14 2 18 5c5 4 7 9 7 15h-6c0-4-2-8-6-10-3-3-7-4-13-4s-10 1-14 3c-3 3-4 6-4 10 0 3 1 5 3 7 2 1 7 3 13 4l12 2c6 1 11 3 13 6 3 2 4 6 4 11 0 6-2 11-7 15-4 3-11 5-19 5-9 0-16-2-21-6s-7-10-7-16v-1z"
			></path></g
		></svg
	>
</a>
