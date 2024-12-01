<script>
	import { postTranslations } from '$lib/stores/translations';
	export let project;

	const LINK = 'https://admin.lands.swiss/assets/';

	$: images = project.posts.map((post) => {
		return {
			id: project.id.toString() + '.' + project.posts.indexOf(post),
			src: getSrc(post.image),
			text: post.text,
			post: post,
			link: post.link,
			prev: getRef(project.posts.indexOf(post), -1),
			next: getRef(project.posts.indexOf(post)),
			date: post.date
		};
	});

	/**
	 * Get the reference of the next or previous image
	 * @param i The index of the current image
	 * @param dir The direction of the reference (1 for next, -1 for previous)
	 */
	function getRef(i, dir = 1) {
		let index = i + dir;
		if (index < 0) index = project.posts.length - 1;
		if (index >= project.posts.length) index = 0;
		return '#' + project.id.toString() + '.' + index;
	}

	/**
	 * Get the source of the image
	 * @param img The image name
	 */
	function getSrc(img) {
		return LINK + img + '?key=modal';
	}

	/**
	 * Set the size of the carousel according to the image size
	 * @param dir The direction of the carousel (1 for next, -1 for previous)
	 */
	function setSize(dir) {
		const carousel = document.getElementById('carousel.' + project.id);
		let index = Number(window.location.href.split('#')[1].split('.')[1]);

		index = index + dir;
		if (index < 0) index = project.posts.length - 1;
		if (index >= project.posts.length) index = 0;

		const imageId = project.id.toString() + '.' + index;
		const image = document.getElementById('img.' + imageId);
		const text = document.getElementById('text.' + imageId);
		const link = document.getElementById('link.' + imageId);

		if (window.innerWidth > image.naturalWidth) {
			carousel.style.maxWidth = image.naturalWidth + 'px';
			carousel.style.maxHeight = image.naturalHeight + 'px';
			if (link != null && link.offsetWidth != null && text != null) {
				text.style.maxWidth = image.naturalWidth / 2 - link.offsetWidth / 2 + 'px';
			}
			if (link != null && link.offsetWidth != null) {
				link.style.left = image.naturalWidth / 2 - link.offsetWidth / 2 + 'px';
			}
		} else {
			carousel.style.maxWidth = window.innerWidth + 'px';
			carousel.style.maxHeight = (2 * image.width) / 3 + 'px';
			if (link != null && link.offsetWidth != null && text != null) {
				text.style.maxWidth = window.innerWidth / 2 - link.offsetWidth / 2 + 'px';
			}
			if (link != null && link.offsetWidth != null) {
				link.style.left = window.innerWidth / 2 - link.offsetWidth / 2 + 'px';
			}
		}
	}

	/**
	 * Handle the resize of the carousel when called
	 * @param dir The direction of the carousel (1 for next, -1 for previous)
	 */
	function handleSetSize(dir) {
		return () => {
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
			<!-- Image -->
			<img id={'img.' + image.id} src={image.src} loading="lazy" alt={project.id} class="w-full" />
			<!-- Text -->
			{#if $postTranslations[image.post.id]}
				<p
					id={'text.' + image.id}
					class="absolute lg:bottom-4 bottom-2 lg:left-4 left-2 lg:text-xl text-sm uppercase p-2 text-white ![text-shadow:_0_0_20px_rgb(0_0_0_/_90%)]"
				>
					{$postTranslations[image.post.id]}
				</p>
			{/if}
			{#if image.link}
				<a
					href={image.link}
					target="_blank"
					id={'link.' + image.id}
					class="absolute btn btn-circle lg:bottom-4 bottom-2 text-xl uppercase p-2 text-white ![text-shadow:_0_0_20px_rgb(0_0_0_/_90%)]"
					>{'🔗'}</a
				>
			{/if}
			{#if image.date}
				<p
					id={'date.' + image.id}
					class="absolute lg:bottom-4 bottom-2 lg:right-4 right-2 lg:text-xl text-sm p-2 text-white ![text-shadow:_0_0_20px_rgb(0_0_0_/_90%)]"
				>
					{image.date}
				</p>
			{/if}
			<!-- Navigation -->
			<div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
				<a href={image.prev} on:click={handleSetSize(-1)} class="btn btn-circle">❮</a>
				<a href={image.next} on:click={handleSetSize(1)} class="btn btn-circle">❯</a>
			</div>
		</div>
	{/each}
</div>
