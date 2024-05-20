<script>
	export let post;

	const URL = 'https://www.free-lands.com/';

	function openModal() {
		const modal = document.getElementById(post.project);
		modal.showModal();
	}
</script>

<button
	class="brick {post.size} p-0 border-0 rounded-xl hover:shadow-[0_0_20px_10px_rgba(0,0,0,0.7)] overflow-hidden"
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
