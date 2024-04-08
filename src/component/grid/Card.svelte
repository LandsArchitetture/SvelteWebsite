<script>

    export let data;

    export let id;
    export let date;
    export let project;
    // export let tags;
    export let image;
    // export let location;
    export let size = 'modal';
    // export let link;

    const URL = 'https://www.free-lands.com/';

    let relatedPosts = data.posts.filter(post => post.project === project);


</script>

<button class="brick {size} p-0 border-0 rounded-xl hover:shadow-[0_0_20px_10px_rgba(0,0,0,0.7)] overflow-hidden" on:click={()=>document.getElementById(project).showModal()}>
    <img id={id + '_' + size} class="object-cover w-full" loading="lazy" src="{URL + image + '_' + size + '.jpeg'}" alt="{project}"/>
    <p class="project text-white [text-shadow:_0_0_5px_rgb(0_0_0)] absolute top-0 left-2 text-xl font-bold">{project}</p>
    <p class="date text-white [text-shadow:_0_0_5px_rgb(0_0_0)] absolute bottom-0 right-2 text-sm">{date}</p>
</button>

<dialog id={project} class="modal">
    <div class="modal-box w-11/12 max-w-5xl p-0">
        <div class="carousel w-full">
            {#each relatedPosts as post, i}
                <div id={i} class="carousel-item relative w-full">
                    <img src="{URL + post.image + '_modal.jpeg'}" loading="lazy" alt="{project}" class="w-full" />
                    <div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
                        <a href={'#slide' + (i-1)} class="btn btn-circle">❮</a> 
                        <a href={'#slide' + (i+1)} class="btn btn-circle">❯</a>
                    </div>
                </div>
            {/each}
        </div>
        <!-- Close button -->
        <form method="dialog">
            <button class="btn btn-sm btn-circle btn-ghost absolute right-4 top-4 text-red-700 scale-150 [text-shadow:_0_0_5px_rgb(0_0_0)]">✕</button>
        </form>
        <!-- Header -->
        <p class="modalHeader text-white absolute top-4 left-4 font-bold text-3xl [text-shadow:_0_0_5px_rgb(0_0_0)]">{project ? project : ''}</p>
        <!-- Carousel -->
    </div>
    <!-- Close when click outside -->
    <form method="dialog" class="modal-backdrop">
        <button>close</button>
    </form>
</dialog>