<script>
    export let post;

    export let related;

    // export let language = 'en-US';

    const URL = 'https://www.free-lands.com/';

    // const BLACK = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/A_black_image.jpg/800px-A_black_image.jpg'

    let src = URL + post.image + '_modal.jpeg';

    let index = related.findIndex(p => p.id === post.id);

    function getRef(post, i, dir) {
        let ref = i + dir;
        if (ref < 0) ref = related.length - 1;
        if (ref >= related.length) ref = 0;
        return '#' + post.project.toString() + '.' + ref;
    }

    function rewriteClass(id, className, add = true) {
        let element = document.getElementById(id);
        if (!element) return;
        if (add) {
            element.classList.add(className);
            Array.from(element.children).forEach(child => child.classList.add(className));
        } else {
            element.classList.remove(className);
            Array.from(element.children).forEach(child => child.classList.remove(className));
        }
    }

    function skip(forward = 1) {
        let ref = getRef(post, index, -1);
        window.history.replaceState(null, document.title, ref);

        rewriteClass(post.project.toString() + '.' + index, 'hidden', true);

        index += forward;
        if (index < 0) index = related.length - 1;
        else if (index >= related.length) index = 0;
        post = related[index];

        rewriteClass(post.project.toString() + '.' + index, 'hidden', false);
    }


</script>
<div class="carousel w-fit select-none">
    {#each related as rel, i}
        {#if rel.id !== post.id}
            <div id={post.project.toString() + '.' + i} class="carousel-item relative w-fit hidden">
                <img src="{src}" loading="lazy" alt="{rel.project}" class="w-full hidden" />
                <p class="absolute bottom-0 left-0 text-white text-xl font-bold p-2 hidden">{rel.text ? rel.text : ''}</p>
                <div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2 hidden">
                    <button on:click={skip(-1)} class="btn btn-circle select-none">❮</button> 
                    <button on:click={skip()} class="btn btn-circle select-none">❯</button>
                </div>
            </div>
        {:else}
            <div id={post.project.toString() + '.' + i} class="carousel-item relative w-fit">
                <img src="{src}" loading="lazy" alt="{rel.project}" class="w-full" />
                <p class="absolute bottom-0 left-0 text-white text-xl font-bold p-2">{rel.text ? rel.text : ''}</p>
                <div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
                    <button on:click={skip(-1)} class="btn btn-circle select-none">❮</button> 
                    <button on:click={skip()} class="btn btn-circle select-none">❯</button>
                </div>
            </div>
        {/if}
    {/each}
</div>

