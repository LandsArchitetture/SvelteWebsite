<script>
	export let data;

	export let related;

	export let project;

	// let post = data.posts.find((p) => p.id === data.projects[0].id);

	// export let language = 'en-US';

	const URL = 'https://www.free-lands.com/';

	// const BLACK = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/A_black_image.jpg/800px-A_black_image.jpg'

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

<div class="w-fit relative carousel">
	{#each related as rel, i}
		<div id={project.toString() + '.' + i} class="carousel-item w-fit">
			<img src={getSrc(rel)} loading="lazy" alt={rel.project} class="w-full aspect-auto" />
			<p class="absolute bottom-4 left-0 text-white text-xl font-bold p-2">
				{rel.text ? rel.text : ''}
			</p>
		</div>
		<div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
			<button href={getRef(rel, i, -1)} class="btn btn-circle select-none">❮</button>
			<button href={getRef(rel, i)} class="btn btn-circle select-none">❯</button>
		</div>
	{/each}
</div>
