<script>
	import { onMount } from 'svelte';
	import Card from './Card.svelte';

	export let posts;

	export let projects;

	let wall;

	function resizeBig(wall) {
		wall.reset({
			selector: '.brick',
			cellW: 200,
			cellH: 200,
			gutterY: 10,
			gutterX: 10
		});
		wall.fixSize({ block: '.1x1', width: 200, height: 200 });
		wall.fixSize({ block: '.2x1', width: 200, height: 400 });
		wall.fixSize({ block: '.1x2', width: 400, height: 200 });
		wall.fixSize({ block: '.2x2', width: 400, height: 400 });
		wall.fixSize({ block: '.3x3', width: 600, height: 600 });
		wall.fixSize({ block: '.3x2', width: 400, height: 600 });
		wall.fixSize({ block: '.2x3', width: 600, height: 400 });
	}

	function resizeSmall(wall) {
		wall.reset({
			selector: '.brick',
			cellW: 100,
			cellH: 100,
			gutterY: 5,
			gutterX: 5
		});

		wall.fixSize({ block: '.1x1', width: 100, height: 100 });
		wall.fixSize({ block: '.2x1', width: 100, height: 200 });
		wall.fixSize({ block: '.1x2', width: 200, height: 200 });
		wall.fixSize({ block: '.2x2', width: 200, height: 200 });
		wall.fixSize({ block: '.3x3', width: 300, height: 300 });
		wall.fixSize({ block: '.3x2', width: 200, height: 300 });
		wall.fixSize({ block: '.2x3', width: 300, height: 200 });
	}

	export function adapt(wall) {
		if (window.innerWidth < 500) resizeSmall(wall);
		else resizeBig(wall);
		wall.fitWidth();
	}

	onMount(async () => {
		if (typeof window === 'undefined') return;
		let freewall = (await import('freewall')).default;
		wall = new freewall.Freewall('#container');
		adapt(wall);

		/* If the screen change resize to fit width */
		window.addEventListener('resize', () => {
			adapt(wall);
		});

		document.getElementById('search').addEventListener('input', () => {
			adapt(wall);
		});

		document.getElementById('proj').addEventListener('click', () => {
			adapt(wall);
		});

		document.getElementById('comp').addEventListener('click', () => {
			adapt(wall);
		});

		document.getElementById('buld').addEventListener('click', () => {
			adapt(wall);
		});

		document.getElementById('misc').addEventListener('click', () => {
			adapt(wall);
		});

		document.getElementById('logo').addEventListener('click', () => {
			adapt(wall);
		});
	});
</script>

<div id="container" class="flex">
	{#each posts as post}
		<Card {post} project={projects.filter((p) => p.id === post.project)[0]} />
	{/each}
</div>
