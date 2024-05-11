<script>
	import Carousel from './Carousel.svelte';

	export let data;

	export let project;

	let related = data.posts.filter((p) => p.project === project);
</script>

<dialog id={project} class="modal">
	<div class="modal-box flex p-0 w-fit">
		<!-- Carousel -->
		<Carousel {data} {related} {project} />
		<!-- Close button -->
		<form method="dialog">
			<button
				class="btn btn-sm btn-circle btn-ghost absolute right-4 top-4 text-red-700 scale-150 [text-shadow:_0_0_5px_rgb(0_0_0)]"
				>✕</button
			>
		</form>
		<!-- Header -->
		<p
			class="modalHeader text-white absolute top-4 left-4 font-bold text-3xl [text-shadow:_0_0_5px_rgb(0_0_0)] select-none"
		>
			{project ? project : ''}
		</p>
		<!-- Carousel -->
	</div>
	<!-- Close when click outside -->
	<form method="dialog" class="modal-backdrop">
		<button class="invisible"></button>
	</form>
</dialog>
