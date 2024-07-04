<script>
	export let project;

	export let language;

	export let translations;

	const URL = 'https://www.free-lands.com/';

	let images = [];

	/**
	 * Add all images of the same project to the images array
	 * @param id The id of the project ('000.0')
	 * @param src The source of the image ('https://www.free-lands.com/000.0_modal.jpeg')
	 * @param text The description of the image ('A small description of the image')
	 * @param link The external referneces link to the image ('https://www.wikipedia.com/')
	 * @param prev The id of the previous image of the project ('#000.0')
	 * @param next The id of the next image of the project ('#000.0')
	 * */
	project.posts.forEach((post) => {
		images.push({
			id: project.id.toString() + '.' + project.posts.indexOf(post),
			src: getSrc(post.image),
			text: getTranslation(post),
			link: post.link,
			prev: getRef(project.posts.indexOf(post), -1),
			next: getRef(project.posts.indexOf(post))
		});
	});

	/**
	 * Get the translation of the post
	 * @param post The post to translate
	 */
	function getTranslation(post) {
		let text = undefined;
		post.translations.forEach((number) => {
			translations.forEach((t) => {
				if (number === t.id && t.languages_id === language) {
					text = t.text;
				}
			});
		});
		return text;
	}

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
		return URL + img + '_modal.jpeg';
	}

	/**
	 * Set the size of the carousel according to the image size
	 * @param dir The direction of the carousel (1 for next, -1 for previous)
	 */
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

	/**
	 * Handle the resize of the carousel when called
	 * @param dir The direction of the carousel (1 for next, -1 for previous)
	 */
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
			<!-- Image -->
			<img id={'img.' + image.id} src={image.src} loading="lazy" alt={project.id} class="w-full" />
			<!-- Text -->
			<a
				href={image.link}
				target="_blank"
				id={'text.' + image.id}
				class="text absolute bottom-4 left-4 text-white text-xl p-2 capitalize">{image.text}</a
			>
			<!-- Navigation -->
			<div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
				<a href={image.prev} on:click={handleSetSize(-1)} class="btn btn-circle">❮</a>
				<a href={image.next} on:click={handleSetSize(1)} class="btn btn-circle">❯</a>
			</div>
		</div>
	{/each}
</div>
