<script context="module">
	import Search from './Search.svelte';
	import Logo from './Logo.svelte';
	import Menu from './Menu.svelte';
</script>

<div class="drawer drawer-end">
	<input id="my-drawer-1" type="checkbox" class="drawer-toggle" />
	<div class="drawer-content">
		<div
			class="w-full navbar bg-base-300 flex sticky top-0 z-10 shadow-[0_5px_2px_0_rgba(0,0,0,0.5)]"
		>
			<div class="flex-1 flex content-start w-fit">
				<Logo on:filter />
			</div>

			<div class="flex-2 hidden lg:flex flex-col">
				<ul class="flex-1 menu menu-horizontal text-xl">
					<Menu on:filter />
				</ul>
			</div>

			<div class="flex-1 hidden form-control lg:flex items-end p-0">
				<Search on:filter />
			</div>

			<div class="flex-1 flex lg:hidden justify-end p-0">
				<label for="my-drawer-1" aria-label="open sidebar" class="btn btn-square btn-ghost">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						class="inline-block w-6 h-6 stroke-current"
						><path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M4 6h16M4 12h16M4 18h16"
						></path></svg
					>
				</label>
			</div>
		</div>

		<!-- Page content here -->
		<slot />
	</div>

	<div class="drawer-side">
		<label for="my-drawer-1" aria-label="close sidebar" class="drawer-overlay"></label>
		<ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
			<Menu />
			<Search on:filter />
		</ul>
	</div>
</div>
