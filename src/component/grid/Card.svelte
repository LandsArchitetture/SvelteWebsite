<script>
	export let post;

	export let project;

	const LINK = 'https://admin.lands.swiss/assets/';

	let index = project.posts.indexOf(post);

	function openModal() {
		index = project.posts.indexOf(post);
		const modal = document.getElementById(post.project);
		const carousel = document.getElementById('carousel.' + post.project);
		const imageId = post.project + '.' + index;
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

		modal.showModal();

		window.location.hash = '';
		window.location.hash = post.project + '.' + index;
	}

	function error(name, id, size) {
		let image = document.getElementById(id + '_' + size);
		image.src =
			'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/A_black_image.jpg/800px-A_black_image.jpg';
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
		src={LINK + post.image + '?key=' + post.size}
		on:error={error(post.image, post.id, post.size)}
		alt={post.image}
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
