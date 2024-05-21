<script>
	import Wall from '../component/grid/Wall.svelte';
	import Modal from '../component/modal/Modal.svelte';
	import Navbar from '../component/navbar/Navbar.svelte';
	import { createDirectus, rest, readItems, readFiles } from '@directus/sdk';

	let isLoading = true;
	let data = undefined;
	let all_posts = [];
	let filtered = [];

	(async () => {
		try {
			const directus = createDirectus('https://admin.lands.swiss/').with(rest());
			const posts = await directus.request(readItems('posts', { sort: '-date', limit: -1 }));
			const projects = await directus.request(readItems('projects', { limit: -1 }));
			const files = await directus.request(readFiles({ limit: -1 }));
			const posts_translations = await directus.request(
				readItems('posts_translations', { limit: -1 })
			);
			const languages = await directus.request(readItems('languages', { limit: -1 }));

			data = { posts, projects, files, posts_translations, languages };
			all_posts = data.posts;
			filtered = all_posts;
		} catch (error) {
			console.error('Failed to fetch data:', error);
		} finally {
			isLoading = false;
		}
	})();

	function filterPosts(posts, filter) {
		filtered = posts.filter((post) => {
			if (post.location.toLowerCase().includes(filter)) {
				return post;
			} else if (post.project.toLowerCase().includes(filter)) {
				return post;
			} else if (post.text && post.text.toLowerCase().includes(filter)) {
				return post;
			} else if (post.tags && post.tags.some((tag) => tag.toLowerCase().includes(filter))) {
				return post;
			}
		});
	}

	function handleFilter(event) {
		let filter = event.detail.text.toLowerCase();
		if (filter === '') {
			filtered = all_posts;
		} else if (all_posts.length > 0) {
			filterPosts(all_posts, filter);
		}
	}
</script>

{#if isLoading}
	<div class="h-screen flex justify-center items-center">
		<div class="loading loading-lg">
			<span class="loading loading-dots loading-lg"></span>
		</div>
	</div>
{:else}
	<Navbar on:filter={handleFilter}>
		<div class="freewall m-2">
			<Wall {data} posts={filtered} />
			{#each data.projects as proj}
				<Modal {data} project={proj.id} />
			{/each}
		</div>
	</Navbar>
{/if}
