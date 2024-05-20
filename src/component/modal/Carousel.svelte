<script>
	export let related;

	let image = [];

	console.log(related);

	const URL = 'https://www.free-lands.com/';

	// const BLACK = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/A_black_image.jpg/800px-A_black_image.jpg'

	related.forEach((rel) => {
		image.push({
			project: rel.project,
			id: rel.project.toString() + '.' + related.indexOf(rel),
			src: getSrc(rel),
			text: rel.text,
			link: rel.link,
			prev: getRef(rel, related.indexOf(rel), -1),
			next: getRef(rel, related.indexOf(rel))
		});
	});

	function getRef(post, i, dir = 1) {
		let ref = i + dir;
		if (ref < 0) ref = related.length - 1;
		if (ref >= related.length) ref = 0;
		return '#' + post.project.toString() + '.' + ref;
	}

	function getSrc(post) {
		return URL + post.image + '_modal.jpeg';
	}
</script>

<div class="carousel carousel-center relative flex lg:max-w-[900px] max-w-screen w-fit">
	{#each image as img}
		<div class="carousel-item relative">
			<img src={img.src} loading="lazy" alt={img.project} class="lg:w-full aspect-[3/2] w-screen" />
			{#if img.text}
				<p class="absolute bottom-4 left-4 text-white text-xl p-2 capitalize">{img.text}</p>
			{/if}
			{#if img.link}
				<button
					href={img.link}
					class="btn btn-circle btn-ghost w-auto absolute bottom-4 right-4 text-white text-2xl [text-shadow:_0_0_5px_rgb(0_0_0)]"
					>🔗</button
				>
			{/if}
			<div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
				<button href={img.prev} class="btn btn-circle">❮</button>
				<button href={img.next} class="btn btn-circle">❯</button>
			</div>
		</div>
	{/each}
</div>
