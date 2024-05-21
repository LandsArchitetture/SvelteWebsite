<script>
	export let data;

	export let post;

	let related = data.posts.filter((p) => p.project === post.project);

	const URL = 'https://www.free-lands.com/';

	let index = related.indexOf(post);

	function openModal() {
		const modal = document.getElementById(post.project);
		const carousel = document.getElementById('carousel.' + post.project);
		const image = document.getElementById('img.' + post.project + '.' + index);

		if (window.innerWidth > image.naturalWidth) {
			carousel.style.maxWidth = image.naturalWidth + 'px';
			carousel.style.maxHeight = image.naturalHeight + 'px';
		} else {
			carousel.style.maxWidth = window.innerWidth + 'px';
			carousel.style.maxHeight = (2 * image.width) / 3 + 'px';
		}

		modal.showModal();

		window.location.hash = post.project + '.' + index;
	}
</script>

<button
	class="brick {post.size} p-0 border-0 rounded-xl hover:shadow-[0_0_20px_10px_rgba(0,0,0,0.7)] hover:scale-[103%] overflow-hidden"
	on:click={openModal}
>
	<img
		id={post.id + '_' + post.size}
		class="object-cover w-full"
		loading="lazy"
		src={URL + post.image + '_' + post.size + '.jpeg'}
		alt={post.project}
	/>
	<p
		class="project text-white [text-shadow:_0_0_5px_rgb(0_0_0)] absolute top-0 left-2 text-xl font-bold"
	>
		{post.project}
	</p>
	<p class="date text-white [text-shadow:_0_0_5px_rgb(0_0_0)] absolute bottom-0 right-2 text-sm">
		{post.date}
	</p>
</button>
