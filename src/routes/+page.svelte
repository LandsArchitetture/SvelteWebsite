<script>
	import Wall from '../component/grid/Wall.svelte';
	import Modal from '../component/modal/Modal.svelte';
	import Navbar from '../component/navbar/Navbar.svelte';
	import AboutModal from '../component/navbar/menu/AboutModal.svelte';
	import ContactModal from '../component/navbar/menu/ContactModal.svelte';
	import { createDirectus, rest, readItems, readFiles } from '@directus/sdk';
	import {
		loadPostTranslations,
		loadNavbarTranslations,
		updateLanguage
	} from '$lib/stores/translations';

	let isLoading = true;
	let data;
	let all_posts = [];
	let filtered = [];
	let TYPES = ['progetto', 'concorso', 'edificio', 'varie'];

	/**
	 * Fetch the data from the Directus API and reorder them in
	 * @param data The data fetched from the Directus API
	 * @param all_posts The list of all the posts
	 * @param filtered The list of the filtered posts
	 */
	(async () => {
		try {
			const directus = createDirectus('https://admin.lands.swiss/').with(rest());
			const posts = await directus.request(readItems('posts', { sort: '-date', limit: -1 }));
			const projects = await directus.request(readItems('projects', { limit: -1 }));
			const files = await directus.request(readFiles({ limit: -1 }));
			const languages = await directus.request(readItems('languages', { limit: -1 }));
			// await loadPostTranslations(directus);
			// await loadNavbarTranslations();
			// updateLanguage();

			data = { posts, projects, files, languages };
			console.log('Data fetched:', data);
			all_posts = data.posts;
			filtered = all_posts;
		} catch (error) {
			console.error('Failed to fetch data:', error);
		} finally {
			data.projects.forEach((proj) => {
				proj['posts'] = [];
				data.posts.forEach((post) => {
					if (post.project === proj.id) {
						proj.posts.push(post);
					}
				});
			});
			isLoading = false;
		}
	})();

	/**
	 * Filter the posts according to the filter
	 * @param filter The filter to apply
	 * @param posts The list of all the posts
	 */
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

	/**
	 * Filter the projects according to the corresponding string in TYPES
	 * @param filter The filter to apply
	 */
	function specialFilter(filter) {
		let filterProjects = [];
		data.projects.filter((proj) =>
			proj.type.forEach((type) => {
				if (type.toLowerCase() == filter) {
					filterProjects.push(proj);
				}
			})
		);
		let filterPosts = [];
		filterProjects.reverse().forEach((proj) => {
			if (proj.posts.length > 0) {
				filterPosts.push(proj.posts[0]);
			}
		});
		filtered = filterPosts;
	}

	/**
	 * Handle the filter event by choosing the right filter
	 * @param event The event to handle
	 */
	function handleFilter(event) {
		let filter = event.detail.text.toLowerCase();
		if (filter == '') {
			filtered = all_posts;
		} else if (TYPES.includes(filter)) {
			specialFilter(filter);
		} else {
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
		<div class="freewall m-2 select-none">
			<Wall posts={filtered} projects={data.projects} />
			{#each data.projects as proj}
				<Modal project={proj} />
			{/each}
			<AboutModal />
			<ContactModal />
		</div>
	</Navbar>
{/if}
