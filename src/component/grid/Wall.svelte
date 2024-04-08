<script>
    import { onMount } from 'svelte';
    import Card from './Card.svelte';

    export let data;

    let wall;

    function resizeBig(wall) {
        wall.reset({
            selector: '.brick',
            cellW: 200,
            cellH: 200,
            gutterY: 5,
            gutterX: 5,
        })
        wall.fixSize({ block: '.1x1', width: 200, height: 200 })
        wall.fixSize({ block: '.2x1', width: 200, height: 400 })
        wall.fixSize({ block: '.1x2', width: 400, height: 200 })
        wall.fixSize({ block: '.2x2', width: 400, height: 400 })
        wall.fixSize({ block: '.3x3', width: 600, height: 600 })
        wall.fixSize({ block: '.3x2', width: 400, height: 600 })
        wall.fixSize({ block: '.2x3', width: 600, height: 400 })
    };

    function resizeSmall(wall) {
        wall.reset({
            selector: '.brick',
            cellW: 100,
            cellH: 100,
            gutterY: 2,
            gutterX: 2,
        })

        wall.fixSize({ block: '.1x1', width: 100, height: 100 })
        wall.fixSize({ block: '.2x1', width: 100, height: 200 })
        wall.fixSize({ block: '.1x2', width: 200, height: 200 })
        wall.fixSize({ block: '.2x2', width: 200, height: 200 })
        wall.fixSize({ block: '.3x3', width: 300, height: 300 })
        wall.fixSize({ block: '.3x2', width: 200, height: 300 })
        wall.fixSize({ block: '.2x3', width: 300, height: 200 })
    };

    function adapt(wall) {
        if (window.innerWidth < 500) resizeSmall(wall)
        else resizeBig(wall)
        wall.fitWidth()
    };

    onMount(async () => {
        if (typeof window === 'undefined') return
        let freewall = (await import('freewall')).default
        wall = new freewall.Freewall('#container')
        adapt(wall)

        /* If the screen change resize to fit width */
        window.addEventListener('resize', event => {
            adapt(wall)
        });
    });

    let posts = data.posts;
    let post = posts[0];

</script>

<div id="container" class="flex">
    <!-- <Card data={data} {...post}/> -->
    {#each posts as post}
        <Card data={data} {...post} />
    {/each}
</div>
