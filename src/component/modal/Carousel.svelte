<script>
	import { onMount } from 'svelte';

	export let project;

	let images = [];

	const URL = 'https://www.free-lands.com/';

	// const BLACK = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/A_black_image.jpg/800px-A_black_image.jpg'

	project.posts.forEach((post) => {
		images.push({
			id: project.id.toString() + '.' + project.posts.indexOf(post),
			src: getSrc(post),
			text: post.text,
			link: post.link,
			prev: getRef(project.posts.indexOf(post), -1),
			next: getRef(project.posts.indexOf(post))
		});
	});

	function getRef(i, dir = 1) {
		let index = i + dir;
		if (index < 0) index = project.posts.length - 1;
		if (index >= project.posts.length) index = 0;
		return '#' + project.id.toString() + '.' + index;
	}

	function getSrc(post) {
		return URL + post.image + '_modal.jpeg';
	}

	function setSize(dir) {
		let carousel = document.getElementById('carousel.' + project.id);
		let index = Number(window.location.href.split('#')[1].split('.')[1]);

		index = index + dir;
		if (index < 0) index = project.posts.length - 1;
		if (index >= project.posts.length) index = 0;

		let image = document.getElementById('img.' + project.id + '.' + index);

		if (window.innerWidth > image.naturalWidth) {
			carousel.style.maxWidth = image.naturalWidth + 'px';
			carousel.style.maxHeight = image.naturalHeight + 'px';
		} else {
			carousel.style.maxWidth = window.innerWidth + 'px';
			carousel.style.maxHeight = (2 * image.width) / 3 + 'px';
		}
	}

	function handleSetSize(dir) {
		return (event) => {
			setSize(dir);
		};
	}
</script>

<div
	id={'carousel.' + project.id}
	class="carousel relative transition-all duration-200 lg:max-w-[900px] max-h-fit max-w-screen flex w-fit"
>
	{#each images as image}
		<div id={image.id} class="carousel-item relative w-fit">
			<img id={'img.' + image.id} src={image.src} loading="lazy" alt={project.id} class="w-full" />
			{#if image.text}
				<p class="absolute bottom-4 left-4 text-white text-xl p-2 capitalize">{image.text}</p>
			{/if}
			{#if image.link}
				<a
					href={image.link}
					class="btn btn-circle w-auto absolute bottom-4 right-4 text-white text-2xl [text-shadow:_0_0_5px_rgb(0_0_0)]"
					>🔗</a
				>
			{/if}
			<div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
				<a href={image.prev} on:click={handleSetSize(-1)} class="btn btn-circle">❮</a>
				<a href={image.next} on:click={handleSetSize(1)} class="btn btn-circle">❯</a>
			</div>
		</div>
	{/each}
</div>
