<script>
	export let data;

	export let post;

	const URL = 'https://www.free-lands.com/';

	let related = data.posts.filter((p) => p.project === post.project);

	let index = related.findIndex((p) => p.id === post.id);
</script>

<button
	class="brick {post.size} p-0 border-0 rounded-xl hover:shadow-[0_0_20px_10px_rgba(0,0,0,0.7)] overflow-hidden"
	on:click={() => {
		window.history.replaceState(null, document.title, '#' + post.project + '.' + index);
		document.getElementById(post.project.toString() + '.' + index).classList.remove('hidden');
		document.getElementById(post.project.toString() + '.' + index).style.display = 'block';
		document.getElementById(post.project).showModal();
	}}
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

<!-- <Modal {post} {related} /> -->
