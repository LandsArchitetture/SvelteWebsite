<script>
	import { setContext } from "svelte";
    import Wall from "../component/grid/Wall.svelte";
    import Navbar from "../component/navbar/Navbar.svelte";
    import { createDirectus, rest, readItems, readFiles } from '@directus/sdk';

    let isLoading = true;
    let data = undefined;

    (async () => {
        try {
            const directus = createDirectus('https://admin.lands.swiss/').with(rest());
            const posts = await directus.request(readItems('posts', {sort: '-date', limit: -1}));
            const projects = await directus.request(readItems('projects', {limit: -1}));
            const files = await directus.request(readFiles({limit: -1}));
            const posts_translations = await directus.request(readItems('posts_translations', {limit: -1}));
            const languages = await directus.request(readItems('languages', {limit: -1}));

            data = { posts, projects, files, posts_translations, languages };
        } catch (error) {
            console.error('Failed to fetch data:', error);
        } finally {
            isLoading = false;
        }
    })();

    if (typeof data !== 'undefined') {
        setContext('posts', data.posts.data);
        setContext('projects', data.projects.data);
        setContext('files', data.files.data);
        setContext('translations', data.posts_translations.data);
        setContext('languages', data.languages.data);
    }
</script>

{#if isLoading}
<div class="h-screen flex justify-center items-center">
    <div class="loading loading-lg">
        <span class="loading loading-dots loading-lg "></span>
    </div>
</div>
{:else}
    <Navbar>
        <div class="freewall m-2">
            <Wall {data} />
        </div>
    </Navbar>
{/if}
