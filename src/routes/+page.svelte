<script>
    import Wall from "../component/grid/Wall.svelte";
    import Navbar from "../component/navbar/Navbar.svelte";
    import { createDirectus, rest, readItems, readFiles } from '@directus/sdk';
    import { setContext } from 'svelte';

    const getStaticProps = async () => {
        const directus = createDirectus('https://admin.lands.swiss/').with(rest());

        const posts = await directus.request(readItems('posts',{sort: '-date', limit: -1}));
        const projects = await directus.request(readItems('projects',{limit: -1}));
        const files = await directus.request(readFiles({limit: -1}));
        const posts_translations = await directus.request(readItems('posts_translations',{limit: -1}));
        const languages = await directus.request(readItems('languages',{limit: -1}));

        return {
            props: {
                posts,
                projects,
                files,
                posts_translations,
                languages
            }
        }
    }

    const data = getStaticProps();

    setContext('projects', data.projects);
    setContext('posts', data.posts);
    setContext('files', data.files);
    setContext('posts_translations', data.posts_translations);
    setContext('languages', data.languages);




</script>


<Navbar>
    <div class="freewall m-2">
        <Wall />
    </div>
</Navbar>


