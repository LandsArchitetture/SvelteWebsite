<script>
	import Carousel from './Carousel.svelte';

	export let project;
</script>

<dialog id={project.id} class="modal">
	<div class="modal-box flex p-0 w-fit max-w-fit max-h-fit select-none">
		<!-- Carousel -->
		<Carousel {project} />
		<!-- Close button -->
		<form method="dialog">
			<button
				class="btn btn-sm btn-circle btn-ghost absolute right-4 top-4 text-red-700 text-2xl [text-shadow:_0_0_5px_rgb(0_0_0)]"
				>✕</button
			>
		</form>
		<!-- Header -->
		<p
			class="modalHeader text-white absolute top-4 left-4 font-bold text-3xl [text-shadow:_0_0_5px_rgb(0_0_0)] select-none"
		>
			{project.id ? project.id : ''}
		</p>
	</div>
	<!-- Close when click outside -->
	<form method="dialog" class="modal-backdrop">
		<button>✕</button>
	</form>
</dialog>
